import requests
import streamlit as st
from utils import format_docx, format_pdf, format_html_preview, sanitize_text

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main-title { text-align:center; font-size:42px; font-weight:700; }
    .subtitle { text-align:center; color:#777; margin-bottom:25px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">⚖️ LegalEase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True
)

if "document" not in st.session_state:
    st.session_state.document = ""

backend_url = st.sidebar.text_input(
    "FastAPI Backend URL",
    value="http://localhost:8000"
)

st.subheader("Create a Legal Document")

document_type = st.text_input(
    "Document Type",
    placeholder="e.g. NDA, Employment Contract, Lease Agreement"
)

parties = st.text_area(
    "Parties Involved",
    placeholder="e.g. Jane Doe (Service Provider), ABC Corp (Client)"
)

terms = st.text_area(
    "Terms & Conditions",
    placeholder="Separate clauses with semicolons (;)"
)

dates = st.text_input(
    "Effective Date",
    placeholder="e.g. 10/04/2026"
)

if st.button("Generate Document", type="primary"):
    if not all([document_type, parties, terms, dates]):
        st.error("Please fill in all fields.")
    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }

        try:
            with st.spinner("Generating your document..."):
                response = requests.post(
                    f"{backend_url.rstrip('/')}/generate",
                    json=payload,
                    timeout=120
                )
                response.raise_for_status()
                st.session_state.document = response.json()["document"]
            st.success("Document generated successfully.")
        except requests.RequestException as exc:
            st.error(f"Backend connection failed: {exc}")

if st.session_state.document:
    st.subheader("Document Preview")

    st.markdown(
        format_html_preview(st.session_state.document),
        unsafe_allow_html=True
    )

    st.subheader("Edit Document")
    edited = st.text_area(
        "You can edit the generated document here:",
        value=st.session_state.document,
        height=400
    )
    st.session_state.document = edited

    clean_text = sanitize_text(st.session_state.document)
    docx_data = format_docx(clean_text, document_type or "Legal Document")
    pdf_data = format_pdf(clean_text, document_type or "Legal Document")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            "Download TXT",
            data=clean_text,
            file_name="legalease_document.txt",
            mime="text/plain"
        )

    with col2:
        st.download_button(
            "Download DOCX",
            data=docx_data,
            file_name="legalease_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    with col3:
        st.download_button(
            "Download PDF",
            data=pdf_data,
            file_name="legalease_document.pdf",
            mime="application/pdf"
        )

st.divider()
st.caption(
    "LegalEase generates drafts for informational purposes. "
    "Have important legal documents reviewed by a qualified legal professional."
)

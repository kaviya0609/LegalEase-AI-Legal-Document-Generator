# ⚖️ LegalEase — AI-Powered Legal Document Generator

LegalEase is a student-friendly full-stack project that uses **Streamlit**, **FastAPI**, and **Google Gemini** to generate editable legal-document drafts.

The project is based on the supplied LegalEase project specification, which describes legal document generation, editable previews, and TXT/DOCX/PDF export. 

## Features

- AI-powered legal document drafting
- Document types such as:
  - Employment Contract
  - NDA
  - Lease Agreement
  - General Agreement
  - Contract
- Inputs for:
  - Document type
  - Parties
  - Terms and conditions
  - Effective date
- FastAPI `POST /generate` endpoint
- Streamlit web interface
- Editable document preview
- TXT export
- DOCX export
- PDF export
- Environment-variable API key configuration
- Demo fallback mode when Gemini API key is not configured

## Project Structure

```text
LegalEase/
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
├── app.py
├── main.py
├── routes.py
├── utils.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Install Python

Use Python 3.10+.

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Gemini

Copy `.env.example` to `.env`:

```text
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-1.5-pro
```

Do **not** upload `.env` to GitHub.

## 5. Start FastAPI

```bash
uvicorn main:app --reload
```

API:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

## 6. Start Streamlit

Open another terminal with the virtual environment activated:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## 7. Test

Enter:

- Document Type: `Non-Disclosure Agreement`
- Parties: `Jane Doe (Disclosing Party), ABC Corp (Receiving Party)`
- Terms: `Confidential information must be protected; Disclosure is prohibited without written permission; Agreement may be terminated by either party`
- Effective Date: `10/04/2026`

Click **Generate Document**.

You can then edit the generated document and download it as:

- `.txt`
- `.docx`
- `.pdf`

## API Example

### POST `/generate`

Request:

```json
{
  "document_type": "Employment Contract",
  "parties": "Jane Doe (Employee), ABC Corp (Employer)",
  "terms": "Salary will be paid monthly; Employee must maintain confidentiality",
  "dates": "10/04/2026"
}
```

Response:

```json
{
  "success": true,
  "document": "Generated legal document..."
}
```

## GitHub Upload

After extracting this ZIP:

```bash
git init
git add .
git commit -m "Initial LegalEase project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Or upload the extracted files directly through GitHub's web interface.

## Important

LegalEase is a document-drafting project and does not replace advice from a qualified lawyer. Generated content should be reviewed before real-world legal use.

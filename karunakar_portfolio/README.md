# Karunakar Reddy — Data Analyst Portfolio

A single-page, responsive portfolio website built with Python and Streamlit. It presents a profile, skill groups, project summaries, education, certifications, resume download, and contact links.

## Design

- Dark charcoal/forest-green theme with emerald accents
- Single scrolling page with anchor navigation (no sidebar navigation)
- Responsive layout for desktop and mobile
- Resume download when `assets/resume.pdf` is present
- Certificate cards link directly to the matching Google Drive files

## Project structure

```text
karunakar_portfolio/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    ├── README.md
    ├── resume.pdf                 # add your own PDF
    └── certificates/              # optional certificate images/PDFs
```

## Run locally

1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Create and activate a virtual environment if you use one.
4. Install packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the site:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Before publishing

Open `app.py` and update `EMAIL`, `PHONE`, `LOCATION`, `LINKEDIN_URL`, and `GITHUB_URL` with your current details. Check education dates, certificate names, and project descriptions against your source documents. Replace any generic links with actual project repositories or dashboards. Do not publish placeholder or unverified information.

The provided resume is included at `assets/resume.pdf`. Certificate cards are linked to the Google Drive URLs supplied by the portfolio owner. Make sure each Drive file is shared as **Anyone with the link — Viewer** so recruiters can open it.

## Deploy to a permanent public URL

1. Create a GitHub repository and upload these files.
2. In Streamlit Community Cloud, create an app from that repository and choose `app.py` as the entry point.
3. Deploy and test the public URL.
4. Add the same public URL to your resume and LinkedIn.

A hosted URL remains accessible while the hosting service, repository, and deployment remain active and within their service terms. Keep a copy of the project in GitHub.

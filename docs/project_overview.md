# Abhay Sharma Portfolio

This repository contains the source code for Abhay Sharma's portfolio website and resume.

## Directory Structure

- **`website/`**: Contains the static website code (`index.html`, `blog/`, etc.).
- **`resume/`**: Contains the LaTeX source code for the resume.
- **`.github/workflows/`**: Contains GitHub Action workflows for CI/CD.
- **`docs/`**: Additional documentation.

## Workflows

### 1. Deploy to Cloudflare Pages
**File**: `.github/workflows/deploy-cloudflare.yml`

This workflow automatically deploys the website to [Cloudflare Pages](https://pages.cloudflare.com/).

- **Trigger**: Pushes to `main` or `master` branch WHERE files in `website/**` are modified.
- **Action**: Deploys the `website/` directory to Cloudflare Pages.
- **Project Name**: `abhaysharma` (configured in workflow).

### 2. Build LaTeX PDF
**File**: `.github/workflows/build-latex.yml`

This workflow compiles the LaTeX resume into a PDF.

- **Trigger**: Pushes to `main` or `master` branch WHERE files in `resume/**` are modified, or manual dispatch.
- **Action**: 
    1. Compiles `resume/2026-fullstack.tex` using `pdflatex`.
    2. Uploads the PDF as a GitHub Artifact.
    3. Uploads the PDF to `tmpfiles.org`.
    4. Sends a notification to Slack with the download link.

## Secrets & Environment Variables

To run these workflows successfully, the following Secrets must be configured in the repository settings:

| Secret Name | Description | Workflow |
| :--- | :--- | :--- |
| `CLOUDFLARE_INT_TOKEN` | API Token for Cloudflare with Pages permissions. | Deploy to Cloudflare |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare Account ID. | Deploy to Cloudflare |
| `SLACK_WEBHOOK_URL` | Webhook URL for sending notifications to Slack. | Build LaTeX PDF |

> [!NOTE]
> `CLOUDFLARE_API_TOKEN` is used in the workflow file, but standard Cloudflare docs often refer to it as just API Token. Ensure the secret name matches what is in `.github/workflows/deploy-cloudflare.yml`.

## Local Development

### Website
Simply open `website/index.html` in your browser. No build process required for the vanilla HTML/CSS/JS.

### Resume
You need a LaTeX distribution (like TeX Live) installed.
```bash
cd resume
pdflatex 2026-fullstack.tex
```

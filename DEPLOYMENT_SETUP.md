# Deployment Setup Guide

This guide explains how to configure the deployment for this portfolio to **GitHub Pages** and **Cloudflare Pages**.

## 1. GitHub Pages Configuration

To enable GitHub Pages deployment via GitHub Actions:

1. Go to your repository **Settings**.
2. Click on **Pages** in the left sidebar.
3. Under **Build and deployment** > **Source**, select **GitHub Actions**.
   - This tells GitHub to wait for the workflow to upload the artifact instead of trying to build from a branch directly.

## 2. Secrets Configuration

The following secrets need to be added to your repository's **Settings** > **Secrets and variables** > **Actions** > **Repository secrets**.

### Required for Cloudflare Pages

*   **`CLOUDFLARE_API_TOKEN`**:
    1.  Go to the [Cloudflare Dashboard](https://dash.cloudflare.com/profile/api-tokens).
    2.  Click **Create Token**.
    3.  Select the **Edit Cloudflare Workers** template (or create a custom token with **Cloudflare Pages: Edit** permissions).
    4.  Copy the generated token and save it as `CLOUDFLARE_API_TOKEN`.

*   **`CLOUDFLARE_ACCOUNT_ID`**:
    1.  Go to your [Cloudflare Dashboard](https://dash.cloudflare.com).
    2.  The Account ID is usually displayed in the URL (e.g., `dash.cloudflare.com/<ACCOUNT_ID>`) or on the right side of the dashboard overview page.
    3.  Save it as `CLOUDFLARE_ACCOUNT_ID`.

**Note:** The workflow assumes the Cloudflare Pages project name is `portfolio`. If you named it something else in Cloudflare, update the `projectName` field in `.github/workflows/deploy.yml`.

### Required for Notifications (Legacy)

*   **`SLACK_WEBHOOK_URL`**:
    - The webhook URL for the Slack channel where build notifications should be sent.

## 3. Workflow Overview

The `.github/workflows/deploy.yml` workflow performs the following steps:

1.  **Build**: Installs LaTeX and compiles `resumes/2026-fullstack.tex` into a PDF.
2.  **Prepare**: Creates a `public` directory containing `index.html`, `blog/`, `robots.txt`, and the compiled `resume.pdf`.
3.  **Deploy to GitHub Pages**: Uploads the `public` directory artifact and deploys it.
4.  **Deploy to Cloudflare Pages**: Pushes the `public` directory to Cloudflare Pages using the configured secrets.
5.  **Notify**: Sends a message to Slack with a link to the generated PDF (hosted temporarily on tmpfiles.org).

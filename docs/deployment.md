# Deploying to Cloudflare Pages

This project includes a GitHub Action workflow to automatically deploy to Cloudflare Pages on every push to the `main` or `master` branch.

## Prerequisites

1.  **Cloudflare Account**: You need a Cloudflare account.
2.  **Cloudflare Pages Project**:
    *   Go to the Cloudflare Dashboard > Pages.
    *   Create a new project.
    *   Connect your GitHub repository.
    *   Set the "Build command" to empty (or your build command if you stick to a framework later).
    *   Set the "Build output directory" to `/` (root) for this static site.
    *   **Project Name**: Note the project name you created (e.g., `abhay-portfolio`). If it's different from `abhay-portfolio`, update the `projectName` in `.github/workflows/deploy-cloudflare.yml`.

## Getting Credentials

To allow GitHub Actions to deploy to your Cloudflare Pages project, you need to provide API credentials.

1.  **Account ID**:
    *   Go to your Cloudflare Dashboard.
    *   The Account ID is usually displayed in the URL or on the right sidebar of the Overview page.

2.  **API Token**:
    *   Go to [User Profile > API Tokens](https://dash.cloudflare.com/profile/api-tokens).
    *   Click **Create Token**.
    *   Use the **Edit Cloudflare Workers** template (it covers Pages too) or create a Custom Token with:
        *   **Permissions**: `Account` > `Cloudflare Pages` > `Edit`

## Setting GitHub Secrets

1.  Go to your GitHub Repository.
2.  Navigate to **Settings** > **Secrets and variables** > **Actions**.
3.  Click **New repository secret** and add the following:

| Name | Value |
| :--- | :--- |
| `CLOUDFLARE_ACCOUNT_ID` | Your Cloudflare Account ID |
| `CLOUDFLARE_API_TOKEN` | Your Cloudflare API Token |

## Usage

Once configured, any push to the `main` or `master` branch will trigger the workflow and deploy your "brutalist" portfolio to the wild!

import os
import glob
import subprocess
import json
import sys
from urllib.request import Request, urlopen

def compile_latex(file_path):
    print(f"Compiling {file_path}...")
    # Run pdflatex. output-directory=resumes ensures PDFs stay in resumes/
    # We allow stdout to print so we can debug compilation errors in CI logs
    cmd = ["pdflatex", "-interaction=nonstopmode", "-output-directory=resumes", file_path]
    try:
        subprocess.check_call(cmd)
        print(f"Successfully compiled {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {file_path}: {e}")
        raise

def upload_file(file_path):
    print(f"Uploading {file_path}...")
    # Use curl for upload
    cmd = [
        "curl", "-s",
        "-F", f"file=@{file_path}",
        "https://tmpfiles.org/api/v1/upload"
    ]
    try:
        result = subprocess.check_output(cmd)
        response = json.loads(result)
        if 'data' in response and 'url' in response['data']:
            url = response['data']['url']
            print(f"Uploaded to {url}")
            return url
        else:
            print(f"Unexpected response from tmpfiles.org: {response}")
            return None
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
        return None

def send_slack(links):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set, skipping Slack notification.")
        return

    text = "Resume PDF Build Complete!\n\n" + "\n".join(links)
    payload = json.dumps({"text": text}).encode('utf-8')
    req = Request(webhook_url, data=payload, headers={'Content-Type': 'application/json'})

    try:
        with urlopen(req) as response:
            print(f"Slack notification sent: {response.status} {response.reason}")
    except Exception as e:
        print(f"Error sending Slack notification: {e}")

def main():
    tex_files = glob.glob("resumes/*.tex")
    if not tex_files:
        print("No .tex files found in resumes/")
        return

    links = []

    for tex_file in tex_files:
        try:
            compile_latex(tex_file)
            # The PDF should be in the same directory as the tex file because of -output-directory=resumes
            pdf_file = tex_file.replace(".tex", ".pdf")

            # Verify PDF exists
            if os.path.exists(pdf_file):
                url = upload_file(pdf_file)
                if url:
                    links.append(f"<{url}|{os.path.basename(pdf_file)}>")
            else:
                print(f"Error: Expected PDF {pdf_file} not found.")
        except Exception as e:
            print(f"Skipping {tex_file} due to error.")

    if links:
        send_slack(links)
    else:
        print("No files were successfully processed and uploaded.")

if __name__ == "__main__":
    main()

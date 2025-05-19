import os

# Get credentials from environment variables (recommended for security)
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not aws_access_key_id or not aws_secret_access_key:
    raise ValueError("Missing AWS credentials in environment variables.")

# Define YAML content
yaml_content = f"""apiVersion: v1
kind: Secret
metadata:
  name: s3creds
  annotations:
    serving.kserve.io/s3-endpoint: s3.ap-south-1.amazonaws.com
    serving.kserve.io/s3-usehttps: "1"
    serving.kserve.io/s3-region: "ap-south-1"
    serving.kserve.io/s3-useanoncredential: "false"
type: Opaque
stringData:
  AWS_ACCESS_KEY_ID: {aws_access_key_id}
  AWS_SECRET_ACCESS_KEY: {aws_secret_access_key}

---

apiVersion: v1
kind: ServiceAccount
metadata:
  name: s3-read-only
secrets:
  - name: s3creds
"""

# Ensure directory exists
os.makedirs("argo-apps", exist_ok=True)

# Write file
with open("argo-apps/s3-secret.yaml", "w") as f:
    f.write(yaml_content)

print("✅ s3-secret.yaml has been generated in the argo-apps/ folder.")

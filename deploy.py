import os
import subprocess
import sys
from dotenv import load_dotenv
import paramiko
from scp import SCPClient
from paramiko import RSAKey
from tqdm import tqdm
import io

# -------------------- Load .env --------------------
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
EC2_KEY_PATH = os.getenv("EC2_KEY_PATH")
EC2_USER = os.getenv("EC2_USER", "ec2-user")
EC2_INSTANCE_ID = os.getenv("EC2_INSTANCE_ID")
EC2_PUBLIC_IP = os.getenv("EC2_PUBLIC_IP")
PROJECT_DIR = os.getenv("PROJECT_DIR", os.path.abspath("."))

if not EC2_KEY_PATH or not EC2_PUBLIC_IP:
    raise ValueError("Missing EC2_KEY_PATH or EC2_PUBLIC_IP in .env")

# -------------------- Ensure dependencies --------------------
required_packages = ["boto3", "paramiko", "scp", "tqdm"]
for pkg in required_packages:
    try:
        __import__(pkg)
    except ImportError:
        print(f"Installing missing package: {pkg}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# -------------------- SSH Connect --------------------
print(f"🔐 Connecting to EC2 {EC2_PUBLIC_IP} ...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = RSAKey.from_private_key_file(EC2_KEY_PATH)
ssh.connect(hostname=EC2_PUBLIC_IP, username=EC2_USER, pkey=key)

# -------------------- Upload project with tqdm --------------------
def upload_file(scp, local_path, remote_path):
    """Upload a single file with tqdm progress."""
    file_size = os.path.getsize(local_path)
    with open(local_path, "rb") as f:
        file_bytes = f.read()
    file_obj = io.BytesIO(file_bytes)

    with tqdm(total=file_size, unit="B", unit_scale=True, desc=f"Uploading {os.path.basename(local_path)}") as pbar:
        def progress(sent_bytes):
            pbar.update(sent_bytes - pbar.n)
        scp.putfo(file_obj, remote_path, file_size=file_size, progress=progress)


def upload_project(ssh):
    print("📤 Uploading project to EC2...\n")
    scp = SCPClient(ssh.get_transport())
    for root, dirs, files in os.walk(PROJECT_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, PROJECT_DIR)
            remote_path = f"~/financial-fraud-agentic-system/{rel_path}"
            remote_dir = os.path.dirname(remote_path)
            ssh.exec_command(f"mkdir -p {remote_dir}")
            upload_file(scp, local_path, remote_path)
    scp.close()
    print("\n✅ Upload complete.\n")

# -------------------- Remote Deployment --------------------
commands = """
sudo apt-get update -y || sudo yum update -y

# Install Python3 and pip if missing
sudo apt-get install -y python3 python3-venv python3-pip || sudo yum install -y python3 python3-pip

cd ~/financial-fraud-agentic-system

python3 -m venv .venv
source .venv311/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Kill old processes
pkill -f "adk web" || true
pkill -f "streamlit" || true

# Start Financial Agent
nohup adk web --port 9001 > agent1.log 2>&1 &

# Start Fraud Agent
nohup adk web --port 9002 > agent2.log 2>&1 &

# Start Streamlit App
nohup streamlit run streamlit_app/app.py --server.port 8501 > streamlit.log 2>&1 &
"""

# -------------------- Run deployment --------------------
print("🚀 Executing remote deployment commands...")
stdin, stdout, stderr = ssh.exec_command(commands)
print(stdout.read().decode())
errors = stderr.read().decode()
if errors:
    print("⚠️ Errors:\n", errors)

ssh.close()

print("✅ Deployment complete!")
print(f"🌐 Streamlit UI: http://{EC2_PUBLIC_IP}:8501")
print(f"🔹 Financial Agent: http://{EC2_PUBLIC_IP}:9001")
print(f"🔹 Fraud Agent: http://{EC2_PUBLIC_IP}:9002")

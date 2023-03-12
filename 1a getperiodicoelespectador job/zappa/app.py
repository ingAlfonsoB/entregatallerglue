"""
Your module description
"""
# Import Libraries
import boto3
from datetime import datetime
from urllib.request import urlopen

# Get day
today = datetime.now().date()

# Config client of boto3
client = boto3.client("s3", "us-east-1")
bucket = "getperiodico2"
file_name = f"elespectador-{today}.html"

# Newspaper's url
url = "https://www.elespectador.com/"

# Open and save html of newspaper front page
with urlopen(url) as response:
    res = response.read()

# Put object in the bucket
client.put_object(Bucket=bucket, Body=res, Key=file_name)
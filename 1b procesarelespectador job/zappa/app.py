"""
Your module description
"""
# import libraries
from bs4 import BeautifulSoup
import boto3
from datetime import datetime

# Get day
today = datetime.now().date()

# Configure access to news raw bucket
raw_bucket = "getperiodico2"
raw_file_name = f"elespectador-{today}.html"

client = boto3.client("s3", "us-east-1")
response = client.get_object(Bucket=raw_bucket, Key=raw_file_name)

html_doc = response['Body'].read()

# Scraping html front page to get headlines
soup = BeautifulSoup(html_doc, 'html.parser')
articles = soup.find_all("article")

# Function to get the tag with the url
def get_article_url(meta):
    return meta.has_attr('itemid')

# Save headlines to csv
proccesed_headlines = "Category,Headline,Link\n" # Config headers for csv

for n in articles:
    category = n['data-category'] if n.has_attr('data-category') else None
    name = n['data-name'] if n.has_attr('data-name') else None
    url = n.find(get_article_url)['itemid'] if n.find(get_article_url) else None

    if (category and name and url):
        print(f"Category: {category}, Nombre: {name}, URL: {url}")
        proccesed_headlines += f"{category},{name},{url}\n"

# Save csv file to proccesed data bucket
# import libraries
from bs4 import BeautifulSoup
import boto3
from datetime import datetime

# Get day
today = datetime.now().date()

# Configure access to news raw bucket
raw_bucket = "getperiodico2"
raw_file_name = f"elespectador-{today}.html"

client = boto3.client("s3", "us-east-1")
response = client.get_object(Bucket=raw_bucket, Key=raw_file_name)

html_doc = response['Body'].read()

# Scraping html front page to get headlines
soup = BeautifulSoup(html_doc, 'html.parser')
articles = soup.find_all("article")

# Function to get the tag with the url
def get_article_url(meta):
    return meta.has_attr('itemid')

# Save headlines to csv
proccesed_headlines = "Category,Headline,Link\n" # Config headers for csv

for article in articles:
    category = article['data-category'] if article.has_attr('data-category') else None
    name = article['data-name'] if article.has_attr('data-name') else None
    url = article.find(get_article_url)['itemid'] if article.find(get_article_url) else None

    if (category and name and url):
        print(f"Category: {category}, Nombre: {name}, URL: {url}")
        proccesed_headlines += f"{category},{name},{url}\n"

# Save csv file to proccesed data bucket
# Config boto3 for saving file
proccesed_bucket = "procesadoperiodico2"
proccesed_file_name = f"periodico=eltiempo/year={today.year}/month={today.month}/day={today.day}/eltiempo-{today}.csv"

client.put_object(Bucket=proccesed_bucket, Body=proccesed_headlines, Key=proccesed_file_name)
proccesed_bucket = "procesadoperiodico2"
proccesed_file_name = f"periodico=eltiempo/year={today.year}/month={today.month}/day={today.day}/eltiempo-{today}.csv"

#put in s3
client.put_object(Bucket=proccesed_bucket, Body=proccesed_headlines, Key=proccesed_file_name)
import os
import re
import requests
from bs4 import BeautifulSoup

folder_name = "test"
url = "https://www.fairmont.com/fr/hotels/masai-mara/fairmont-mara-safari-club.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Clean filename
title = soup.title.string.strip() if soup.title else "untitled"
safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
file_name = safe_title + ".txt"
file_path = os.path.join(folder_name, file_name)

# Remove script/style/meta/noscript tags
for tag in soup(["script", "style", "noscript", "meta"]):
    tag.decompose()

# Extract structured content (headings, paragraphs, list items)
def extract_structured_content(soup):
    lines = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']):
        text = tag.get_text(strip=True)
        if not text:
            continue
        if tag.name == "p":
            lines.append(text + "\n\n")  # Double newline for paragraph break
        elif tag.name in ["h1", "h2", "h3"]:
            lines.append("\n" + text.upper() + "\n\n")  # Heading
        elif tag.name == "li":
            lines.append("- " + text)
    return lines

# Extract text lines
lines = extract_structured_content(soup)

# Ensure folder exists
os.makedirs(folder_name, exist_ok=True)

# Write raw structured content to main file
with open(file_path, "w", encoding="utf-8") as f:
    f.write("TITLE: " + title + "\n")
    f.write("=" * 50 + "\n\n")
    for line in lines:
        f.write(line.strip() + "\n")

# ---- MERGING LOGIC STARTS HERE ----

# Step 1: Join lines to one big text
raw_text = "\n".join(lines)

# Step 2: Split text at 4+ line breaks (3+ blank lines → new paragraph)
paragraph_candidates = re.split(r'\n{4,}', raw_text)

# Step 3: Merge close chunks (1–3 line breaks → just space)
merged_paragraphs = []
for block in paragraph_candidates:
    clean_block = re.sub(r'\n{1,3}', ' ', block.strip())  # collapse small breaks
    if clean_block:
        merged_paragraphs.append(clean_block.strip())

# Step 4: Save merged paragraphs to new file
merged_file_path = os.path.join(folder_name, safe_title + "_merged_paragraphs.txt")
with open(merged_file_path, "w", encoding="utf-8") as f:
    for para in merged_paragraphs:
        f.write(para + "\n\n")




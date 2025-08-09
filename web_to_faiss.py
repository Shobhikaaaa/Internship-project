import os
import re
import requests
import faiss
import pickle
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

# CONFIG
folder_name = "test"
url = "https://www.fairmont.com/fr/hotels/masai-mara/fairmont-mara-safari-club.html"
model_name = "all-MiniLM-L6-v2"
faiss_index_file = "vector_index.faiss"
metadata_file = "vector_metadata.pkl"

# Step 1: Get HTML & clean
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Title-safe filename
title = soup.title.string.strip() if soup.title else "untitled"
safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)

# Remove unwanted tags
for tag in soup(["script", "style", "noscript", "meta"]):
    tag.decompose()

# Step 2: Extract structured content
def extract_structured_content(soup):
    lines = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']):
        text = tag.get_text(strip=True)
        if not text:
            continue
        if tag.name == "p":
            lines.append(text + "\n\n")  # double newline for para break
        elif tag.name in ["h1", "h2", "h3"]:
            lines.append("\n" + text.upper() + "\n\n")
        elif tag.name == "li":
            lines.append("- " + text)
    return lines

lines = extract_structured_content(soup)

# Save full content to raw file
os.makedirs(folder_name, exist_ok=True)
with open(os.path.join(folder_name, safe_title + ".txt"), "w", encoding="utf-8") as f:
    f.write("TITLE: " + title + "\n")
    f.write("=" * 50 + "\n\n")
    for line in lines:
        f.write(line.strip() + "\n")

# Step 3: Merge lines into paragraphs
raw_text = "\n".join(lines)
paragraph_candidates = re.split(r'\n{4,}', raw_text)

merged_paragraphs = []
for block in paragraph_candidates:
    clean_block = re.sub(r'\n{1,3}', ' ', block.strip())
    if clean_block:
        merged_paragraphs.append(clean_block.strip())

# Save merged paragraphs to file
with open(os.path.join(folder_name, safe_title + "_merged_paragraphs.txt"), "w", encoding="utf-8") as f:
    for para in merged_paragraphs:
        f.write(para + "\n\n")

# Step 4: Vectorize with SentenceTransformer
model = SentenceTransformer(model_name)
embeddings = model.encode(merged_paragraphs, convert_to_numpy=True)

# Step 5: Store in FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, os.path.join(folder_name, faiss_index_file))

# Save metadata (to map vectors back to paragraph text)
with open(os.path.join(folder_name, metadata_file), "wb") as f:
    pickle.dump(merged_paragraphs, f)

print(f"\n✅ Stored {len(merged_paragraphs)} paragraphs in FAISS DB.")

import pickle

# Load the metadata file (which contains the list of paragraphs)
with open("test/vector_metadata.pkl", "rb") as f:
    paragraphs = pickle.load(f)

# Print each paragraph with its index
for i, para in enumerate(paragraphs):
    print(f"[{i}] {para}\n")
output_file = "test/indexed_paragraphs.txt"

with open("test/vector_metadata.pkl", "rb") as f:
    paragraphs = pickle.load(f)

with open(output_file, "w", encoding="utf-8") as f:
    for i, para in enumerate(paragraphs):
        f.write(f"[{i}] {para}\n\n")

print(f"Saved indexed paragraphs to: {output_file}")

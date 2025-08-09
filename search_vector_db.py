import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Load vector DB and metadata
index_path = "test/vector_index.faiss"
metadata_path = "test/vector_metadata.pkl"

index = faiss.read_index(index_path)
with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Define search query
query = "hotel accommodations"

# 4. Convert query to vector
query_vector = model.encode([query])

# 5. Search top k results
k = 5
D, I = index.search(np.array(query_vector).astype("float32"), k)

# 6. Write top results to file
output_file_path = "test/search_results.txt"
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(f"Top {k} results for query: '{query}'\n")
    f.write("=" * 60 + "\n\n")
    for rank, idx in enumerate(I[0], 1):
        if 0 <= idx < len(metadata):
            f.write(f"{rank}. {metadata[idx]}\n\n")

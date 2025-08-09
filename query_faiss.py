import faiss, pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
query = "luxury safari experience in Kenya"

# Load FAISS index and metadata
index = faiss.read_index("test/vector_index.faiss")
with open("test/vector_metadata.pkl", "rb") as f:
    paragraphs = pickle.load(f) 

# Encode the query and search
q_embedding = model.encode([query])
D, I = index.search(q_embedding, k=3)

# Show top 3 matching paragraphs
for rank, idx in enumerate(I[0], 1):
    print(f"\n[{rank}] Score: {D[0][rank-1]:.2f}")
    print(paragraphs[idx]) 





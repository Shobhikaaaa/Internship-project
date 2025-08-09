import json
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def tofloat32Vector(text):
    embedding = model.encode(sentences=text).astype("float32")
    return embedding
    
def toVector(text):
    embedding = model.encode(sentences=text)
    return embedding

def saveToDB(vectors):
    dimension = vectors.shape[1]  # should be 384
    index = faiss.IndexFlatL2(dimension)  
    index.add(vectors)
    return index

def searchDB(text):
    index = faiss.read_index("vector_db.index")
    with open("metadata.json") as f:
        metadata = json.load(f)

    query = "I enjoy programming in Python"
    query_vector = model.encode([query]).astype("float32")

    k = 3
    distances, indices = index.search(query_vector, k)

    print("\n🔍 Top matches:")

if __name__ == "__main__":
    sentences = [
        "Today is sunday.",
        "Today is saturday.",
        "Today is monday.",
    ]
    vector = tofloat32Vector(sentences)
    index = saveToDB(vectors=vector)

    #save it to a file
    faiss.write_index(index, "vector_db.index")

    #save index mapping with metadata
    metadata = {i: sentence for i, sentence in enumerate(sentences)}

    with open("metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print("✅ Vector DB and metadata saved.")

    # Load index and metadata
    index = faiss.read_index("vector_db.index")
    with open("metadata.json") as f:
        loaded_metadata = json.load(f)
    
    query = "Today is sunday."
    k = 3 #top 3 search

    query_vector = tofloat32Vector([query])
    distances, indices = index.search(query_vector, k)

    print("\n🔍 Top matches:")
    print(indices[0])
    for rank in indices[0]:
        print(loaded_metadata[str(rank)] + " : " + str(distances[0][int(rank)]))
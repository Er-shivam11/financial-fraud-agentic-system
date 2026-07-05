from embeddings.embedding_service import generate_embedding

text = "Fraud is an unauthorized transaction."

vector = generate_embedding(text)

print(type(vector))
print(len(vector))
print()

print(vector[:10])
# embeddings/embedding_service.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)


def generate_embedding(text: str):
    """
    Convert text into a vector embedding.
    """
    return embeddings.embed_query(text)
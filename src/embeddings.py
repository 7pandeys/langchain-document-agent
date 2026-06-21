# from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
#
# load_dotenv()
#
# def get_embeddings():
#     return GoogleGenerativeAIEmbeddings(
#         model="models/embedding-004"
#     )
from src.config import GOOGLE_API_KEY
from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
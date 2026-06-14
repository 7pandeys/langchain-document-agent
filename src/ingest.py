from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    return chunks
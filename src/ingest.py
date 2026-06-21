from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# def load_pdf(path):
#     reader = PdfReader(path)
#
#     text = ""
#
#     for page in reader.pages:
#         text += page.extract_text()
#
#     return text

def load_pdf_documents(path):
    reader = PdfReader(path)

    documents = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path,
                    "page": page_num + 1,
                    "version": "v1"
                }
            )
        )

    return documents
def chunk_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    # chunks = splitter.split_text(text)  # Before METADATA implement
    chunks = splitter.split_documents(documents) # To enable METADATA

    return chunks
from pypdf import PdfReader

from backend.config import CHUNK_SIZE
from backend.config import CHUNK_OVERLAP

from backend.parser.chunker import split_into_chunks


def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    metadata = []

    for page_number, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

            metadata.append({

                "page": page_number + 1,

                "text": page_text

            })

    return text, metadata


def process_pdf(pdf_path):

    text, page_metadata = extract_text(pdf_path)

    chunks = split_into_chunks(

        text,

        chunk_size=CHUNK_SIZE,

        overlap=CHUNK_OVERLAP

    )

    chunk_metadata = []

    page_index = 0

    for i, chunk in enumerate(chunks):

        if page_index >= len(page_metadata):

            page_index = len(page_metadata) - 1

        chunk_metadata.append({

            "chunk_id": i,

            "page": page_metadata[page_index]["page"],

            "document": pdf_path.split("\\")[-1],

            "text": chunk

        })

        if page_index < len(page_metadata) - 1:

            page_index += 1

    return chunks, chunk_metadata
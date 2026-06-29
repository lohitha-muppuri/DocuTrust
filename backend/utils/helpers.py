import os
import uuid
from datetime import datetime


def generate_document_id():

    return str(uuid.uuid4())


def get_filename(file_path):

    return os.path.basename(file_path)


def get_file_extension(file_path):

    return os.path.splitext(file_path)[1]


def current_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_chunks(chunks):

    formatted = []

    for chunk in chunks:

        formatted.append(chunk["metadata"]["text"])

    return "\n\n".join(formatted)


def clean_text(text):

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text


def create_metadata(

        filename,

        page,

        chunk_id,

        text

):

    return {

        "document": filename,

        "page": page,

        "chunk_id": chunk_id,

        "text": clean_text(text)

    }


def top_score(results):

    if len(results) == 0:

        return 0

    return max(

        r.get(

            "relevance_score",

            r.get(

                "score",

                0

            )

        )

        for r in results

    )


def average_score(results):

    if len(results) == 0:

        return 0

    scores = [

        r.get(

            "relevance_score",

            r.get(

                "score",

                0

            )

        )

        for r in results

    ]

    return sum(scores) / len(scores)


def workflow_log(

        step,

        message

):

    return {

        "time": current_timestamp(),

        "step": step,

        "message": message

    }
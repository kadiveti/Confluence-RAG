# Upload the document and split it into chunks
from app.models.text_split import TextSplitter

class UploadDocument:
    def __init__(self, document):
        self.document = document
        self.text_splitter = TextSplitter(chunk_size=100, chunk_overlap=0)

    def upload_and_split(self):
        return self.text_splitter.split_text(self.document)
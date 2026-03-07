from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:
    def __init__(self, chunk_size=100, chunk_overlap=0):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, document):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter.split_text(document)
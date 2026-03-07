# Pick from all the app function write a small flask app which it do som basic uploaddocument and ask question to the document and get the answer from the document using LLM and vector store.
from flask import Flask, request, jsonify
from app.services.upload_document import UploadDocument
from app.services.llm_service import LLMService

app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload_document():
    document = request.form['document']
    upload_service = UploadDocument(document)
    upload_service.upload_and_split()
    return jsonify({"message": "Document uploaded and split successfully!"})
@app.route('/ask', methods=['POST'])
def ask_question():
    document = request.form['document']
    question = request.form['question']
    llm_service = LLMService(document)
    answer = llm_service.ask_question(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
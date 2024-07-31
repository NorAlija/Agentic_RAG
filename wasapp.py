# from flask import Flask, render_template, request
# from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
# from llama_index.llms import openai
# from llama_index.llms.openai import OpenAI
# import pypdf
# import os
# from dotenv import load_dotenv
# load_dotenv()

# #Function to read data from directory

# def get_data():
#     document = SimpleDirectoryReader(input_dir="data", recursive=True).load_data()

#     service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the document and can provide helpful summaries"))
#     index = VectorStoreIndex.from_documents(document, service_context=service_context)
#     chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
  
#     return chat_engine

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'pdf_file' in request.files:
#         pdf_file = request.files['pdf_file']
#         if pdf_file.filename.endswith('.pdf'):

#             upload_folder = 'data'
#             os.makedirs(upload_folder, exist_ok=True)
#             pdf_path = os.path.join(upload_folder, pdf_file.filename)
#             pdf_file.save(pdf_path)
#             print(f"Uploaded PDF path: {pdf_path}")

#             return render_template('chat.html', upload_success=True)
#         else:
#             return render_template('index.html', upload_error="Invalid file format. Please upload a PDF.")
#     else:
#         return render_template('index.html', upload_error="No file uploaded.")

# @app.route('/chat', methods=['POST'])
# def chat():
#     chat_engine = get_data()
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         response = chat_engine.chat(prompt)
#         return render_template('chat.html', prompt=prompt, response=response.response)
    
# if __name__ == '__main__':
#     app.run(debug=True)
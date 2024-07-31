import os
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

def process_pdf(file_path):
    # Add code to process the PDF if needed
    pass

def chat_with_document(prompt):
    # Load data
    document = SimpleDirectoryReader(input_dir=os.getenv('UPLOAD_FOLDER', 'data'), recursive=True).load_data()
    
    # Setup service context and chat engine
    service_context = ServiceContext.from_defaults(
        llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the document and can provide helpful summaries"))
    
    index = VectorStoreIndex.from_documents(document, service_context=service_context)
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
    
    # Get response from chat engine
    response = chat_engine.chat(prompt)
    
    return response.response

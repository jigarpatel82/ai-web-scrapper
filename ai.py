from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


llm = OllamaLLM(model='llama3.2')

def parse_content_with_ollama(dom_content, parse_description):
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=6000, chunk_overlap=200)
    chunks = text_spliter.split_text(dom_content)
    template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)
    prompt = ChatPromptTemplate.from_template(template)

    documents = [Document(page_content=chunk) for chunk in chunks ]
    
    chain = prompt | llm
    
    responses = []
    for document in documents:
        response = chain.invoke({'dom_content': document.page_content, 'parse_description':parse_description})
        responses.append(response)
    return ('\n').join(responses)
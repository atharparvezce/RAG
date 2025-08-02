from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.noon.com/saudi-en/5-gallon-water-bottle-pump-usb-charging-portable-electric-water-pump-for-2-5-gallon-jugs-usb-charging-portable-water-dispenser-for-office-home-camping-kitchen-and-etc-white/Z18FD5EDB4BEFEF2838C1Z/p/?o=z18fd5edb4befef2838c1z-1&shareId=9f419387-302f-47e4-8a10-206f8820e904'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))
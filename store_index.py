from dotenv import load_dotenv
import weaviate, os
import weaviate.classes as wvc
from src.helper import load_pdfs, filter_extracted_data, text_split, download_embeddings


load_dotenv()



WEAVIATE_URL=os.environ.get("WEAVIATE_URL")
WEAVIATE_API_KEY=os.environ.get("WEAVIATE_API_KEY")
os.environ["WEAVIATE_URL"] = WEAVIATE_URL
os.environ["WEAVIATE_API_KEY"] = WEAVIATE_API_KEY


extracted_data=load_pdfs('Z:\VsCode\Medussa-Medical Chatbot\Medussa--Medical-Chatbot-\data')
filter_data =  filter_extracted_data(extracted_data)
text_chunks=text_split(filter_data)

embeddings = download_embeddings()



URL = os.getenv("WEAVIATE_URL")
APIKEY = os.getenv("WEAVIATE_API_KEY")

# Connect to Weaviate Cloud
client= weaviate.connect_to_weaviate_cloud(
    cluster_url=URL,
    auth_credentials=wvc.init.Auth.api_key(APIKEY),
)



from langchain_weaviate import WeaviateVectorStore
import weaviate

from langchain_weaviate import WeaviateVectorStore
import weaviate
from tqdm import tqdm

doc_search = WeaviateVectorStore(
    client=client,
    index_name="Medussa",
    embedding=embeddings,
    text_key="page_content"
)

# Insert in batches with tqdm
batch_size = 100
for i in tqdm(range(0, len(text_chunks), batch_size), desc="Uploading to Weaviate"):
    batch = text_chunks[i:i+batch_size]
    doc_search.add_documents(batch)



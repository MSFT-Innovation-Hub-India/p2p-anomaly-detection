
from dotenv import load_dotenv
import os
load_dotenv()


api_key=os.getenv("api_key")
model=os.getenv("model")
az_logic_app_url=os.getenv("logicapp_url")
vector_store_id=os.getenv("vector_store_id")
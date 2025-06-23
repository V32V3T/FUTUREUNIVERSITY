import os
from dotenv import load_dotenv
from fastapi import FastAPI
from supabase import create_client, Client


load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Create client
supabase: Client = create_client(url, key)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    """
    Fetch all posts from the 'posts' table.
    """
    response = supabase.table("posts").select("*").execute()
    
    # return the list of posts
    return {"posts": response.data}

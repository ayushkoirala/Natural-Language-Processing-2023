from fastapi import FastAPI
from PIL import Image
import io
from io import BytesIO
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from utils.backbone import topwords
import asyncio
import nest_asyncio
nest_asyncio.apply()


app = FastAPI()

class ResponseModel(BaseModel):
    text: str
    image: bytes

@app.post("/process_data")
async def process_data(text: str):
    # process the text and generate an image
    img_bytes, topbad, topgood = topwords(text)
    dict1 = {'images':img_bytes,'Topbad':topbad,'topgood':topgood}
    # create a response model with the text and the image
   # StreamingResponse(img_bytes, media_type="image/png")

    # return the response model
    return dict1

from io import BytesIO
from PIL import Image
from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile


class ImageMetadata(BaseModel):
    format: str
    size: tuple[int, int]
    mode: str


app = FastAPI()


@app.post("/image_metadata")
async def image_metadata(file: UploadFile = File(...)) -> ImageMetadata:
    image = Image.open(BytesIO(await file.read()))
    return ImageMetadata(
        format=image.format,
        size=image.size,
        mode=image.mode,
    )

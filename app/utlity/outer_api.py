import requests
from fastapi import UploadFile

IMGBB_API_KEY = "9803985eb1cb9910bdd2a790770333d5"  # Replace with your Imgbb API key

async def upload_image_to_imgbb(file: UploadFile) -> str:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMGBB_API_KEY,
    }
    files = {
        "image": (file.filename, await file.read(), file.content_type),
    }

    response = requests.post(url, data=payload, files=files)
    if response.status_code == 200:
        return response.json()["data"]["url"]  # Return the uploaded image URL
    else:
        raise Exception("Failed to upload image to ImgBB")

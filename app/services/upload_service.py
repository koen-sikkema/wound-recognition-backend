from fastapi    import UploadFile
from io         import BytesIO

class UploadService:
    def __init__(self):
        pass

    async def process_image(self, image: UploadFile, bodypart: str = None, notes: str = None):
        ''' 
            This function processes an uploaded image and returns some information about it.
        '''
        image_data = await image.read()
        
        # TODO: Implement the actual validation of the image here
           
        print(f"Received image: {image.filename}")
        print(f"Image size: {len(image_data)} bytes")
        print(f"Body part: {bodypart}")
        print(f"Notes: {notes}")
        
        return {"filename": image.filename, "size": len(image_data), "notes": notes}
    

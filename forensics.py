from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    try:
        # 1. Open the image
        img = Image.open(image_path)
        
        # 2. Extract EXIF data
        info = img._getexif()
        
        if info is None:
            print(f"No metadata found in {image_path}")
            return

        print(f"--- Metadata for {image_path} ---")
        
        # 3. Translate the numeric tags into readable labels
        for tag_id, value in info.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name:20}: {value}")

    except Exception as e:
        print(f"Error: {e}")

# Run the function (Replace 'my_photo.jpg' with your actual image file)
extract_metadata("my_photo.jpg")
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configure Cloudinary
cloudinary.config(
    cloud_name='',
    api_key='',
    api_secret=''
)

def upload_image(file):
    # Upload an image
    response = cloudinary.uploader.upload(file)

    # Print the response details
    print("Uploaded Image Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']
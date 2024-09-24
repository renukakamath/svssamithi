import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configure Cloudinary
cloudinary.config(
    cloud_name='dhojqnvsg',
    api_key='766411243646231',
    api_secret='KZErp3xo8xIqZqbpUYwF3VghhNY'
)

def upload_image(file):
    # Upload an image
    response = cloudinary.uploader.upload(file)

    # Print the response details
    print("Uploaded Image Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']
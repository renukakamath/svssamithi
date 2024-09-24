import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configure Cloudinary
cloudinary.config(
    cloud_name='ddmzrsm8r',
    api_key='561275631182275',
    api_secret='rQq_RXSz_MzH1IiqP7Z_QaDUgP4'
)

def upload_image(file):
    # Upload an image
    response = cloudinary.uploader.upload(file)

    # Print the response details
    print("Uploaded Image Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']
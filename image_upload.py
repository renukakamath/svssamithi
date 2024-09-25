import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import mimetypes

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



def upload_video(file):
    # Upload a video
    response = cloudinary.uploader.upload(file, resource_type="video")

    # Print the response details
    print("Uploaded Video Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']



def upload_audio(file):
    # Upload an audio file
    response = cloudinary.uploader.upload(file, resource_type="audio")

    # Print the response details
    print("Uploaded Audio Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']



def upload_pdf(file):
    # Upload a PDF file
    response = cloudinary.uploader.upload(file, resource_type="raw")

    # Print the response details
    print("Uploaded PDF Details:")
    print(f"Public ID: {response['public_id']}")
    print(f"URL: {response['url']}")
    
    return response['url']



def upload_file(file):
    # Determine the MIME type of the file
    mime_type, _ = mimetypes.guess_type(file.filename)

    if mime_type and mime_type.startswith("video"):
        # If the file is a video, upload as a video
        return upload_video(file)
    else:
        # Otherwise, treat it as an image
        return upload_image(file)

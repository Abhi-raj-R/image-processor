import cv2
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read image!")
        return

    # Task I: Print the size and shape of the image
    print(f"Image Shape: {image.shape}")  # (height, width, channels)
    print(f"Image Size: {image.size} bytes")

    # Task II: Convert the image to binary and grayscale formats
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(grayscale_image, 128, 255, cv2.THRESH_BINARY)

    # Save grayscale and binary images
    cv2.imwrite('grayscale_image.jpg', grayscale_image)
    cv2.imwrite('binary_image.jpg', binary_image)

    # Task III: Scale the image by reducing its size
    scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imwrite('scaled_image.jpg', scaled_image)

    # Task IV: Remove noise from the image
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite('denoised_image.jpg', denoised_image)

    print("Processed images have been saved as files in the current directory.")

# Input image path
image_path = 'bg.png'  # Replace with your image file path
process_image(image_path)
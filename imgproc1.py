import cv2
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Unable to read image!")
        return

    # Task I: Perform an inverse transformation on the image
    inverse_image = cv2.bitwise_not(image)
    cv2.imwrite('inverse_image.jpg', inverse_image)

    # Task II: Enhance the image using contrast stretching
    min_val = np.min(image)
    max_val = np.max(image)
    contrast_stretched_image = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    cv2.imwrite('contrast_stretched_image.jpg', contrast_stretched_image)

    # Task III: Generate a histogram-equalized image to improve contrast
    hist_equalized_image = cv2.equalizeHist(image)
    cv2.imwrite('hist_equalized_image.jpg', hist_equalized_image)

    # Task IV: Detect edges in the image using an edge detection technique
    edges_image = cv2.Canny(image, threshold1=100, threshold2=200)
    cv2.imwrite('edges_image.jpg', edges_image)

    print("Processed images have been saved successfully!")

# Input image path
image_path = 'bg.png'  # Replace with your image file path
process_image(image_path)
import pyautogui
from PIL import Image

# Check Image Weight and Height
# Load the reference image
reference_image_path = './晚班水位/ven326.png'
reference_image = Image.open(reference_image_path)

# Get the dimensions of the reference image
image_width, image_height = reference_image.size

# Print image dimensions
print(f"Image width: {image_width}, Image height: {image_height}")

from PIL import Image
import os

def convert_to_kindle_grayscale(input_path, output_path, dither=True):
    """
    Convert an image to grayscale optimized for Kindle e-ink displays.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the converted image
        dither (bool): Whether to apply dithering for better grayscale rendering
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to grayscale (L mode for 8-bit grayscale)
        img_gray = img.convert('L')
        
        # Apply dithering if specified (Floyd-Steinberg dithering)
        if dither:
            img_gray = img_gray.convert('L', dither=Image.FLOYDSTEINBERG)
        
        # Save the image (PNG is suitable for Kindle)
        img_gray.save(output_path, 'PNG')
        print(f"Image saved successfully to {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")

def batch_convert(input_folder, output_folder, dither=True):
    """
    Convert all images in a folder to Kindle-compatible grayscale.
    
    Args:
        input_folder (str): Folder containing input images
        output_folder (str): Folder to save converted images
        dither (bool): Whether to apply dithering
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"gray_{filename}")
            convert_to_kindle_grayscale(input_path, output_path, dither)

if __name__ == "__main__":
    # Example usage
    input_image = "C:/Users/orion/Desktop/KindleWp/Kindle_test"  # Replace with your image path
    output_image = "C:/Users/orion/Desktop/KindleWp/Kindle_test1"  # Output path
    convert_to_kindle_grayscale(input_image, output_image, dither=True)
    
    # For batch processing
    # input_folder = "input_folder"
    # output_folder = "output_folder"
    # batch_convert(input_folder, output_folder, dither=True)cleaar
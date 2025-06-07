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
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Verify input file exists
        if not os.path.isfile(input_path):
            raise FileNotFoundError(f"Input file does not exist: {input_path}")
        
        # Open and process the image
        img = Image.open(input_path)
        img_gray = img.convert('L')
        if dither:
            img_gray = img_gray.convert('L', dither=Image.FLOYDSTEINBERG)
        
        # Save the image
        img_gray.save(output_path, 'PNG')
        print(f"Image saved successfully to {output_path}")
        
    except PermissionError as e:
        print(f"Permission denied: {e}. Try running as administrator or check folder permissions.")
    except FileNotFoundError as e:
        print(e)
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
    try:
        # Ensure input folder exists
        if not os.path.isdir(input_folder):
            raise FileNotFoundError(f"Input folder does not exist: {input_folder}")
        
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Supported image extensions
        supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
        
        # Loop through all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(supported_extensions):
                input_path = os.path.join(input_folder, filename)
                # Create output filename (e.g., gray_originalname.png)
                output_filename = f"gray_{filename}"
                output_path = os.path.join(output_folder, output_filename)
                convert_to_kindle_grayscale(input_path, output_path, dither)
            else:
                print(f"Skipping {filename}: Unsupported file type")
                
        print(f"Batch conversion completed. Processed files saved to {output_folder}")
        
    except Exception as e:
        print(f"Error during batch conversion: {e}")

if __name__ == "__main__":
    # Specify input and output folders (use forward slashes or raw strings for Windows paths)
    input_folder = "C:/Users/orion/Desktop/KindleWp/Kindle_test"  # Replace with your input folder
    output_folder = "C:/Users/orion/Desktop/KindleWp/Kindle_test1"  # Replace with your output folder
    batch_convert(input_folder, output_folder, dither=True)
from PIL import Image
import os

def convert_to_kindle_grayscale(input_path, output_path, dither=True):
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


# Batch processing function to convert multiple images in a directory
def batch_convert_to_kindle_grayscale(input_dir, output_dir, dither=True):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
# Create output directory if it doesn't exist
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")


 # Supported image formats
supported_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
def is_supported_image(filename):
    return any(filename.lower().endswith(ext) for ext in supported_extensions)

# Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            # Check if the file is a supported image format
            output_file = f"gray_{filename}"
            output_path = os.path.join(output_folder, filename)
            convert_to_kindle_grayscale(input_folder, output_folder, dither)
    else:
            print(f"Skipping unsupported file: {filename}")

    print(f"Batch converision completed. Processed files saved to  {output_folder}")

if __name__ == "__main__":
    input_folder = "C:/Users/orion/Desktop/KindleWp\Kindle_test/"  # Replace with your input image
    output_folder = "C:/Users/orion/Desktop/KindleWp/Kindle_test1"  # Explicit file extension
    batch_convert_to_kindle_grayscale(input_folder, output_image, dither=True)
    #convert_to_kindle_grayscale(input_image, output_image, dither=True)

    print("Batch conversion completed.")
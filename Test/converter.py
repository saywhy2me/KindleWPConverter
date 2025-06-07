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

if __name__ == "__main__":
    input_image = "C:/Users/orion/Desktop/KindleWp\Kindle_test/photo1.png"  # Replace with your input image
    output_image = "C:/Users/orion/Desktop/KindleWp/Kindle_test/photo1.1.png"  # Explicit file extension
    convert_to_kindle_grayscale(input_image, output_image, dither=True)
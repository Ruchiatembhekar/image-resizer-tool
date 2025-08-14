import os
import sys
from PIL import Image

def resize_images(input_folder, output_folder, width=800, height=600, quality=95):
    """
    Resize all images in a folder to specified dimensions
    
    Args:
        input_folder (str): Path to folder containing images
        output_folder (str): Path to folder where resized images will be saved
        width (int): Target width in pixels
        height (int): Target height in pixels
        quality (int): JPEG quality (1-100, higher is better)
    """
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist!")
        return
    
    # Get list of image files
    image_files = []
    for filename in os.listdir(input_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_formats:
            image_files.append(filename)
    
    if not image_files:
        print(f"No supported image files found in '{input_folder}'")
        print(f"Supported formats: {', '.join(supported_formats)}")
        return
    
    print(f"Found {len(image_files)} images to process...")
    print("-" * 50)
    
    processed_count = 0
    failed_count = 0
    
    for filename in image_files:
        try:
            # Full path to input image
            input_path = os.path.join(input_folder, filename)
            
            # Open and resize image
            with Image.open(input_path) as img:
                # Get original dimensions
                original_width, original_height = img.size
                
                # Resize image (you can choose different resize methods)
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Prepare output filename
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_resized{ext}"
                output_path = os.path.join(output_folder, output_filename)
                
                # Save resized image
                if ext.lower() in ['.jpg', '.jpeg']:
                    # Convert to RGB if necessary (for JPEG)
                    if resized_img.mode in ('RGBA', 'LA', 'P'):
                        resized_img = resized_img.convert('RGB')
                    resized_img.save(output_path, 'JPEG', quality=quality, optimize=True)
                else:
                    resized_img.save(output_path, optimize=True)
                
                print(f"✓ {filename} ({original_width}x{original_height}) → {output_filename} ({width}x{height})")
                processed_count += 1
                
        except Exception as e:
            print(f"✗ Failed to process {filename}: {str(e)}")
            failed_count += 1
    
    print("-" * 50)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed_count} images")
    print(f"Failed: {failed_count} images")

def resize_images_maintain_aspect_ratio(input_folder, output_folder, max_width=800, max_height=600, quality=95):
    """
    Resize images while maintaining aspect ratio
    
    Args:
        input_folder (str): Path to folder containing images
        output_folder (str): Path to folder where resized images will be saved
        max_width (int): Maximum width in pixels
        max_height (int): Maximum height in pixels
        quality (int): JPEG quality (1-100, higher is better)
    """
    
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist!")
        return
    
    image_files = []
    for filename in os.listdir(input_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_formats:
            image_files.append(filename)
    
    if not image_files:
        print(f"No supported image files found in '{input_folder}'")
        return
    
    print(f"Found {len(image_files)} images to process (maintaining aspect ratio)...")
    print("-" * 50)
    
    processed_count = 0
    failed_count = 0
    
    for filename in image_files:
        try:
            input_path = os.path.join(input_folder, filename)
            
            with Image.open(input_path) as img:
                original_width, original_height = img.size
                
                # Calculate new dimensions while maintaining aspect ratio
                ratio = min(max_width/original_width, max_height/original_height)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
                
                # Only resize if image is larger than max dimensions
                if ratio < 1:
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    resized_img = img.copy()
                    new_width, new_height = original_width, original_height
                
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_resized{ext}"
                output_path = os.path.join(output_folder, output_filename)
                
                if ext.lower() in ['.jpg', '.jpeg']:
                    if resized_img.mode in ('RGBA', 'LA', 'P'):
                        resized_img = resized_img.convert('RGB')
                    resized_img.save(output_path, 'JPEG', quality=quality, optimize=True)
                else:
                    resized_img.save(output_path, optimize=True)
                
                print(f"✓ {filename} ({original_width}x{original_height}) → {output_filename} ({new_width}x{new_height})")
                processed_count += 1
                
        except Exception as e:
            print(f"✗ Failed to process {filename}: {str(e)}")
            failed_count += 1
    
    print("-" * 50)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed_count} images")
    print(f"Failed: {failed_count} images")

def main():
    print("=" * 60)
    print("           IMAGE RESIZER TOOL")
    print("=" * 60)
    
    # Get user input
    input_folder = input("Enter input folder path (or press Enter for 'input_images'): ").strip()
    if not input_folder:
        input_folder = "input_images"
    
    output_folder = input("Enter output folder path (or press Enter for 'output_images'): ").strip()
    if not output_folder:
        output_folder = "output_images"
    
    print("\nResize options:")
    print("1. Fixed dimensions (may distort image)")
    print("2. Maintain aspect ratio (recommended)")
    
    choice = input("Choose option (1 or 2, default is 2): ").strip()
    
    # Get dimensions
    try:
        if choice == "1":
            width = int(input("Enter target width (default 800): ") or "800")
            height = int(input("Enter target height (default 600): ") or "600")
            quality = int(input("Enter JPEG quality 1-100 (default 95): ") or "95")
            
            print(f"\nProcessing images from '{input_folder}' to '{output_folder}'")
            print(f"Target size: {width}x{height} pixels")
            resize_images(input_folder, output_folder, width, height, quality)
            
        else:  # Default to option 2
            max_width = int(input("Enter maximum width (default 800): ") or "800")
            max_height = int(input("Enter maximum height (default 600): ") or "600")
            quality = int(input("Enter JPEG quality 1-100 (default 95): ") or "95")
            
            print(f"\nProcessing images from '{input_folder}' to '{output_folder}'")
            print(f"Maximum size: {max_width}x{max_height} pixels (aspect ratio maintained)")
            resize_images_maintain_aspect_ratio(input_folder, output_folder, max_width, max_height, quality)
            
    except ValueError:
        print("Error: Please enter valid numbers for dimensions and quality!")
        return
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return

if __name__ == "__main__":
    main()
from PIL import Image
import os

def convert_webp_to_jpg(webp_path, jpg_path):
    with Image.open(webp_path) as img:
        rgb_img = img.convert('RGB')
        rgb_img.save(jpg_path, 'JPEG')

def main():
    webp_images = [
        
    ]

    output_dir = '/home/images/jpg_images/'  # Change this to your output directory
    os.makedirs(output_dir, exist_ok=True)

    # Loop through the list of WEBP images
    for webp_file in webp_images:
        if webp_file.endswith('.webp'):
            jpg_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(webp_file))[0]}.jpg")
            convert_webp_to_jpg(webp_file, jpg_file)
            print(f"Converted {webp_file} to {jpg_file}")

if __name__ == "__main__":
    main()

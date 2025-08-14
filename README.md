# 🖼️ Image Resizer Tool

A powerful yet simple **Python tool** to batch resize images effortlessly using [Pillow](https://python-pillow.org/).  
Easily choose between **fixed dimensions** or **maintaining aspect ratio** — perfect for photographers, web developers, or anyone handling lots of images! 🚀

---

## ✨ Features
✅ Batch resize **all images** in a folder  
✅ Choose between **fixed size** or **maintain aspect ratio**  
✅ Supports multiple formats: JPG, PNG, BMP, TIFF, WEBP  
✅ Adjustable JPEG quality (1–100)  
✅ Automatically creates output folder if not present  
✅ Clear logs showing before → after sizes  
✅ Error handling for missing folders and unsupported files  

---

## 🛠️ Requirements
- Python 3.7+
- [Pillow library](https://pypi.org/project/Pillow/)

Install Pillow:
```bash
pip install pillow
📂 Project Structure
bash
Copy
Edit
image-resizer-tool/
│
├── image_resizer.py      # Main script
├── README.md             # Documentation
├── input_images/         # (Optional) Put your original images here
└── output_images/        # (Generated) Resized images will be saved here
🚀 How to Use
Step 1 — Prepare Folders
Create an input folder with images you want to resize.
Example: input_images

Create (or let the script create) an output folder for results.
Example: output_images

Step 2 — Run the Script
In the terminal:

bash
Copy
Edit
python image_resizer.py
Step 3 — Follow the Prompts
Example run:

java
Copy
Edit
============================================================
           IMAGE RESIZER TOOL
============================================================
Enter input folder path (or press Enter for 'input_images'): input_images
Enter output folder path (or press Enter for 'output_images'): output_images

Resize options:
1. Fixed dimensions (may distort image)
2. Maintain aspect ratio (recommended)
Choose option (1 or 2, default is 2): 2

Enter maximum width (default 800): 800
Enter maximum height (default 600): 600
Enter JPEG quality 1-100 (default 95): 90

Processing images from 'input_images' to 'output_images'
Maximum size: 800x600 pixels (aspect ratio maintained)
Found 3 images to process (maintaining aspect ratio)...
--------------------------------------------------
✓ photo1.jpg (1920x1080) → photo1_resized.jpg (800x450)
✓ photo2.png (1200x800) → photo2_resized.png (800x533)
✓ photo3.webp (500x500) → photo3_resized.webp (500x500)
--------------------------------------------------
Processing complete!
Successfully processed: 3 images
Failed: 0 images

Original:

photo1.jpg → 1920×1080

photo2.png → 1200×800

After Resizing (800×600 max):

photo1_resized.jpg → 800×450

photo2_resized.png → 800×533

💡 Tips
Fixed dimensions (option 1) may distort images — best for uniform thumbnails.

Maintain aspect ratio (option 2) keeps proportions, avoids stretching.

JPEG quality of 85–95 gives great quality with smaller file size.

You can reuse the same output folder — old files will be overwritten.

📜 License
MIT License – Free to use, modify, and share.

👩‍💻 Author
Developed with ❤️ by Ruchi Tembhekar.
If you like this project, ⭐ star it on GitHub!

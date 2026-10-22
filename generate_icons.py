import os
from PIL import Image

base_dir = r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide"
src_img_path = os.path.join(base_dir, "assets", "images", "page_1_img_2_9.png")

res_dir = os.path.join(base_dir, "android", "app", "src", "main", "res")

sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192
}

if os.path.exists(src_img_path):
    img = Image.open(src_img_path)
    # create a square crop of the panel
    w, h = img.size
    # crop center-top where the panel screen and logo are
    crop_size = min(w, int(h * 0.7))
    left = (w - crop_size) // 2
    top = int(h * 0.1)
    right = left + crop_size
    bottom = top + crop_size
    cropped = img.crop((left, top, right, bottom))
    
    for folder, size in sizes.items():
        out_dir = os.path.join(res_dir, folder)
        os.makedirs(out_dir, exist_ok=True)
        resized = cropped.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(os.path.join(out_dir, "ic_launcher.png"), "PNG")
        resized.save(os.path.join(out_dir, "ic_launcher_round.png"), "PNG")
        resized.save(os.path.join(out_dir, "ic_launcher_foreground.png"), "PNG")
        print(f"Generated {size}x{size} icon for {folder}")
        
    print("All Android icons generated successfully!")
else:
    print("Source image not found:", src_img_path)

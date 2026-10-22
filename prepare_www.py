import os
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
www_dir = os.path.join(base_dir, "www")

os.makedirs(www_dir, exist_ok=True)

files_to_copy = ["index.html", "manifest.json", "sw.js"]
for f in files_to_copy:
    src = os.path.join(base_dir, f)
    dst = os.path.join(www_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {f} to www/")

assets_src = os.path.join(base_dir, "assets")
assets_dst = os.path.join(www_dir, "assets")
if os.path.exists(assets_src):
    if os.path.exists(assets_dst):
        shutil.rmtree(assets_dst)
    shutil.copytree(assets_src, assets_dst)
    print("Copied assets to www/assets")

print("www directory prepared successfully!")

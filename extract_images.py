import os
import fitz
import pypdf

pdf_path = r"C:\Users\PREDATOR\Desktop\User Manual - Arabic\Teledata_One_User_Manual_AR.pdf"
doc = fitz.open(pdf_path)
reader = pypdf.PdfReader(pdf_path)

out_dir = r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide\assets\images"
os.makedirs(out_dir, exist_ok=True)

report = []

# Collect captions using pypdf
page_captions = {}
for pno, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    figs = [l for l in lines if "الشكل" in l or "شكل" in l]
    if figs:
        page_captions[pno + 1] = figs

print(f"Pages with figure captions: {len(page_captions)}")

extracted_files = []
for pno in range(len(doc)):
    page_num = pno + 1
    page = doc[pno]
    image_list = page.get_images(full=True)
    
    # filter out the repeating header logo (709x55)
    page_imgs = []
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w, h = base_img["width"], base_img["height"]
        ext = base_img["ext"]
        
        # Skip small repeating teledata logo unless page 1
        if (w == 709 and h == 55) and page_num > 1:
            continue
            
        img_bytes = base_img["image"]
        filename = f"page_{page_num}_img_{img_idx+1}_{xref}.{ext}"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, "wb") as f:
            f.write(img_bytes)
        
        captions = page_captions.get(page_num, [])
        page_imgs.append({
            "page": page_num,
            "filename": filename,
            "width": w,
            "height": h,
            "xref": xref,
            "captions": captions
        })
        extracted_files.append((page_num, filename, w, h, captions))

with open(r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide\extracted_images.txt", "w", encoding="utf-8") as f:
    for item in extracted_files:
        f.write(f"Page {item[0]}: {item[1]} ({item[2]}x{item[3]}) -> Captions: {item[4]}\n")

print(f"Extracted {len(extracted_files)} images successfully!")

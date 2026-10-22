import os
import base64
import json

webp_dir = r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide\assets\images_webp"

# Map figure numbers / pages to the webp filenames
fig_map = {
    "cover": "page_1_img_2_9.webp",
    "logo": "page_1_img_1_4.webp",
    "fig_1": "page_11_img_1_686.webp",
    "fig_2": "page_19_img_1_703.webp",
    "fig_3": "page_22_img_1_710.webp",
    "fig_4": "page_24_img_1_715.webp",
    "fig_5": "page_25_img_1_718.webp",
    "fig_6": "page_27_img_1_723.webp",
    "fig_7": "page_28_img_1_726.webp",
    "fig_8": "page_29_img_1_729.webp",
    "table_hardware_config": "page_32_img_1_736.webp",
    "fig_9": "page_33_img_1_736.webp",
    "fig_10": "page_33_img_2_739.webp",
    "fig_11": "page_34_img_1_743.webp",
    "fig_12": "page_42_img_1_761.webp",
    "fig_13": "page_44_img_1_766.webp",
    "fig_14": "page_44_img_2_767.webp",
    "fig_15": "page_45_img_1_770.webp",
    "fig_16": "page_46_img_1_773.webp",
    "fig_17": "page_47_img_1_776.webp",
    "fig_18": "page_50_img_1_783.webp",
    "fig_19": "page_51_img_1_786.webp",
    "fig_20": "page_52_img_1_789.webp",
    "fig_21": "page_53_img_1_792.webp",
    "fig_22": "page_54_img_1_795.webp",
    "fig_23": "page_55_img_1_798.webp",
    "fig_24": "page_56_img_1_801.webp",
    "fig_25": "page_58_img_1_806.webp",
    "fig_26": "page_59_img_1_809.webp",
    "fig_27": "page_60_img_1_812.webp",
    "fig_28": "page_61_img_1_815.webp",
    "fig_29": "page_61_img_2_816.webp",
    "fig_30": "page_73_img_1_841.webp",
    "fig_31": "page_73_img_2_842.webp",
    "fig_32": "page_74_img_1_845.webp",
    "fig_33": "page_75_img_1_848.webp",
    "fig_34": "page_76_img_1_851.webp",
    "fig_35": "page_78_img_1_856.webp",
    "fig_36": "page_79_img_1_860.webp",
    "fig_37": "page_80_img_1_863.webp",
    "fig_38": "page_81_img_1_866.webp",
    "fig_39": "page_82_img_1_869.webp",
    "fig_40": "page_83_img_1_872.webp",
    "fig_41": "page_85_img_1_877.webp",
    "fig_42": "page_92_img_1_894.webp",
    "fig_43": "page_94_img_1_899.webp",
}

b64_dict = {}
missing = []
for k, fname in fig_map.items():
    fpath = os.path.join(webp_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "rb") as f:
            b = base64.b64encode(f.read()).decode("ascii")
            b64_dict[k] = f"data:image/webp;base64,{b}"
    else:
        missing.append((k, fname))

print(f"Loaded {len(b64_dict)} figures into base64. Missing: {missing}")

with open(r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide\images_base64.json", "w", encoding="utf-8") as f:
    json.dump(b64_dict, f)
print("Saved images_base64.json successfully!")

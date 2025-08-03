import os
import base64
import json
from pathlib import Path

folder_path = Path("F:/Thuc_tap/automation-testing/tests/screenshots/image_xno")
pattern = "san_bot*.png"

# Tìm tất cả ảnh san_bot_...png trong thư mục
image_files = list(folder_path.glob(pattern))

encoded_images = []
for img_path in image_files:
    with open(img_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")
        encoded_images.append({
            "filename": img_path.name,
            "base64": encoded_image,
            "image_url": f"data:image/png;base64,{encoded_image}"
        })

output_dir = Path("F:/Thuc_tap/automation-testing/structured-output")
output_dir.mkdir(parents=True, exist_ok=True)

# Ghi file JSON
json_output_path = output_dir / "san_bot_images.json"
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump({"images": encoded_images}, f, indent=2)

print("-- Đã xuất JSON:", json_output_path)

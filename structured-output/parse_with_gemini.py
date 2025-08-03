import os
import json
import base64
from pathlib import Path
from dotenv import load_dotenv

# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv("F:/Thuc_tap/automation-testing/.env")
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("- GEMINI_API_KEY chưa được thiết lập trong .env")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2, google_api_key=api_key)

class BotInfo(BaseModel):
    bot_name: str = Field(..., description="Tên của bot")
    signal_status: str = Field(..., description="Trạng thái tín hiệu (Mua, Bán, Không tín hiệu)")
    win_rate_percent: float = Field(..., description="Tỷ lệ thắng của bot (%)")
    roi_percent: float = Field(..., description="ROI (return on investment) của bot (%)")
    signal_type: str = Field(..., description="Loại bot (Phái sinh hoặc Cơ sở)")


structured_llm = llm.with_structured_output(BotInfo)

# Load ảnh từ file JSON
json_path = Path("F:/Thuc_tap/automation-testing/structured-output/san_bot_images.json")
if not json_path.exists():
    raise FileNotFoundError(f"Không tìm thấy file: {json_path}")

with open(json_path, "r", encoding="utf-8") as f:
    image_data = json.load(f)["images"]

output_results = []

for img in image_data:
    print(f"\n- Phân tích ảnh: {img['filename']}")

    prompt = HumanMessage(
        content=[
            {"type": "text",
             "text": "Trích xuất thông tin bot từ ảnh gồm: tên bot, trạng thái tín hiệu, winrate (%), ROI (%) và loại bot (phái sinh/cơ sở)."},
            {"type": "image_url", "image_url": img["image_url"]},
        ]
    )

    try:
        result: BotInfo = structured_llm.invoke([prompt])
        print(f"- Kết quả có cấu trúc: {result}")
        output_results.append({
            "filename": img["filename"],
            "bot_info": result.dict()
        })
    except Exception as e:
        print(f"-- Lỗi khi xử lý ảnh {img['filename']}: {e}")
        output_results.append({
            "filename": img["filename"],
            "error": str(e)
        })

#  Ghi ra JSON
output_file = Path("F:/Thuc_tap/automation-testing/structured-output/san_bot_result.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_results, f, ensure_ascii=False, indent=2)

print(f"\n- Kết quả đã được lưu vào: {output_file}")

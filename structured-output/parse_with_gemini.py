import os
import json
import base64
from pathlib import Path
from dotenv import load_dotenv

# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field  # Use pydantic for structured output (new)
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv("F:/Thuc_tap/automation-testing/.env")
api_key = os.getenv("GEMINI_API_KEY") # Ensure GEMINI_API_KEY
if not api_key:
    raise ValueError("- GEMINI_API_KEY chưa được thiết lập trong .env")

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2, google_api_key=api_key)

# Define the structured output model
class BotInfo(BaseModel):
    bot_name: str = Field(..., description="Tên của bot")
    signal_status: str = Field(..., description="Trạng thái tín hiệu (Mua, Bán, Không tín hiệu)")
    win_rate_percent: float = Field(..., description="Tỷ lệ thắng của bot (%)")
    roi_percent: float = Field(..., description="ROI (return on investment) của bot (%)")
    signal_type: str = Field(..., description="Loại bot (Phái sinh hoặc Cơ sở)")

# Enable structured output for the LLM
structured_llm = llm.with_structured_output(BotInfo)

# Path to the JSON file containing image data
json_path = Path("F:/Thuc_tap/automation-testing/structured-output/san_bot_images.json")
if not json_path.exists():
    raise FileNotFoundError(f"Không tìm thấy file: {json_path}")

# Load the image data from JSON
with open(json_path, "r", encoding="utf-8") as f:
    image_data = json.load(f)["images"]

output_results = []  # List to store results

# Process each image and extract bot information
for img in image_data:
    print(f"\n- Phân tích ảnh: {img['filename']}")

    # Create a human message with the image URL
    prompt = HumanMessage(
        content=[
            {"type": "text",
             "text": "Trích xuất thông tin bot từ ảnh gồm: tên bot, trạng thái tín hiệu, winrate (%), ROI (%) và loại bot (phái sinh/cơ sở)."},
            {"type": "image_url", "image_url": img["image_url"]},
        ]
    )

    try:
        # Invoke the LLM with the prompt
        result: BotInfo = structured_llm.invoke([prompt])
        print(f"- Kết quả có cấu trúc: {result}")
        # Append the result to the output list
        output_results.append({
            "filename": img["filename"],
            "bot_info": result.dict()
        })
    except Exception as e:
        # Handle any errors during processing
        print(f"-- Lỗi khi xử lý ảnh {img['filename']}: {e}")
        output_results.append({
            "filename": img["filename"],
            "error": str(e)
        })

# Save the output results to a JSON file
output_file = Path("F:/Thuc_tap/automation-testing/structured-output/san_bot_result.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_results, f, ensure_ascii=False, indent=2)

print(f"\n- Kết quả đã được lưu vào: {output_file}")

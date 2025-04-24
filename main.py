from openai import OpenAI
import requests

# === Cấu hình ===
OPENAI_API_KEY = "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"
TELEGRAM_TOKEN = "8035399118:AAHj_Misk6wnjHpAbTHkG4_93EAp-l-j_gE"
TELEGRAM_CHAT_ID = "1533204526"

# === Prompt GPT tạo call lệnh ===
PROMPT = """
Dựa trên dữ liệu kỹ thuật giả định, hãy tạo call lệnh dạng ngắn gọn cho BTC (khung giờ 1H). 
Chỉ dùng định dạng sau: 
MUA/BÁN BTC @giá vào – SL – TP.
Không phân tích dài dòng.
"""

# === Gọi GPT theo chuẩn mới ===
client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(model="gpt-3.5-turbo",
                                          messages=[{
                                              "role": "user",
                                              "content": PROMPT
                                          }])
call = response.choices[0].message.content


# === Gửi về Telegram ===
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    requests.post(url, data=payload)


send_to_telegram(call)

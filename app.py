import gradio as gr
from google import genai

# 1. วางรหัส API Key ของคุณที่นี่ (ห้ามลืมเครื่องหมายคำพูด)
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

# 2. เชื่อมต่อระบบใหม่ (New SDK 2026)
client = genai.Client(api_key=MY_API_KEY)

def chat_fn(message, history):
    try:
        # ใช้รุ่น gemini-1.5-flash ผ่านระบบใหม่
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=message,
            config={
                'system_instruction': "คุณคือน้องกุ้ง แอดมินร้านจัดสวนและขายหญ้า ตอบลูกค้าอย่างสุภาพและปิดการขายเก่งๆ"
            }
        )
        return response.text
    except Exception as e:
        return f"ขออภัยครับ ระบบขัดข้อง: {str(e)}"

# 3. สร้างหน้าจอแชท
demo = gr.ChatInterface(fn=chat_fn, title="Nong Kung AI (New System)")

if __name__ == "__main__":
    # ตั้งค่า share=True เพื่อให้ได้ลิงก์ .gradio.live
    demo.launch(share=True)

import gradio as gr
from google import genai

# 1. วางรหัส API Key ของคุณที่นี่
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

# 2. ตั้งค่าการเชื่อมต่อแบบใหม่ (New SDK)
client = genai.Client(api_key=MY_API_KEY)

def chat_fn(message, history):
    try:
        # ใช้รุ่น gemini-1.5-flash
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=message,
            config={
                'system_instruction': "คุณคือน้องกุ้ง แอดมินขายหญ้าและจัดสวน ตอบลูกค้าอย่างสุภาพและเป็นมืออาชีพ"
            }
        )
        return response.text
    except Exception as e:
        return f"ขออภัยครับ เกิดปัญหา: {str(e)}"

# 3. สร้างหน้าจอแชท
demo = gr.ChatInterface(
    fn=chat_fn, 
    title="Nong Kung AI (New System)",
    description="ระบบน้องกุ้งเวอร์ชันอัปเดตใหม่ล่าสุด"
)

if __name__ == "__main__":
    # เปิด share=True เพื่อให้ได้ลิงก์ .gradio.live มาใช้
    demo.launch(share=True)

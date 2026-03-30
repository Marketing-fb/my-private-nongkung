import google.generativeai as genai
import gradio as gr

# 1. วางรหัส API Key ของคุณตรงนี้ (อย่าลืมเครื่องหมายคำพูดนะครับ)
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

genai.configure(api_key=MY_API_KEY)

def chat_fn(message, history):
    # ใช้รุ่น gemini-pro เพราะเป็นรุ่นมาตรฐานที่เข้าถึงได้ทุกคนครับ
    try:
        model = genai.GenerativeModel('gemini-pro')
        # ใส่คำสั่งเบื้องหลังแบบง่ายๆ
        full_prompt = f"คุณคือน้องกุ้ง แอดมินขายหญ้าและจัดสวน ตอบคำถามนี้อย่างสุภาพ: {message}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"ขออภัยครับ เกิดปัญหา: {str(e)}"

# 2. สร้างหน้าจอแชท และเปิดโหมด Share
demo = gr.ChatInterface(
    fn=chat_fn, 
    title="Nong Kung AI (Stable Version)",
    theme="soft"
)

if __name__ == "__main__":
    # share=True จะช่วยสร้างลิงก์พิเศษที่ใช้งานได้แน่นอน
    demo.launch(share=True)

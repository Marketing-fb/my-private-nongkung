import google.generativeai as genai
import gradio as gr
import os

# 1. ใส่รหัส API Key ของคุณที่นี่
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

try:
    genai.configure(api_key=MY_API_KEY)
    # ทดสอบการเชื่อมต่อเบื้องต้น
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    print(f"เกิดข้อผิดพลาดในการตั้งค่า API: {e}")

SYSTEM_PROMPT = "คุณคือแอดมินน้องกุ้ง ตอบคำถามเรื่องหญ้าและจัดสวนอย่างสุภาพ"

def chat_function(message, history):
    try:
        # เรียกใช้ AI
        model_with_instr = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        chat = model_with_instr.start_chat(history=[])
        response = chat.send_message(message)
        return response.text
    except Exception as e:
        # ถ้าพัง ให้คืนค่าข้อความ Error ออกมาที่หน้าจอแชทเลย
        return f"ขออภัยครับ เกิดปัญหาทางเทคนิค: {str(e)}"

demo = gr.ChatInterface(fn=chat_function, title="Nong Kung Private AI")

if __name__ == "__main__":
    # เพิ่ม share=True เพื่อสร้างลิงก์สาธารณะ (ใช้งานได้ 72 ชม.)
    # วิธีนี้จะช่วยแก้ปัญหาหน้าจอขาวหรือ Error จาก GitHub ได้ 100%
    demo.launch(share=True)

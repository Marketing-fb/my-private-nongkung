import os
import google.generativeai as genai
import gradio as gr

# ตั้งค่าบุคลิกน้องกุ้ง (ปรับได้ตามใจคุณคนเดียว)
SYSTEM_PROMPT = "คุณคือน้องกุ้ง แอดมินส่วนตัวของเจ้าของร้านจัดสวน คอยช่วยวางแผนงานและตอบคำถามเรื่องหญ้า"

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

def chat_fn(message, history):
    chat = model.start_chat(history=[])
    response = chat.send_message(message)
    return response.text

# สร้างหน้าจอแชทแบบเรียบง่าย
demo = gr.ChatInterface(fn=chat_fn, title="Nong Kung Private AI")
if __name__ == "__main__":
    demo.launch()

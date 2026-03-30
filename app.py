import google.generativeai as genai
import gradio as gr

# 1. วางรหัส API Key ของคุณตรงนี้
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

genai.configure(api_key=MY_API_KEY)

def chat_fn(message, history):
    # รายชื่อโมเดลที่ต้องการลองใช้ (เรียงจากใหม่ไปเก่า)
    model_names = ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro']
    
    error_msg = ""
    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            response = model.generate_content(message)
            return response.text
        except Exception as e:
            error_msg = str(e)
            continue # ถ้าพัง ให้ลองรุ่นถัดไป
            
    return f"พยายามทุกรุ่นแล้วแต่ยังไม่ได้: {error_msg}"

# สร้างหน้าจอแชท
demo = gr.ChatInterface(fn=chat_fn, title="Nong Kung Private AI (Debug Mode)")

if __name__ == "__main__":
    # ใช้ share=True เพื่อให้ได้ลิงก์ .gradio.live ซึ่งเสถียรกว่าใน Codespaces
    demo.launch(share=True)

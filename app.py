import google.generativeai as genai
import gradio as gr

# 1. ใส่รหัส API Key ของคุณที่นี่
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

genai.configure(api_key=MY_API_KEY)

# 2. ตั้งค่าข้อมูลน้องกุ้ง
SYSTEM_PROMPT = "คุณคือแอดมินน้องกุ้ง ตอบคำถามเรื่องหญ้าและจัดสวนอย่างสุภาพครับ"

def chat_function(message, history):
    try:
        # เราจะลองใช้ gemini-1.5-flash-latest ซึ่งเป็นชื่อที่แน่นอนที่สุด
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash-latest', 
            system_instruction=SYSTEM_PROMPT
        )
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        # ถ้ายังพังอีก ให้ลองใช้รุ่น 1.0 Pro (รุ่นมาตรฐาน) เป็นตัวสำรอง
        try:
            model_backup = genai.GenerativeModel('gemini-pro')
            response = model_backup.generate_content(f"{SYSTEM_PROMPT}\n\nคำถามจากลูกค้า: {message}")
            return response.text
        except:
            return f"ระบบยังมีปัญหา: {str(e)}"

# 3. สร้างหน้าแชท
demo = gr.ChatInterface(fn=chat_function, title="Nong Kung Private AI")

if __name__ == "__main__":
    # ใช้ share=True เพื่อความชัวร์ จะได้ลิงก์ .gradio.live มาใช้
    demo.launch(share=True)

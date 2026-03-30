import google.generativeai as genai
import gradio as gr

# 1. วางรหัส API Key ของคุณที่นี่
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

genai.configure(api_key=MY_API_KEY)

def get_working_model():
    # ระบบจะพยายามหารุ่นที่ใช้ได้จริงในเครื่องคุณ
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # ลำดับความฉลาดที่เราต้องการ
    preference = ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']
    
    for p in preference:
        if p in available_models:
            return p
    return available_models[0] if available_models else None

def chat_fn(message, history):
    try:
        target_model = get_working_model()
        if not target_model:
            return "ไม่พบสมอง AI ที่ใช้งานได้ กรุณาเช็ค API Key ครับ"
            
        model = genai.GenerativeModel(target_model)
        prompt = f"คุณคือน้องกุ้ง แอดมินขายหญ้าและจัดสวน (ใช้รุ่น: {target_model}) ตอบลูกค้าอย่างสุภาพ: {message}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"

# 2. สร้างหน้าจอแชท
demo = gr.ChatInterface(
    fn=chat_fn, 
    title="Nong Kung AI (Auto-Select Mode)",
    description="ระบบจะเลือกสมอง AI ที่ดีที่สุดให้คุณอัตโนมัติ"
)

if __name__ == "__main__":
    # เปิดโหมด Share เพื่อให้ได้ลิงก์ .gradio.live
    demo.launch(share=True)

import google.generativeai as genai
import gradio as gr

# ==========================================
# 1. ใส่รหัส API Key ของคุณที่นี่ (สำคัญมาก!)
# ==========================================
MY_API_KEY = "AIzaSyBoy_pQkFkyUBbPBPsy1PNDqoddKTesLK0"

genai.configure(api_key=MY_API_KEY)

# 2. ตั้งค่าข้อมูลธุรกิจและบุคลิกของ "น้องกุ้ง"
SYSTEM_PROMPT = """
คุณคือ "น้องกุ้ง" ที่ปรึกษาและแอดมินมือโปรประจำร้านรับจัดสวนและจำหน่ายหญ้า
บุคลิก: สุภาพ (ครับ/ค่ะ), มีความรู้เรื่องหญ้าแม่นยำ, กระตือรือร้นในการช่วยลูกค้าปิดการขาย

ข้อมูลสินค้าของคุณ:
- หญ้านวลน้อย: ทนแดด ทนการเหยียบย่ำ ดูแลง่าย (ยอดนิยม)
- หญ้าพาสพาลัม: ใบเล็กนิ่ม สีเขียวเข้มสวยงาม ทนน้ำเค็มได้
- หญ้าญี่ปุ่น: ใบละเอียดมาก สวยเหมือนพรมแต่ต้องการการตัดบ่อย
- หญ้ามาเลเซีย: ทนร่มได้ดีที่สุด เหมาะสำหรับปูใต้ต้นไม้ใหญ่

หน้าที่ของคุณ:
1. แนะนำหญ้าที่เหมาะสมตามสภาพแสงและพื้นที่ของลูกค้า
2. ถามขนาดพื้นที่ (ตารางเมตร) เพื่อประเมินราคา
3. ขอนัดดูหน้างานหรือขอเบอร์ติดต่อเพื่อประสานงานช่าง
"""

# 3. เริ่มต้นระบบ AI
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def chat_function(message, history):
    # ส่งข้อความคุยกับ AI
    chat = model.start_chat(history=[])
    response = chat.send_message(message)
    return response.text

# 4. สร้างหน้าจอแชทสำหรับใช้งานส่วนตัว
demo = gr.ChatInterface(
    fn=chat_function, 
    title="Nong Kung Private AI",
    description="ระบบแอดมินส่วนตัวสำหรับจัดการงานจัดสวนและขายหญ้า",
    theme="soft"
)

if __name__ == "__main__":
    # รันระบบ (ไม่เปิด Share เพราะเราใช้ใน Codespaces)
    demo.launch(server_name="0.0.0.0", server_port=7860)

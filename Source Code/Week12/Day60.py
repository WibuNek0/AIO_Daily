import streamlit as st
import os
import google.generativeai as genai

# Lấy Google Gemini API key từ file .streamlit/secrets.toml
# Cần định nghĩa [google] api_key = "your_gemini_key" trong đó
gemini_api_key = st.secrets.get("google", {}).get("api_key")

# Cấu hình Gemini API
genai.configure(api_key=gemini_api_key)

# Tạo model
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Chat với Google Gemini")

# Khởi tạo history nếu chưa có
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Khởi tạo chat
    st.session_state.chat = model.start_chat(history=[])

# Hiển thị toàn bộ hội thoại
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    # Hiển thị tin nhắn của người dùng
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        # Gọi API Gemini để trả lời
        response = st.session_state.chat.send_message(prompt)
        reply = response.text
        
        # Hiển thị phản hồi
        st.chat_message("assistant").write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Lỗi khi gọi Gemini API: {str(e)}")
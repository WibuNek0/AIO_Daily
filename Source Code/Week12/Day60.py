import streamlit as st
import os
import requests  # import thư viện requests để gọi Google Gemini API

# Lấy Google Gemini API key từ file .streamlit/secrets.toml (cần định nghĩa [google] api_key = "your_gemini_key" trong đó)
google_api_key = st.secrets.get("google", {}).get("api_key")

st.title("Chat với Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị toàn bộ hội thoại
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gọi API Google Gemini text-bison-001
    endpoint = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={google_api_key}"
    payload = {
        "prompt": {"text": prompt},
        "temperature": 0.2,
        "maxOutputTokens": 1024
    }
    res = requests.post(endpoint, json=payload)
    if res.status_code == 200:
        data = res.json()
        reply = data["candidates"][0]["output"]
    else:
        reply = f"Error {res.status_code}: {res.text}"

    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
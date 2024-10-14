import streamlit as st
import time

def speech_to_sign_ui():
    # Custom CSS for the interface
    st.markdown("""
        <style>
            body {
                background: linear-gradient(145deg, #f0f4f8, #ffffff);
                font-family: 'Arial', sans-serif;
            }
            .title {
                font-size: 48px;
                color: #2c3e50;
                text-align: center;
                font-weight: bold;
                margin: 40px 0 20px 0;
                text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .subtitle {
                font-size: 20px;
                color: #34495e;
                text-align: center;
                margin-bottom: 40px;
                text-shadow: 1px 1px 5px rgba(0,0,0,0.1);
            }
            .button {
                background-color: #2980b9;
                color: white;
                border: none;
                padding: 15px 30px;
                text-align: center;
                font-size: 20px;
                border-radius: 30px;
                margin: 10px 0;
                cursor: pointer;
                width: 100%;
                transition: all 0.3s ease;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            }
            .button:hover {
                background-color: #3498db;
                transform: translateY(-2px);
                box-shadow: 0 6px 30px rgba(0, 0, 0, 0.2);
            }
            .button:active {
                transform: translateY(1px);
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            .intro-image {
                margin: 20px auto;
                display: block;
                width: 70%;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            }
            .result-text {
                font-size: 24px;
                color: #2c3e50;
                text-align: center;
                margin-top: 30px;
                animation: fadeIn 1s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .column {
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display title and subtitle
    st.markdown("<div class='title'>Chuyển Đổi Giọng Nói Sang Ngôn Ngữ Ký Hiệu</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Chuyển đổi giọng nói của bạn sang các ký hiệu.</div>", unsafe_allow_html=True)

    # Introductory image
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4MsLwQcrXHlHoIezTPh2ba2K7rD3bOC_Tos72H0yjtojxilsCNJszTDuDIxLegfQS9KppgGNdouCx3EbJtaX0mH82X4gEZvGrnhPVyK-dRzPTUi7aXn7jxxVXgcOozxrJ7BA-pg9F7rMMg51qmJuP-AT_kO9RebzDvajBO7KrEmh7NrZtqg-EnFU3/s16000/Traveling%20with%20a%20Disability%20in%20Vietnam%2004.jpg", 
             use_column_width=True, caption="Chào mừng đến với ứng dụng Ngôn Ngữ Ký Hiệu", output_format="PNG")

    # Buttons for functionalities
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='column'>", unsafe_allow_html=True)
        if st.button("Nhập Văn Bản", key='text_input_button', help="Nhập văn bản để chuyển đổi sang ngôn ngữ ký hiệu"):
            text_input = st.text_input("Nhập văn bản của bạn:", "")
            if text_input:
                st.markdown(f"<div class='result-text'>Bạn đã nhập: '{text_input}'</div>", unsafe_allow_html=True)
                # Placeholder for displaying the image based on text
                st.image("https://via.placeholder.com/300?text=Ký+Hiệu+Tương+Ứng", caption="Hình ảnh ngôn ngữ ký hiệu tương ứng", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='column'>", unsafe_allow_html=True)
        if st.button("Bắt đầu nói", key='start_button', help="Nhấn để bắt đầu nhận diện giọng nói"):
            st.write("Đang lắng nghe... Hãy nói vào micro!")
            time.sleep(2)  # Simulate processing time
            st.markdown("<div class='result-text'>Bạn đã nói: 'Xin chào'</div>", unsafe_allow_html=True)
            # Example image with 3D effect
            st.image("https://via.placeholder.com/300?text=Ký+Hiệu+Tương+Ứng", caption="Hình ảnh ngôn ngữ ký hiệu tương ứng", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)



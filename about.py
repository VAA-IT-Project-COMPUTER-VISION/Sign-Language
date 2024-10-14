import streamlit as st
import pandas as pd

def show_about_app():
    st.title('Nhận diện ngôn ngữ ký hiệu qua cử chỉ tay sử dụng thị giác máy tính')
    st.markdown('''
        Trong ứng dụng này, chúng tôi sử dụng **MediaPipe** để phát hiện ngôn ngữ ký hiệu. 
        Thư viện **SpeechRecognition** của Python để nhận diện giọng nói và thuật toán máy học chuyển đổi giọng nói thành ngôn ngữ ký hiệu.
    ''')

    # Hình ảnh đầu trang
    st.markdown('<div class="image-container"><img src="https://www.1specialplace.com/wp-content/uploads/2022/06/Sign-Language-around-the-World-1SpecialPlace.jpg" alt="Image" /></div>', unsafe_allow_html=True)

    st.markdown('<div class="title">THÀNH VIÊN NHÓM 04</div>', unsafe_allow_html=True)

    st.markdown('''
    <div class="section">
        <strong>HỌC PHẦN:</strong> Xử lý ảnh và thị giác máy tính <br>
        <strong>Giảng viên:</strong> Trần Nguyên Bảo <br>
        <strong>Mã lớp học phần:</strong> 010100086905 <br>
        <strong>Tên đề tài:</strong> Nhận diện ngôn ngữ ký hiệu qua cử chỉ tay sử dụng thị giác máy tính
    </div>
    ''', unsafe_allow_html=True)

    members = [
        {"STT": 1, "Họ và tên": "Lê Hoàng Anh", "MSSV": "2154810101"},
        {"STT": 2, "Họ và tên": "Phan Tuấn Anh", "MSSV": "2254810044"},
        {"STT": 3, "Họ và tên": "Nguyễn Hữu Minh Hoàng", "MSSV": "2254810155"},
        {"STT": 4, "Họ và tên": "Đinh Hữu Đức", "MSSV": "2254810323"},
        {"STT": 5, "Họ và tên": "Nguyễn Ngọc Thảo Ngân", "MSSV": "2254810252"},
    ]

    # Tạo DataFrame từ danh sách thành viên
    df_members = pd.DataFrame(members)

    # Hiển thị bảng thành viên với CSS
    st.markdown('''
        <style>
            body {
                background-color: #f0f4f8;  /* Màu nền sáng */
                font-family: 'Arial', sans-serif;
                color: #333;
            }
            .title {
                text-align: center;
                font-size: 28px;
                color: #4CAF50;
                margin: 20px 0;
                text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
                animation: fadeIn 1.5s ease;
            }
            .section {
                margin: 20px auto;
                padding: 20px;
                background: #ffffff;
                border-radius: 10px;
                box-shadow: 0 6px 30px rgba(0, 0, 0, 0.1);
                animation: slideIn 0.5s ease;
                max-width: 800px; /* Giới hạn chiều rộng */
                transition: transform 0.3s; /* Hiệu ứng 3D khi di chuột */
            }
            .section:hover {
                transform: translateY(-5px) scale(1.02); /* Hiệu ứng phóng to */
            }
            .member-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 1em;
                font-family: 'Arial', sans-serif;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            }
            .member-table th, .member-table td {
                padding: 15px;
                text-align: center;
                border: 1px solid #4CAF50;
                transition: background-color 0.3s, transform 0.3s;
            }
            .member-table th {
                background-color: #4CAF50;
                color: white;
                border-bottom: 2px solid #388E3C; /* Đường viền dưới cho tiêu đề */
                text-transform: uppercase; /* Chữ hoa cho tiêu đề */
            }
            .member-table tr:nth-child(even) {
                background-color: #f9f9f9; /* Màu nền cho hàng chẵn */
            }
            .member-table tr:hover {
                background-color: #e0f7fa;
                transform: translateY(-3px); /* Hiệu ứng nâng lên khi di chuột */
            }
            .image-container {
                text-align: center;
                margin-top: 20px;
                animation: fadeIn 1.5s ease; /* Hiệu ứng xuất hiện cho hình ảnh */
            }
            img {
                width: 100%;  /* Kích thước hình ảnh lớn hơn */
                max-width: 800px; /* Kích thước tối đa */
                height: auto;
                border-radius: 15px;  /* Tạo bo góc cho hình ảnh */
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);  /* Hiệu ứng bóng cho hình ảnh */
                transition: transform 0.3s; /* Hiệu ứng phóng to hình ảnh */
            }
            img:hover {
                transform: scale(1.05); /* Hiệu ứng phóng to khi di chuột */
            }
            h4 {
                color: #4CAF50;
                margin-top: 20px;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideIn {
                from { transform: translateY(-20px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown(df_members.to_html(classes='member-table', index=False), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="image-container"><img src="https://www.signsolutions.uk.com/wp-content/uploads/2022/03/AdobeStock_253122665.jpeg" alt="Image" /></div>', unsafe_allow_html=True)

    # Khu vực video hướng dẫn
    st.markdown('''
        <div class="section">
            <h4>Video Demo</h4>
            <p>Video sẽ được thêm vào sau</p>
        </div>
    ''', unsafe_allow_html=True)

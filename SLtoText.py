import streamlit as st
import cv2
import tempfile
import os

def SLtoText():
    st.title('Sign Language to Text', anchor=None)  # Set the title without an anchor
    st.markdown("""
        <style>
            .title {
                color: #4B0082;  /* Indigo color */
                font-size: 32px;
                font-weight: bold;
                text-align: center;
            }
            .output-text {
                font-size: 24px;
                color: #2E8B57; /* SeaGreen color */
                text-align: center;
                margin: 20px 0;
            }
            .sidebar-title {
                font-size: 18px;
                font-weight: bold;
                color: #FF6347;  /* Tomato color */
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar options
    st.sidebar.markdown('<p class="sidebar-title">Video Input Options</p>', unsafe_allow_html=True)
    use_webcam = st.sidebar.button('Use Webcam')
    record = st.sidebar.checkbox("Record Video")
    
    st.sidebar.markdown('---')
    
    # File uploader
    st.sidebar.markdown('<p class="sidebar-title">Upload Video File</p>', unsafe_allow_html=True)
    video_file_buffer = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", 'avi', 'asf', 'm4v'])
    
    # Output area
    st.markdown('## Output', unsafe_allow_html=True)
    output_text = ""  # Placeholder for output text
    st.markdown(f'<p class="output-text">{output_text}</p>', unsafe_allow_html=True)

    # Placeholder for video frame
    stframe = st.empty()

    # Temporary file for video upload
    tfflie = tempfile.NamedTemporaryFile(delete=False)

    if not video_file_buffer:
        if use_webcam:
            vid = cv2.VideoCapture(0)  # Use webcam if selected
        else:
            # Demo video path
            DEMO_VIDEO = 'demo.mp4'
            vid = cv2.VideoCapture(DEMO_VIDEO)
            tfflie.name = DEMO_VIDEO
    else:
        tfflie.write(video_file_buffer.read())
        tfflie.close()  # Close the temporary file after writing
        vid = cv2.VideoCapture(tfflie.name)

    # Get video properties
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_input = int(vid.get(cv2.CAP_PROP_FPS))

    # Prepare output video writer
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # Use * for better readability
    output_file_name = 'output1.mp4'
    out = cv2.VideoWriter(output_file_name, codec, fps_input, (width, height))

    st.markdown("<hr/>", unsafe_allow_html=True)

    # Video processing loop
    while True:
        ret, img = vid.read()
        if not ret:
            break  # Break the loop if the video ends

        img = cv2.flip(img, 1)  # Flip image horizontally
        frame = cv2.resize(img, (640, 480))  # Resize frame
        stframe.image(frame, channels='BGR', use_column_width=True)  # Display frame
        
        # Write the processed frame to output video
        out.write(img)

    # Finished processing
    st.text('Video Processed')

    # Release resources
    vid.release()
    out.release()

    # Check if video output file was created
    if os.path.exists(output_file_name):
        # Output the video
        with open(output_file_name, 'rb') as output_video:
            out_bytes = output_video.read()
            st.video(out_bytes)
    else:                  
        st.error("Video output file not found.")

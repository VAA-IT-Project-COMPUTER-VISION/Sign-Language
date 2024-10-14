import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image
from styles import apply_styles
from about import show_about_app
from SLtoText import SLtoText
from interface import speech_to_sign_ui


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Apply styles to the app
apply_styles()

# Sidebar title and header
st.sidebar.markdown('<p class="sidebar-title">Image Processing & Computer Vision</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="sidebar-subheader">Sign Language Detection</p>', unsafe_allow_html=True)

# Function to resize images
@st.cache_data()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

# Dropdown for app mode
app_mode = st.sidebar.selectbox('Choose the App mode', [
    'About App', 
    'Sign Language to Text', 
    'Text to Sign Language'
])

# Main application logic based on selected mode
if app_mode == 'About App':
    show_about_app()  # Show the About section
elif app_mode == 'Sign Language to Text':
    SLtoText()  # Call the sign language to text function
elif app_mode == 'Text to Sign Language':
    # Add functionality for Text to Sign Language here
    speech_to_sign_ui()


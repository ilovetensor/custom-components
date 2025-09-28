import streamlit as st
from my_component import my_component
from PIL import Image
from io import BytesIO
import base64

# Image Processing Functions
def image_to_base64_url(image):
    """Convert PIL image to base64 data URL"""
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

def crop_image(image, crop_params):
    """Crop image based on provided parameters"""
    return image.crop((
        crop_params['x'],
        crop_params['y'], 
        crop_params['x'] + crop_params['width'],
        crop_params['y'] + crop_params['height']
    ))

# Main Application
st.title("🖼️ Image Cropper")
st.markdown("Upload an image and use the interactive cropper to select a portion of it.")

# Image Upload Section
st.header("📁 Upload Image")
image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "webp"], help="Supported formats: JPG, JPEG, PNG, WEBP")

if image:
    # Process uploaded image
    pil_image = Image.open(image)
    image_url = image_to_base64_url(pil_image)
    
    # Cropping Controls
    st.header("⚙️ Cropping Settings")
    aspect_ratio = st.slider(
        "Aspect Ratio", 
        min_value=0.1, 
        max_value=1.0, 
        value=1.0, 
        step=0.1,
        help="Adjust the aspect ratio for the crop selection"
    )
    
    # Interactive Cropper
    st.header("✂️ Crop Selection")
    st.markdown("Use the interactive cropper below to select the area you want to crop.")
    crop_params = my_component(image_url, aspect_ratio=aspect_ratio, key="cropper")
    
    # Display Results
    if crop_params:
        st.header("📸 Cropped Result")
        cropped_image = crop_image(pil_image, crop_params)
        
        with st.container(key="cropped_image"):
            st.image(cropped_image, caption="Your Cropped Image")
        
        # Crop Parameters Display
        st.subheader("📊 Crop Parameters")
        st.json(crop_params)
        
        # Styling for cropped image
        st.markdown("""
        <style>
        .st-key-cropped_image img {
            border: 1px solid red;
            box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
            border-radius: 50%;
            padding: 10px;
            margin: 10px;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
        }
        </style>
        """, unsafe_allow_html=True)
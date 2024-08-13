import streamlit as st
import requests
import json

# Define the API endpoint and API key
API_ENDPOINT = "https://modelslab.com/api/v6/video/text2video"
API_KEY = "xiMN5ez5IVTbDtCsQmKS5DlcXRWAlDJ6DmbUPP7xqNPHUC7ZqsQe7gvQ1Etk"

# Create the Streamlit app
st.title("Text-to-Video Generation")

# Get user input
prompt = st.text_area("Enter a prompt:", height=100)
negative_prompt = st.text_area("Enter a negative prompt (optional):", height=50)
model_id = st.selectbox("Select a model:", ["zeroscope", "dark-sushi-mix-vid", "epicrealismnaturalsi-vid", "hellonijicute25d-vid"])
height = st.number_input("Video height (max 512):", min_value=1, max_value=512, value=320, step=1)
width = st.number_input("Video width (max 512):", min_value=1, max_value=512, value=512, step=1)  # Set default to 512
num_frames = st.number_input("Number of frames (max 25):", min_value=1, max_value=25, value=16, step=1)
num_inference_steps = st.number_input("Number of inference steps (max 50):", min_value=1, max_value=50, value=20, step=1)
guidance_scale = st.number_input("Guidance scale (0-8):", min_value=0.0, max_value=8.0, value=7.0, step=0.1)
output_type = st.selectbox("Output type:", ["mp4", "gif"])

# Create a button to generate the video
if st.button("Generate Video"):
    # Prepare the request payload
    payload = {
        "key": API_KEY,
        "model_id": model_id,
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width,
        "num_frames": num_frames,
        "num_inference_steps": num_inference_steps,
        "guidance_scale": guidance_scale,
        "output_type": output_type
    }

    # Send the POST request to the API
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))

    # Display the generated video
    if response.status_code == 200:
        result = response.json()
        video_url = result["output"][0]
        st.video(video_url)
    else:
        st.error("Error generating the video.")

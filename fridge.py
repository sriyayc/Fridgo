###        Invoice extractor

## Importing All the modules
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv


# Load all environment Variables
load_dotenv()

## Configuring the api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Vision Pro Vision Model and Get response
def get_gemini_response(input, image, prompt):
    ## Loading the desired Model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, image[0], prompt])
    return response.text

## Function to extract data from Image Uploaded
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
# Initializing our Streamlit Prompt
st.set_page_config(page_title="Gemini Image Demo")

st.header("Fridgo")
input = "Identify the vegetables from the image and suggest me the recipes that can be made using them and give me the number of calories for each recipe."

# Asking the user if they have any allergies
allergy_input = st.text_input("Do you have any food allergies? (e.g., peanuts, gluten, dairy)")
disease_input = st.text_input("Do you have any health issues")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Submit")

##  DEFINING A SYSTEM PROMPT

# If there is an allergy input, include it in the prompt
if allergy_input:
    allergy_info = f" Avoid any recipes that contain {allergy_input}."
else:
    allergy_info = ""

if disease_input:
    disease_info = f" Avoid any recipes that contain {disease_input}."
else:
    disease_info = ""

input_prompt = f"You have been given an image which contains different vegetables. Identify the number of vegetables and different types of vegetables and list them. Also list all different recipes (both veg and non-veg) that can be made from them, and give me calories for each recipe.{allergy_info} avoid reciepies which includes this, and i have {disease_info} so suggest me recipies accordingly"

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)

    st.subheader("Items and available recipes are: ")
    st.write(response)

    st.balloons()

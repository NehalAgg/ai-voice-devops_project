import streamlit as st
import requests
import speech_recognition as sr

# 1. Setup the webpage design
st.set_page_config(page_title="AI Voice Assistant", page_icon="🎙️")
st.title("🎙️ AI Voice Intent Classifier")
st.write("Welcome to the DevOps AI Project! Click the button below and tell me what to do.")

# 2. Create the big button
if st.button("🎤 Click Here to Speak"):
    
    recognizer = sr.Recognizer()
    
    # 3. Turn on the microphone
    with sr.Microphone() as source:
        st.info("Listening... Speak clearly into your mic!")
        
        try:
            # Capture the audio
            audio = recognizer.listen(source, timeout=5)
            st.success("Got it! Processing your voice...")
            
            # Translate voice to text
            text = recognizer.recognize_google(audio)
            st.write(f"**You said:** '{text}'")
            
            # 4. Send the text to your "Brain" (FastAPI)
            # We assume your API uses /predict. 
            response = requests.post(f"http://127.0.0.1:8000/predict?text={text}")
            
            if response.status_code == 200:
                intent = response.json()
                st.success(f"🤖 **Predicted Intent:** {intent}")
            else:
                st.error("Uh oh! The Brain (FastAPI) didn't understand. Is it running?")
                
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand what you said. Try again!")
        except sr.RequestError:
            st.error("Could not connect to Google's voice service.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
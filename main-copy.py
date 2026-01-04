import streamlit as st
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def school_chatbot(user_input):
    user_input = user_input.lower()
# Basic greetings and information
#“The chatbot first checks predefined rules using if–else logic.
#If no rule matches, the query is forwarded to Gemini for general information.”

    if "hello" in user_input or "hi" in user_input:
        return "Hello!"
    elif "how are you" in user_input:
        return "I am just a bot, but thank you for asking!"
    elif "what is your name" in user_input:
        return "I am the School Helpdesk Voice Bot."
    elif "who created you" in user_input:
        return "I was created by Head boy of the school Pranay."
    elif "what can you do" in user_input:
        return "I can help you with information about school timings, exams, subjects, and teachers."

    elif "application form" in user_input:
        return "You can obtain the application form from the school office or download it from the school's official website."
    elif "fee structure" in user_input:
        return  "You can contact the school office for detailed information about the fee structure."
    elif "admission process" in user_input:
        return "The admission process typically involves filling out an application form, submitting required documents, and attending an interview or assessment if necessary. Please contact the school office for specific details."
        
    elif "admission form" in user_input:
        return "You can obtain the admission form from the school office or download it from the school's official website."
    
    elif 'help with admission' in user_input or 'admission help' in user_input or 'help' in user_input:
        return "I can assist you with information about application forms, fee structure, admission process, and admission forms. If you have another query you can contact the school office for further assistance."
    
    elif 'house system' in user_input:
        if "working" in user_input:
            return "There are four houses in our school: Raman, Gandhi, Shivaji and Tagore. Students are assigned to houses to promote teamwork and healthy competition through various activities and events."
        elif "portfolios" in user_input:
            return "The house portfolios include House Captain, House representative Sports Captain, Cultural Captain, and Discipline Captain. These roles help in organizing house activities and fostering leadership among students. And there are other designations too head boy,school representative, school solicitor, students coordinatior."
        else:
            return "The school has a house system with four houses: Raman, Gandhi, Shivaji, and Tagore. Students are assigned to houses to promote teamwork and healthy competition through various activities and events. The house portfolios include House Captain, House representative Sports Captain, Cultural Captain, and Discipline Captain. These roles help in organizing house activities and fostering leadership among students."
        
    elif " school timing" in user_input or "school timings" in user_input or "school hours" in user_input:
        if "primary" in user_input:
            return "Primary school timings are from 10 AM to 3 PM."
        elif "higher" in user_input:
            return "Higher school timings are from 7:15 AM to 1:10 PM."
        elif "middle" in user_input:
            return "Middle school timings are from 8:30 AM to 3:00 PM."
        else:
            return "School timings are from 10 AM to 3 PM, 7:15 AM to 1:10 PM, and 8:30 AM to 3:00 PM for primary, Higher, and middle schools respectively."

    elif "exam" in user_input:
        return "Exams are conducted as per the academic calendar."

    elif "subject" in user_input:
        if "primary" in user_input:
            return "Primary school subjects include Math, Science, English, and Social Studies."
        elif "higher" in user_input:
            return "Higher school subjects include Math, Science, English, and Social Studies."
        elif "middle" in user_input:
            return "Middle school subjects include Math, Science, English, and Social Studies."
        else:
            return "Subjects include Math, Science, English, and Social Studies."


    elif "teacher" in user_input:
        return "Please ask incharge Veena Sharma mam for precise information."

    elif "exit" in user_input or "bye" in user_input or "thank" in user_input:
        return "Thank you for using the School Helpdesk. Goodbye."
    
    elif "lunch timing" in user_input or "lunch break" in user_input or "lunch hours" in user_input or "lunch timings" in user_input:
        if "primary" in user_input:
            return "Primary school lunch break is from 12 PM to 12:30 PM."
        elif "higher" in user_input:
            return "Higher school lunch break is at 10 AM for 20 minutes."
        elif "middle" in user_input:
            return "Middle school lunch break is from 10:30 for 20 minutes."
        else:
            return "Lunch breaks are 12 PM to 12:30 PM, 10 AM for 20 minutes, and 10:30 for 20 minutes for primary, higher, and middle schools respectively."
    
    elif 'principal information' in user_input or "about principal" in user_input:
        return "The principal of our school is Mister Navin Mudgal. He has many ahivements and recongnitions in the field of education and is dedicated to the overall development of students."
    
    elif 'vice principal information' in user_input or "vice principal" in user_input or "VP" in user_input or "vp mam" in user_input:
        return "The vice principal of our school is Misses Rupali Trivedi. She is very kind and helpful towards students and staff. And she also has many achivements and recongitions."

    else:
        return "I'm sorry, I don't have specific information about that right now. I can help you with school timings, subjects, exams, teachers, house system, admissions, and other school-related topics. Please ask about those or contact the school office for more details."


# Streamlit UI
st.title("Shri Cloth Market Vaishnav Higher Secondary School Helpdesk Chatbot")

st.write("Welcome! Ask me questions about the school.")

# Load and apply custom CSS
with open('style.css', 'r') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display conversation history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message['role'] == 'You':
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Spacer to push input to bottom
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Speak button
if st.button("🎤 Speak"):
    try:
        with sr.Microphone() as source:
            st.info("Listening... Please speak now.")
            audio = recognizer.listen(source, timeout=5)
            spoken_text = recognizer.recognize_google(audio)
            
            # Add user message
            st.session_state.messages.append({"role": "You", "content": spoken_text})
            
            # Get bot response
            reply = school_chatbot(spoken_text)
            
            # Add bot message
            st.session_state.messages.append({"role": "Bot", "content": reply})
            
            st.success(f"You said: {spoken_text}")
            st.rerun()
    except sr.WaitTimeoutError:
        st.error("No speech detected. Please try again.")
    except sr.UnknownValueError:
        st.error("Could not understand the speech. Please try again.")
    except sr.RequestError as e:
        st.error(f"Speech recognition error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# User input at the bottom
with st.form(key='chat_form'):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Enter your query:", label_visibility="collapsed")
    with col2:
        send_button = st.form_submit_button("Send", use_container_width=True)

if send_button and user_input:
    # Add user message
    st.session_state.messages.append({"role": "You", "content": user_input})
    
    # Get bot response
    reply = school_chatbot(user_input)
    
    # Add bot message
    st.session_state.messages.append({"role": "Bot", "content": reply})
    
    # Rerun to update display
    st.rerun()

# Optional: Add a clear button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

import speech_recognition as sr
from gtts import gTTS
import pygame

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    pygame.mixer.quit()

def school_chatbot(user_input):

    if "timing" in user_input:
        return "School timings are from 8 AM to 2 PM."

    elif "exam" in user_input:
        return "Exams are conducted as per the academic calendar."

    elif "subject" in user_input:
        return "Subjects include Maths, Science, English, Social Science, Computer Science, and AI."

    elif "teacher" in user_input:
        return "Each subject has a dedicated teacher. Please ask about a subject."

    elif "exit" in user_input or "bye" in user_input:
        return "Thank you for using the School Helpdesk. Goodbye."

    else:
        return "Sorry, I did not understand. Please ask about school timings, exams, subjects, or teachers."

# Speech Recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

speak("Welcome to the School Helpdesk Voice Bot")

while True:
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_voice = recognizer.recognize_google(audio)
        print("You:", user_voice)

        reply = school_chatbot(user_voice)
        print("Bot:", reply)
        speak(reply)

        if "goodbye" in reply.lower():
            break

    except:
        speak("Sorry, I could not hear you properly. Please try again.")

import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def school_chatbot(user_input):

# Basic greetings and information

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
    elif "help" in user_input:
        if "application form" in user_input:
            return "You can obtain the application form from the school office or download it from the school's official website."
        elif "fee structure" in user_input:
            return  "You can contact the school office for detailed information about the fee structure."
        elif "admission process" in user_input:
            return "The admission process typically involves filling out an application form, submitting required documents, and attending an interview or assessment if necessary. Please contact the school office for specific details."
        
        elif "admission form" in user_input:
            return "You can obtain the admission form from the school office or download it from the school's official website."
        else:
            return "I can assist you with information about application forms, fee structure, admission process, and admission forms. If you have another query you can contact the school office for further assistance."
    
    elif 'house system' in user_input:
        if "working" in user_input:
            return "There are four houses in our school: Raman, Gandhi, Shivaji and Tagore. Students are assigned to houses to promote teamwork and healthy competition through various activities and events."
        elif "portfolios" in user_input:
            return "The house portfolios include House Captain, House representative Sports Captain, Cultural Captain, and Discipline Captain. These roles help in organizing house activities and fostering leadership among students. And there are other designations too head boy,school representative, school solicitor, students coordinatior."
        else:
            return "The school has a house system with four houses: Raman, Gandhi, Shivaji, and Tagore. Students are assigned to houses to promote teamwork and healthy competition through various activities and events. The house portfolios include House Captain, House representative Sports Captain, Cultural Captain, and Discipline Captain. These roles help in organizing house activities and fostering leadership among students."
        
    elif " school timing" in user_input:
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
    
    elif "lunch timing" in user_input:
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
    
    elif 'vice principal information' in user_input or "about vice principal" in user_input:
        return "The vice principal of our school is Misses Rupali Trivedi. She is very kind and helpful towards students and staff. And she also has many achivements and recongitions."
    
    else:
        return "Sorry, I did not understand. Please ask about school timings, exams, subjects, or teachers."

    

    #general interactions


# Speech Recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

#interaction jaha se chalu hoga

speak("Welcome to the Shri Cloth Market vaishnav higher secondary Helpdesk Voice Bot")
speak("Would you like to chat or speak with the bot?")
print("Type 'speak' to use voice mode or 'chat' to type your queries:")

mode = input().strip().lower()
if mode == "speak":
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

elif mode == "chat":
    print("You can start chatting with the bot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        reply = school_chatbot(user_input)
        print("Bot:", reply)

        if "goodbye" in reply.lower():
            break

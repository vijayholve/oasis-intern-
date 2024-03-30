
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
webs = [
    "SNAPCHAT","youtube"
    ,"google","instagram","telegram",
    "TIKTOK","PINTEREST","TWITTER","FACEBOOK","LINKEDIN",
    "whatsapp",
    "TUMBLR",
    "VSCO",
    "FLICKR",
    "IMGUR",
    "WEHEARTIT",
    "500PX",
    "ELLO",
    "EYEEM",
    "PICSART",
    "DEVIANTART",
    "BEHANCE",
    "DRIBBBLE",
    "PHOTOBUCKET",
    "PEACH"
]
recn = sr.Recognizer()

def take():
    with sr.Microphone() as source:
        
        recn.adjust_for_ambient_noise(source, duration=1)
        print("listening")
        audio=recn.listen(source, timeout=5)
        print("speech into the text")
        try:
            text2=recn.recognize_google(audio, language="en-IN", show_all=False)
        except:
            print("try again")
        print(text2)
        return text2.lower()
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()


while True:
    # try:
    text=take()
    # except:
    #     text=input("enter quiry: ")
    text_list=text.split()
    

    print(text_list)

    if "open" in text:
        for web in webs:
            if web.lower() in text:
                webbrowser.open(f"https://www.{web.lower()}.com")
                tts(f"open {web}")
    elif "search" in text:
        index_of_search=text.find("search")
        text_list.remove("search")
        search="+".join(text_list)
        
        print(search)
        webbrowser.open(F"https://www.google.com/search?q={search}")
        # tts(f"open to {text} searched {my_list[1]}")
    
    elif "stop" in text:
        #out of loop
        break
    elif "start hack" in text:
       def hack_in_process():
            tts("your accound is hacked")
            sleep(2)
            pyautogui.hotkey('win','r')
            sleep(0.3)
            #x=202, y=804
            pyautogui.click(x=202, y=804)
            sleep(0.3)
            pyautogui.hotkey('alt','enter')
            pyautogui.typewrite("color 0a")
            pyautogui.hotkey("enter")
            pyautogui.typewrite("dir/s")
            pyautogui.hotkey("enter")
        
    elif "weather" in text:
        for city in cities:
            if city.lower() in text:
                print(city)
                tts(f'in {city} temprature is {get_current_weather(city.lower())}')
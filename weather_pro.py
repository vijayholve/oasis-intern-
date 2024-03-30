import requests
import pyttsx3
def get_current_weather(city):
    try:
        api_key = "57e7f4bd73b842fea74103246240802"
        url=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
    except :
        print("rong api key")
    
    temp=data["current"]["temp_f"]
    print("temrature is :",temp)
    tts(f"temrature is :{temp}")
    # print(data["current"]["temp_c"])
    
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()


    
if __name__ == "__main__":
    city=input("enter city: ")
    get_current_weather(city)     
    # tts(f'in {city} temprature is {get_current_weather(city.lower())}')
    
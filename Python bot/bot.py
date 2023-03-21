import pywhatkit
import datetime, time, os, random, keyboard
import messages, dictionary
import requests, os

path = "../Python bot/Images" #my image path directory

#API
url = "https://ajith-messages.p.rapidapi.com/getMsgs"
querystring = {"category":"Birthday"}

headers = {
    "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "ajith-messages.p.rapidapi.com"
}

now = datetime.datetime.now() #modul to get the current date and time


for key,value in dictionary.phone_book.items(): #.items() return a sequence of tuples
    if key == (str(now.day) + "-" + str(now.month)): # checks if the current date is in the dictionary.phone_book (key)
        for name, phone_number in value.items():
            files = os.listdir(path) # saves a list of all the files in the path directory
            rand = random.choice(files) # choose a random file from files
            file_path = os.path.join(path, rand) # joins path and random file
            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.status_code == 200: # check if the server returned 200 OK, if not, the script will use my own messages
                data = response.json() # to only get message from the response, convert object to json string to python dictionary
                message = data["Message"]  #accessing Message key
                pywhatkit.sendwhats_image(phone_number, file_path, caption= name + ', ' + message)
                time.sleep(20)
            else:
                rand_message = random.choice(messages.message)
                pywhatkit.sendwhats_image(phone_number, file_path, caption= name + rand_message) # modul to send a Whatsapp message, it takes phone number, "image source", and a caption of a photo, which consist of person's name and a random birthday wish
                time.sleep(20) #pauses the program for 20 seconds after sending each message to prevent the program from overwhelming the Whatsapp server or if internet connection is to slow so the message can be send on time. The duration of the pause is adjustable.
        break # break out of the loop after sending messages to all the people whose birthdays are today
    # print(key)
        
keyboard.press_and_release("ctrl+shift+w") #closes all the tabs after finishing the script



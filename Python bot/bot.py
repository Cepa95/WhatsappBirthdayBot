import pywhatkit
import datetime, time, os, random, keyboard


message = [", wishing you a very Happy Birthday filled with love, joy, and wonderful memories that will last a lifetime.", 
           ", Happy Birthday! May your day be filled with laughter, love, and all the things that bring you joy!",
           ", another year, another adventure! Wishing you a very Happy Birthday and a year full of exciting experiences and unforgettable memories!",
           ", today is your day to shine! Happy Birthday, my dear friend! May your day be as bright and beautiful as you are! ",
           ", on this special day, I wish you all the happiness, success, and love in the world! Happy Birthday and may all your dreams come true!",
           ", Happy Birthday to someone who makes the world a better place just by being in it! May your day be filled with all the things that make you smile!",
           ", another year older, another reason to celebrate! Happy Birthday and may this year be even more amazing than the last!",
           ", wishing you a Happy Birthday filled with all the things you love! May your day be as wonderful as you are!",
           ", today is the day you were born and the world became a brighter place! Happy Birthday and may your light shine even brighter this year!",
           ", cheers to another year of life and all the adventures that come with it! Happy Birthday and may your day be full of laughter, love, and lots of cake!",
           ", may your birthday be as wonderful and special as you are! Happy Birthday and here's to another year of making unforgettable memories!"]
path = "../Python bot/Images"


now = datetime.datetime.now()
for key,value in dict.items():
    if key == (str(now.day) + "-" + str(now.month)):
        for name, phone_number in value.items():
            files = os.listdir(path)
            rand = random.choice(files)
            file_path = os.path.join(path, rand)
            rand_message = random.choice(message)
            pywhatkit.sendwhats_image(phone_number, file_path, caption=name + rand_message)
            time.sleep(20)
        break
    # print(key)
        
keyboard.press_and_release("ctrl+shift+w")



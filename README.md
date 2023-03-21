# WhatsappBirthdayBot

A simple WhatsApp bot that sends personalized birthday messages and images to your contacts automatically, so you can ensure that you never miss a special day again. With this bot, you'll be able to streamline your birthday wishes and make sure that each message feels unique and thoughtful. Plus, your friends and family will appreciate the effort you put in to remember their birthdays and make them feel special.

![WhatsappExample](https://user-images.githubusercontent.com/124800316/226494295-73ee108c-aad7-4e36-b6ae-6e1e20c5e75a.JPG)



## Setup
Before you can run the script, you need to make sure that you have the necessary Python packages installed. Specifically, you need to have pywhatkit and keyboard installed.   
Open a terminal window. Make sure that pip is installed in your environment.  

You can do it throught the `requirements.txt` file, which contains all Python packages that you will need to run the script. 
Type the following command to install packages: 

```
pip install -r requirements.txt
```
Wait for the installation to complete. You should see a message indicating that the packages were successfully installed. And that's it.  

Another way to do it:  


Type the following command to install pywhatkit: 
```bash 
pip install pywhatkit 
```
Wait for the installation to complete. You should see a message indicating that the package was successfully installed.  
Type the following command to install keyboard:  
```bash
pip install keyboard  
```
Wait for the installation to complete. You should see a message indicating that the package was successfully installed.  
Once you have installed the required packages, you should be able to run the script without any issues.

Type the following command to install keyboard:  
```bash
pip install requests  
```
Wait for the installation to complete. You should see a message indicating that the package was successfully installed.  
Once you have installed the required packages, you should be able to run the script without any issues. 


## To run a Python script automatically

1.	Open the Task Scheduler by searching for it in the Windows search bar.
2.	Look for the "Create Task" option under "Actions" and click on it.
3.	In the panel that opens up, you can define the name of your task and security options. Make sure to configure them according to your operating system.
4.	Next, go to the "Triggers" tab and click on "New". Here, you can set the time when your script should start. Select "Daily" and adjust the time as needed.
5.	Go to the "Actions" tab and click on "New". Add the Python executable file to the "Program/script" field. In the "Add arguments" field, put the name of your Python file with its extension. In "Start in", put the path to the directory where your Python file is located. Click "OK" when you're done.
6.	In the "Conditions" tab, you can adjust the settings to your liking.
7.	Finally, go to the "Settings" tab and adjust the settings as needed.

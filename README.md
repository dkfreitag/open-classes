# open-classes

Python program to automate finding open class sections on the Baruch College CUNYfirst Student Center.

**Purpose:** When I enrolled at Baruch College for my master's, I had a hard time finding open seats in the classes I wanted to take my first semester. 100% of the seats were filled in a number of key prerequisite classes! Dismayed but not discouraged, I wrote this Python program to continually poll the CUNYfirst website for open seats in classes I wanted. As soon as a seat opened up, the program sent me a text message alerting me so I could sign up for the course and grab the open seat before it disappeared!

**Results:** I grabbed open seats in two of the classes I wanted using this program.

**Author's note:** I wrote this before actually taking a formal class in Python, so some of the coding style might be a bit unconventional. I don't have a real use for this script now, so I haven't been motivated to clean it up, but I'm still posting the code here for posterity.

**How it works:** this script uses **webdriver** to run a headless (no window) instance of Chrome. It also uses the **Twilio SMS API** to send text messages.

To run, you will need to modify the script to:

- Use your login credentials
- Search for sections of the classes you are interested in
- Use your Twilio SMS API credentials (sign up for a free acount here: https://www.twilio.com/docs/sms/api)
- Just use the start_script.sh shell script to run the program. The shell script restarts the program if it crashes due to anything unusual happening (e.g. the CUNYfirst page not loading properly).

### Making changes to main.py
- Adjust the the find_open_classes() function arguments to be whatever class you are looking for. Call the function multiple times if you are looking for multiple classes.

### Making changes to open_classes.py
Login:

- Add your username and password in the appropriate places noted in login_to_CUNYfirst().

Twilio API: define the following variables in send_text_message():

- account_sid
- auth_token
- from_
- to

**Note:** open_classes.py also includes commented out code for an earlier version of the script that used opentextingonline.com to send text messages instead of the Twilio API.

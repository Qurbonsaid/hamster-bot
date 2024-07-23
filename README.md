# Hamster-bot

Requirements:
  - Python installed
  - Chrome installed

How to use:
  - Install the requirements
    ```bash
    pip3 install -r requirements.txt
    ```
  - Edit the `config.py` file with your credentials from https://my.telegram.org and leave empty string the SESSION variable.
  - Run the script
    ```bash
    python3 bot.py
    ```
  - Enter your phone number and the code that you received in your phone. If you have 2FA enabled, you will need to enter the password too.
  - Look at your Saved Messages in Telegram and you will see the session string. Copy it and paste it in the `config.py` file.
  - Run the script again
    ```bash
    python3 bot.py
    ```
  - Enjoy!
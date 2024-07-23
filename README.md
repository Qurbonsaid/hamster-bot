# Hamster-bot

Requirements:
  - 1. Python installed
  - 2. Chrome installed

How to use:
  - 1. Install the requirements
    ```bash
    pip3 install -r requirements.txt
    ```
  - 3. Edit the `config.py` file with your credentials from https://my.telegram.org and leave empty string the SESSION variable.
  - 4. Run the script
    ```bash
    python3 bot.py
    ```
  - 5. Enter your phone number and the code that you received in your phone. If you have 2FA enabled, you will need to enter the password too.
  - 6. Look at your Saved Messages in Telegram and you will see the session string. Copy it and paste it in the `config.py` file.
  - 7. Run the script again
    ```bash
    python3 bot.py
    ```
  - 8. Enjoy!
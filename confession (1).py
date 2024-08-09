import time
import sys
from tqdm import tqdm

def animate_text(text, delay=0.05):
    """Function to animate text output."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def confession_message():
    message = (
        "Hi kuya,\n"
        "Just want to express my feelings for you. I don't know if you know na I have a crush on you HAHAHA, it's kinda weird lol.\n"
        "Pero when I saw you before you look so attractive talaga till now naman hehehe.\n"
        "And I hope this confession will stay between us.\n"
        "Goodluck po sa 3rd year life and ang galing mo pong kumanta.\n"
        "Hehehe I'm super shy to say hi to you kanina pero since di naman tayo magka-building and for sure di na kita makikita,\n"
        "kaya I made this confession. I hope that you will become a great teacher in the future, goodluck."
    )

    print("\nHi po...\n")
    for _ in tqdm(range(30), desc="Processing"):
        time.sleep(0.1)  # Simulate processing with a loading bar


    time.sleep(1)
    animate_text(message, delay=0.04)
    print("\n Goodluck po!\n")

# Run the confession program
confession_message()

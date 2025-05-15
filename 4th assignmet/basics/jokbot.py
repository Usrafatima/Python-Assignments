import random


PROMPT = "What do you want? "
SORRY = "Sorry I only tell jokes"


JOKES = [
    "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to art school? Because it had a lot of bytes to express!"
]

def joke_bot():
    user_input = input(PROMPT)
    
    if user_input == "Joke":
        print(random.choice(JOKES))
    else:
        print(SORRY)


joke_bot()

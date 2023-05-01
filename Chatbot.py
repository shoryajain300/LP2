import random

response = {
    "hi": ["Hello", "Aloha! Hope you're having a great day!", "Hello, and a very good morning"],
    "help": ["Hello,how may i help you today?", "Happy to help! what can i do for you?", "At your service! How can i help you?"],
    "bye": ["It was nice to meet you", "Bye!!", "Glad i could be of help.", "Adios, Amigos."],
    "default": ["Didn't quite understand it, could you clarify?", "Hey me no understand, repeat could you?", "Sorry, couldn't understand,try again"]
}


def get_response(intent="hi"):
    if intent in response:
        print(random.choice(response[intent]))
    else:
        print(random.choice(response["default"]))


def main():
    get_response()

    while True:
        intent = input("> ").lower()
        if(intent == "quit"):
            get_response("bye")
            break

        intent = intent.split()[0]
        get_response(intent)


if __name__ == '__main__':
    main()

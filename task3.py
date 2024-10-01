import time

class SimpleChatBot:
    def __init__(self):
        self.reminders = []
    def greet(self):
        print("Hey buddy I am your chat bot. How can I help you?")

    def respond(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return "Hey ,how can i help you"
        elif ("hi"
              "your name") in user_input:
            return "I'm a simple chat bot"
        elif "remind me" in user_input:
            return self.set_reminder(user_input)
        elif "time" in user_input:
            return f"The current time is {time.strftime('%H:%M:%S')}."
        elif "bye" in user_input or "exit" in user_input:
            return "Goodbye! Have a sweet day!"
        else:
            return "I did not get what do you want to sayhell. Can you ask something else?"

    def set_reminder(self, user_input):
        try:
            parts = user_input.split("remind me to ")
            reminder_text = parts[1]
            self.reminders.append(reminder_text)
            return f"Reminder set: {reminder_text}"
        except IndexError:
            return "Please specify what you want to be reminded of."

    def run(self):
        self.greet()
        while True:
            user_input = input("You: ")
            response = self.respond(user_input)
            print(f"Bot: {response}")
            if "bye" in user_input.lower() or "exit" in user_input.lower():
                break

if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.run()
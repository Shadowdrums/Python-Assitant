import os
import subprocess
import re
import csv
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def find_python_files():
    python_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def read_python_file(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
    return file_contents

def run_python_file(file_path):
    subprocess.run(['python', file_path])

def get_response_from_logs(user_input):
    if not os.path.exists('bot_log.csv'):
        with open('bot_log.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['User', 'Bot'])
    
    with open('bot_log.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        matches = []
        for row in reader:
            if row[0] == user_input:
                matches.append(row[1])
        if matches:
            return matches[-1]
    return None

def process_user_input():
    python_files = find_python_files()
    python_file_names = [os.path.basename(file) for file in python_files]

    user_input = input('Enter the number of the file you want to run or type something to get a response: ')
    response = get_response_from_logs(user_input)
    if response:
        speak(response)
        return True

    if user_input.lower() == 'exit':
        speak('Goodbye!')
        return False
    else:
        try:
            index = int(user_input) - 1
            if index >= 0 and index < len(python_files):
                python_file = python_files[index]
                python_file_name = python_file_names[index]
                speak(f'Running {python_file_name}.')
                run_python_file(python_file)
                speak(f'Finished running {python_file_name}.')
            else:
                speak('Invalid selection.')
        except ValueError:
            speak("I'm sorry, I didn't understand. How should I respond to that?")
            response = input("How should I respond to that? ")
            with open('bot_log.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([user_input, response])
            speak("Thanks for letting me know. I'll try to do better next time.")
        else:
            with open('bot_log.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([user_input, f'Ran {python_file_name}'])
        return True

# Create the chat bot
python_files = find_python_files()
python_file_names = [os.path.basename(file) for file in python_files]
speak('Greetings, I am your python assistant. Here are the Python files available to run:')
for i, file_name in enumerate(python_file_names):
    print(f'{i+1}. {file_name}')

while True:
    if not process_user_input():
        break

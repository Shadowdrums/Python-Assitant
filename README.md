#### Python-Assitant
A helpful chat bot for basic learning, it speaks, and it runs python files for you

#### Summary:

This is a Python script for a simple chat bot that helps the user run Python files and provides responses to user input.

The script imports several modules:

os module for interacting with the operating system
subprocess module for running Python files
re module for regular expressions
csv module for reading and writing CSV files
pyttsx3 module for text-to-speech conversion.
The script defines several functions:

speak(text) function uses pyttsx3 to convert text to speech and play it through the computer's speakers.
find_python_files() function uses os.walk() to traverse the current directory and find all files with the .py extension. It returns a list of file paths.
read_python_file(file_path) function opens the specified Python file and returns its contents as a string.
run_python_file(file_path) function runs the specified Python file using the subprocess module.
get_response_from_logs(user_input) function reads the contents of a CSV file called bot_log.csv to check if the specified user input has a corresponding bot response. If a response is found, it returns it. Otherwise, it returns None.
process_user_input() function is the main function for processing user input. It calls the find_python_files() function to get a list of available Python files, then prompts the user to select a file to run or enter some other input. If the user enters a number corresponding to a valid file, it runs the file using run_python_file(). If the user enters text, it checks get_response_from_logs() to see if there is a pre-defined bot response. If not, it prompts the user to provide a response and writes the user input and response to bot_log.csv. Finally, it returns True to indicate that the chat bot should continue running, or False to indicate that it should exit.
The script also has a main loop that calls process_user_input() repeatedly until the user enters "exit" or the program is terminated.

When the script is run, it first calls find_python_files() to get a list of available Python files, then uses speak() to greet the user and list the available files. The script then enters a loop where it prompts the user for input and processes it using process_user_input(). If the user enters "exit", the script calls speak() to say goodbye and exits the loop. If the user enters a number corresponding to a valid file, the script runs the file and calls speak() to indicate that it has finished. If the user enters text, the script checks get_response_from_logs() to see if there is a pre-defined bot response. If not, it prompts the user to provide a response and writes the user input and response to bot_log.csv. Finally, the loop repeats until the user enters "exit" or the program is terminated.

#### Note:

you will need to install pyttsx3:

PS>pip install pyttsx3

#### bot_log.csv

if you choose to use the bot_log.csv it is a small pre trained modual that if you place in the same directory as Python-Assistant, it will has some pre defined conversations.

#### enjoy :)

import sys
from datetime import datetime

def greet(name):
    print(f"Hello, {name}! Welcome to the Docker-powered Python app.")

def add(a, b):
    try:
        result = float(a) + float(b)
        print(f"The sum of {a} and {b} is {result}")
    except ValueError:
        print("Invalid numbers provided.")

def show_time():
    now = datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def help():
    print("""
Usage:
    python app.py greet <name>
    python app.py add <num1> <num2>
    python app.py time
    python app.py help
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        command = sys.argv[1]
        if command == "greet" and len(sys.argv) == 3:
            greet(sys.argv[2])
        elif command == "add" and len(sys.argv) == 4:
            add(sys.argv[2], sys.argv[3])
        elif command == "time":
            show_time()
        else:
            help()

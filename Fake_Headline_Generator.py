import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Headline storage
headline_history = []

# Categories
subjects = {
    "sports": [
        "Virat Kohli", "Rohit Sharma", "A confused umpire", "A retired cricketer"
    ],
    "politics": [
        "Prime Minister Modi", "Nirmala Sitharaman", "Rahul Gandhi", "A political analyst"
    ],
    "dance": [
        "Shahrukh Khan", "A Bollywood choreographer", "A dancing peacock", "A flash mob dancer"
    ],
    "random": [
        "A Mumbai cat", "A group of monkeys", "Auto rickshaw driver from Delhi", "A tea stall vendor"
    ]
}

actions = {
    "sports": [
        "scores century against", "gets bowled over by", "celebrates with", "challenges"
    ],
    "politics": [
        "declares war on", "debates fiercely with", "tweets angrily about", "orders"
    ],
    "dance": [
        "performs bhangra with", "joins flash mob at", "dances with", "choreographs"
    ],
    "random": [
        "eats", "launches", "cancels", "celebrates"
    ]
}

places_or_things = {
    "sports": [
        "during IPL match", "in cricket stadium", "at India Gate", "on national television"
    ],
    "politics": [
        "inside Parliament", "at election rally", "on Twitter", "in front of media"
    ],
    "dance": [
        "on dance reality show", "at Ganga Ghat", "in Mumbai local train", "at Red Fort"
    ],
    "random": [
        "a plate of samosa", "at tea stall", "at Ganga Ghat", "in Mumbai local train"
    ]
}

emojis = ["😂", "🤣", "😳", "🤯", "😎", "🙈"]

# Generate headline
def generate_headline():
    category = category_var.get()
    if category not in subjects:
        messagebox.showerror("Error", "Please select a valid category.")
        return

    subject = random.choice(subjects[category])
    action = random.choice(actions[category])
    place_or_thing = random.choice(places_or_things[category])
    emoji = random.choice(emojis)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    headline = f"{emoji} [{timestamp}] BREAKING NEWS: {subject} {action} {place_or_thing}"
    headline_history.append(headline)

    # Display
    headline_label.config(text=headline)

    # Speak
    engine.say(headline)
    engine.runAndWait()

    # Save to file
    with open("funny_headlines.txt", "a", encoding="utf-8") as file:
        file.write(headline + "\n")

# Show history
def show_history():
    if not headline_history:
        messagebox.showinfo("History", "No headlines generated yet.")
    else:
        history_text = "\n\n".join(headline_history)
        messagebox.showinfo("Headline History", history_text)

# GUI Setup
root = tk.Tk()
root.title("Fake News Headline Generator")
root.geometry("600x400")
root.config(bg="#f0f0f0")

# Category selection
tk.Label(root, text="Select Category:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
category_var = tk.StringVar(value="random")
category_menu = tk.OptionMenu(root, category_var, *subjects.keys())
category_menu.pack()

# Headline display
headline_label = tk.Label(root, text="", wraplength=500, font=("Arial", 12), bg="#f0f0f0", fg="blue")
headline_label.pack(pady=20)

# Buttons
tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Show History", command=show_history, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=5)

root.mainloop()

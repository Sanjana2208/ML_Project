# Fake Headline Generator ?? 



python
import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pyttsx3
Explanation:

random: Allows you to randomly select items from lists (used to create unpredictable headlines).

tkinter: Python’s built-in GUI library for creating windows, buttons, labels, etc.

messagebox: A submodule of tkinter used to show pop-up messages like errors or information.

datetime: Used to get the current date and time, which is added to each headline.

pyttsx3: A text-to-speech library that lets Python speak the generated headline aloud.


🔊 2. Initialize Text-to-Speech Engine
python
engine = pyttsx3.init()
Explanation:

Initializes the text-to-speech engine and stores it in the variable engine.

This engine will be used later to speak the headline aloud.



🗂 3. Headline History Storage
python
headline_history = []
Explanation:

Creates an empty list called headline_history.

Every time a headline is generated, it gets added to this list so the user can view all past headlines.



🎭 4. Define Categories and Content
Subjects
python
subjects = {
    "sports": ["Virat Kohli", "Rohit Sharma", "A confused umpire", "A retired cricketer"],
    "politics": ["Prime Minister Modi", "Nirmala Sitharaman", "Rahul Gandhi", "A political analyst"],
    "dance": ["Shahrukh Khan", "A Bollywood choreographer", "A dancing peacock", "A flash mob dancer"],
    "random": ["A Mumbai cat", "A group of monkeys", "Auto rickshaw driver from Delhi", "A tea stall vendor"]
}
Actions
python
actions = {
    "sports": ["scores century against", "gets bowled over by", "celebrates with", "challenges"],
    "politics": ["declares war on", "debates fiercely with", "tweets angrily about", "orders"],
    "dance": ["performs bhangra with", "joins flash mob at", "dances with", "choreographs"],
    "random": ["eats", "launches", "cancels", "celebrates"]
}
Places or Things
python
places_or_things = {
    "sports": ["during IPL match", "in cricket stadium", "at India Gate", "on national television"],
    "politics": ["inside Parliament", "at election rally", "on Twitter", "in front of media"],
    "dance": ["on dance reality show", "at Ganga Ghat", "in Mumbai local train", "at Red Fort"],
    "random": ["a plate of samosa", "at tea stall", "at Ganga Ghat", "in Mumbai local train"]
}
Emojis
python
emojis = ["😂", "🤣", "😳", "🤯", "😎", "🙈"]
Explanation:

These dictionaries store different elements for each category.

When a headline is generated, one item from each dictionary is randomly selected to create a funny sentence.

Emojis are added to make the headline more expressive and entertaining.



📰 5. Headline Generator Function
python
def generate_headline():
Explanation:

This function is called when the user clicks the "Generate Headline" button.

It creates a complete headline using random selections and updates the GUI, speaks the headline, and saves it to a file.

Get Selected Category
python
    category = category_var.get()
Retrieves the selected category from the dropdown menu.

Validate Category
python
    if category not in subjects:
        messagebox.showerror("Error", "Please select a valid category.")
        return
Checks if the selected category is valid.

If not, shows an error message and exits the function.

Random Selections
python
    subject = random.choice(subjects[category])
    action = random.choice(actions[category])
    place_or_thing = random.choice(places_or_things[category])
    emoji = random.choice(emojis)
Randomly selects one item from each relevant list based on the chosen category.

Timestamp
python
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Gets the current date and time in a readable format.

Construct Headline
python
    headline = f"{emoji} [{timestamp}] BREAKING NEWS: {subject} {action} {place_or_thing}"
Combines all selected elements into a formatted headline string.

Save to History
python
    headline_history.append(headline)
Adds the headline to the history list.

Display in GUI
python
    headline_label.config(text=headline)
Updates the label in the GUI to show the new headline.

Speak the Headline
python
    engine.say(headline)
    engine.runAndWait()
Uses the text-to-speech engine to read the headline aloud.

Save to File
python
    with open("funny_headlines.txt", "a", encoding="utf-8") as file:
        file.write(headline + "\n")
Opens (or creates) a file named funny_headlines.txt and appends the headline to it.



📜 6. Show History Function
python
def show_history():
Explanation:

This function is called when the user clicks the "Show History" button.

It displays all previously generated headlines in a pop-up window.

Check if History Exists
python
    if not headline_history:
        messagebox.showinfo("History", "No headlines generated yet.")
If no headlines have been generated, shows a message saying so.

Display History
python
    else:
        history_text = "\n\n".join(headline_history)
        messagebox.showinfo("Headline History", history_text)
Joins all headlines with line breaks and shows them in a message box.



🖼 7. GUI Setup
python
root = tk.Tk()
root.title("Fake News Headline Generator")
root.geometry("600x400")
root.config(bg="#f0f0f0")
Explanation:

Creates the main application window.

Sets the title, size, and background color.



🎛 8. Category Selection
python
tk.Label(root, text="Select Category:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
category_var = tk.StringVar(value="random")
category_menu = tk.OptionMenu(root, category_var, *subjects.keys())
category_menu.pack()
Explanation:

Adds a label and dropdown menu for selecting a category.

category_var stores the selected category value.


🖥 9. Headline Display
python
headline_label = tk.Label(root, text="", wraplength=500, font=("Arial", 12), bg="#f0f0f0", fg="blue")
headline_label.pack(pady=20)
Explanation:

Creates a label to display the generated headline.

wraplength ensures long headlines wrap within the window.



🔘 10. Buttons
python
tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Show History", command=show_history, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=5)
Explanation:

Adds three buttons:

"Generate Headline" triggers the headline creation.

"Show History" displays all past headlines.

"Exit" closes the application.



🏁 11. Start GUI Loop
python
root.mainloop()
Explanation:

Starts the tkinter event loop.

Keeps the window open and responsive to user actions.

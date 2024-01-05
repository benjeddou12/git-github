import tkinter as tk
from tkinter import messagebox
from difflib import SequenceMatcher

def calculate_similarity(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()

def check_for_boycott():
    user_input = entry.get().lower()

    brands = ["l'oreal", "sturbucks", "fanta", "cocacola", "nestle", "danone", "GAP", "kitkat", "monster", "macdonald's",
              "burger king", "garnier", "nescafee", "doritos", "cheetos", "crunch", "carrefour", "sprite", "mars", "sneakers",
              "m and m's", "saida", "milka", "nike", "puma", "amazon", "kfc", "pepsi", "7up", "seven up"]

    boycott_product = "koul w tarrez bih 7nekek"

    max_similarity = 0
    most_similar_product = ""

    # Check if the input matches any brand in the list
    if user_input in brands:
        messagebox.showinfo("Message", "Boycott for Gaza!")

    # Check similarity with brands
    else:
        for brand in brands:
            similarity = calculate_similarity(brand.lower(), user_input)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_product = brand

        # Check similarity with the boycott product
        boycott_similarity = calculate_similarity(boycott_product.lower(), user_input)
        if boycott_similarity > max_similarity:
            most_similar_product = boycott_product

        # Display the result
        if most_similar_product:
            messagebox.showinfo("Message", f"Do you mean: {most_similar_product}? Enter again.")
        else:
            messagebox.showinfo("Message", "koolCreate the main window
root = tk.Tk()
root.title("Brand Checker")

# Create and place the input text field
entry_label = tk.Label(root, text="Enter a brand or product:")
entry_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the button
button = tk.Button(root, text="Check", command=check_for_boycott)
button.pack(pady=10)

# Run the main loop
root.mainloop()

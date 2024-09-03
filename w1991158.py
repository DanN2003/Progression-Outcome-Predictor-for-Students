# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1991158
# Date: 21/11/2023

import os
from graphics import GraphWin, Rectangle, Text, Point

#change file path if needed
def save_to_file(progression_data, filename="progression_data.txt", save_path="C:\\Users\\accou\\OneDrive\\Desktop\\school coursework CODE"):
    file_path = os.path.join(save_path, filename)
    with open(file_path, "w") as file: # Reference - https://www.tutorialspoint.com/python/python_files_io.htm
        for entry in progression_data:
            file.write(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}\n")

def load_from_file(filename="progression_data.txt", load_path="C:\\Users\\accou\\OneDrive\\Desktop\\school coursework CODE"):
    progression_data = []
    file_path = os.path.join(load_path, filename)
    try:
        with open(file_path, "r") as file:
            for line in file:
                components = line.strip().split(" - ")
                category = components[0]
                credits = list(map(int, components[1].split(", ")))
                progression_data.append([category] + credits)
    except FileNotFoundError:
        pass
    return progression_data

    # Display histogram
def create_histogram(data): 
    win = GraphWin("Progression Outcome Histogram", 800, 300) #Reference - https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
    win.setBackground("grey")

    categories = ["Progress", "Trailing", "Module Retriever", "Exclude"]
    bar_width = 120
    total_students = len(data)

    for i, category in enumerate(categories):
        if total_students != 0:
            bar_height = data.count(category) / total_students * 200
        else:
            bar_height = 0

        x1 = i * 200 + 50
        y1 = 250 - bar_height
        x2 = x1 + bar_width # Reference - https://mcsp.wartburg.edu/zelle/python/graphics.py
        y2 = 250

        bar = Rectangle(Point(x1, y1), Point(x2, y2))
        bar.setFill("darkslategray4")
        bar.draw(win)

        label = Text(Point((x1 + x2) / 2, y2 + 20), f"{category}\n{data.count(category)}")
        label.draw(win)

    win.getMouse()
    win.close()

def predict_progression_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        return "Total incorrect"

    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        return "Progress"
    elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0:
        return "Progress (module trailer)"
    elif pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
        return "Progress (module trailer)"
    elif pass_credits == 80 and defer_credits == 40 and fail_credits == 0:
        return "Do not Progress – module retriever"
    elif pass_credits == 80 and defer_credits == 20 and fail_credits == 20:
        return "Module Retriever"
    elif pass_credits == 80 and defer_credits == 0 and fail_credits == 40:
        return "Do not Progress – module retriever"
    elif pass_credits == 60 and defer_credits == 60 and fail_credits == 0:
        return "Do not progress – module retriever"
    elif pass_credits == 60 and defer_credits == 40 and fail_credits == 20:
        return "Do not progress – module retriever"
    elif pass_credits == 60 and defer_credits == 20 and fail_credits == 40:
        return "Do not progress – module retriever"
    elif pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
        return "Do not progress – module retriever"
    elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
        return "Do not progress – module retriever"
    elif pass_credits == 40 and defer_credits == 60 and fail_credits == 20:
        return "Do not progress – module retriever"
    elif pass_credits == 40 and defer_credits == 40 and fail_credits == 40:
        return "Do not progress – module retriever"
    elif pass_credits == 40 and defer_credits == 20 and fail_credits == 60:
        return "Do not progress – module retriever"
    elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80:
        return "Exclude"
    elif pass_credits == 20 and defer_credits == 100 and fail_credits == 0:
        return "Do not progress – module retriever"
    elif pass_credits == 20 and defer_credits == 80 and fail_credits == 20:
        return "Do not progress – module retriever"
    elif pass_credits == 20 and defer_credits == 60 and fail_credits == 40:
        return "Do not progress – module retriever"
    elif pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
        return "Do not progress – module retriever"
    elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
        return "Exclude"
    elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
        return "Exclude"
    elif pass_credits == 0 and defer_credits == 120 and fail_credits == 0:
        return "Do not progress – module retriever"
    elif pass_credits == 0 and defer_credits == 100 and fail_credits == 20:
        return "Do not progress – module retriever"
    elif pass_credits == 0 and defer_credits == 80 and fail_credits == 40:
        return "Do not progress – module retriever"
    elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
        return "Do not progress – module retriever"
    elif pass_credits == 0 and defer_credits == 40 and fail_credits == 80:
        return "Exclude"
    elif pass_credits == 0 and defer_credits == 20 and fail_credits == 100:
        return "Exclude"
    elif pass_credits == 0 and defer_credits == 0 and fail_credits == 120:
        return "Exclude"
    else:
        return "Invalid input"

def get_user_input():
    try:
        pass_credits = int(input("Enter the number of credits at pass: "))
        defer_credits = int(input("Enter the number of credits at defer: "))
        fail_credits = int(input("Enter the number of credits at fail: "))

        if pass_credits not in {0, 20, 40, 60, 80, 100, 120} or \
           defer_credits not in {0, 20, 40, 60, 80, 100, 120} or \
           fail_credits not in {0, 20, 40, 60, 80, 100, 120}:
            raise ValueError("Out of range")

        return pass_credits, defer_credits, fail_credits
    except ValueError as e:
        print(f"Error: {e}")
        return get_user_input()

def main():
    progression_data = load_from_file()

    print("Welcome to the Progression Outcome Predictor!")

    while True:
        pass_credits, defer_credits, fail_credits = get_user_input()

        progression_outcome = predict_progression_outcome(pass_credits, defer_credits, fail_credits)
        print(f"Your predicted progression outcome is: {progression_outcome}")

        progression_data.append([progression_outcome, pass_credits, defer_credits, fail_credits])
        save_to_file(progression_data)

        choice = input("Enter 'y' to input data for another student, 'q' to quit: ")
        if choice.lower() == 'q':
            break

    create_histogram([entry[0] for entry in progression_data])

    # Print the progression data in the specified format
    print("\nProgression Data:")
    for entry in progression_data:
        print(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}")

if __name__ == "__main__":
    main() #Reference - https://www.programiz.com/python-programming/main-function

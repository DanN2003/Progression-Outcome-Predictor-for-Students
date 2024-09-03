This project is a Python-based application designed to predict the progression outcomes of students based on their academic performance. The system takes in the marks of students and categorizes them into different progression outcomes such as "Progress", "Progress - Module Trailer", "Do Not Progress - Module Retriever", and "Exclude". Below is an overview of how the system works:

Project Structure
Progression Data.py: This script contains the main logic for predicting student progression outcomes. It processes input data (marks) and determines the appropriate progression outcome based on predefined rules.

w1991158.py: This script is an additional component of the project, likely used for testing or further analysis related to the progression outcomes. It may include functions or methods that supplement the main progression predictor or handle specific use cases.

How It Works
Input Data: The system takes input in the form of student marks across various modules. The marks are categorized into "Pass", "Defer", and "Fail" credits based on the performance.

Outcome Determination: The core functionality involves analyzing the distribution of these credits to decide on one of the following outcomes:

Progress: The student has met the criteria to advance to the next stage.
Progress - Module Trailer: The student can progress but needs to retake some modules.
Do Not Progress - Module Retriever: The student has not met the criteria to progress and needs to retake several modules.
Exclude: The student’s performance is poor enough to warrant exclusion from the program.
Processing and Display: Once the data is processed, the system outputs the progression outcome for each student. This output could be printed to the console or written to a file for record-keeping.

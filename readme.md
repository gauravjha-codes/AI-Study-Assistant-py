# AI Study Assistant
## Overview
AI Study Assistant is a Python-based desktop application designed to aid students in their study process. Built with customtkinter for the GUI, it integrates with the Gemini AI API for generating study notes, questions, and summaries, and the Dictionary API for word definitions. The app features three main tabs: Study Assistant, Planner, and Dictionary, providing a comprehensive tool for note-taking, study planning, and vocabulary lookup.
Features

## Study Assistant Tab:
Generate detailed notes from input text using Gemini AI.
Create multiple-choice questions based on generated notes.
Summarize notes into concise bullet points.
Export notes, questions, and summaries to a PDF file.


## Planner Tab:
Generate a day-wise study plan based on input topics and durations.
Save and load study plans as JSON files.
Track task completion with toggleable "Done/Undone" status buttons.


## Dictionary Tab:
Look up word definitions, synonyms, and examples using the Dictionary API.
Display results in a clean, readable format.


## Installation

Clone the repository:
```
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```


Install dependencies:
```
pip install -r requirements.txt
```


Obtain a Gemini API key from Google AI Studio and update the GEN_API_KEY variable in the code.
Run the application:
```
python study_assistant.py
```



## Usage

### Study Assistant:
Enter text in the input box and click "Generate Notes" to create detailed notes.
Use "Generate Questions" to create multiple-choice questions from the notes.
Click "Generate Summary" for a concise summary of the notes.
Export all content to a PDF using the "Export To PDF" button.


### Planner:
Input topics and durations (e.g., "Math: 2 hours, Physics: 3 hours") and click "Generate Plan" to create a study schedule.
Toggle task status between "Done" and "Undone".
Save or load plans using the "Save Tasks" and "Load Tasks" buttons.


### Dictionary:
Enter a word and click "Search" to retrieve definitions, synonyms, and examples.



## Screenshots
![image](https://github.com/user-attachments/assets/59e2c03c-de45-45d6-a938-4f1d4c06a984)
![image](https://github.com/user-attachments/assets/e71c0c74-d454-4d78-857c-81e4d8c1b453)
![image](https://github.com/user-attachments/assets/370ed1a9-5ed6-4235-964d-5cb7159227f7)



# Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -m "Add new feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.


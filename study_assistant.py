import customtkinter as ctk
import google.generativeai as genai
from fpdf import FPDF
from tkinter import filedialog, messagebox
import re
from PIL import Image
import json
import requests

GEN_API_KEY = "YOUR_GEMINI_API"
genai.configure(api_key=GEN_API_KEY)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("AI Study Assistant")
root.geometry("1100x700")
root.configure(bg="#0B0B0B") 


tab_view = ctk.CTkTabview(
    root,
    segmented_button_selected_color="#00ADB5",
    segmented_button_unselected_color="#393E46",
    segmented_button_selected_hover_color="#007B8A",
    text_color="#EEEEEE",
    segmented_button_fg_color="#222831",
    corner_radius=15,
)
tab_view.pack(fill="both", expand=True, pady=5)

study_tab = tab_view.add("Study Assistant")
planner_tab = tab_view.add("Planner")
dict_tab = tab_view.add("Dictionary")

def get_word_info_api(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code != 200:
            return f"No information found for '{word}'."

        data = response.json()[0]
        meanings = data.get("meanings", [])
        definitions = []
        synonyms = set()
        examples = []

        for meaning in meanings[:3]:
            part_of_speech = meaning.get("partOfSpeech", "")
            for defn in meaning.get("definitions", []):
                definition = defn.get("definition", "")
                example = defn.get("example", "")
                definitions.append(f"({part_of_speech}) {definition}")
                if example:
                    examples.append(example)
                synonyms.update(defn.get("synonyms", []))

        def_text = "\n".join(definitions) or "No definitions found."
        syn_text = ", ".join(list(synonyms)[:10]) or "No synonyms found."
        ex_text = "\n".join(examples[:3]) or "No examples found."

        return f"Definition:\n{def_text}\n\nSynonyms:\n{syn_text}\n\nExamples:\n{ex_text}"
    except Exception as e:
        return f"Error: {str(e)}"

def search_word():
    word = dict_input.get("1.0", "end-1c").strip()
    if not word:
        messagebox.showwarning("Warning", "Please enter a word to search.")
        return

    result = get_word_info_api(word)

    dict_output.configure(state="normal")
    dict_output.delete("1.0", "end")
    dict_output.insert("1.0", result)
    dict_output.configure(state="disabled")


def addr_placeholder(event):
    if dict_input.get("1.0", "end").strip() == "":
        dict_input.insert("1.0", "Enter a word...")
        dict_input.configure(fg_color="#2A2A2A")

def remover_placeholder(event):
    if dict_input.get("1.0", "end").strip() == "Enter a word...":
        dict_input.delete("1.0", "end")
        dict_input.configure(fg_color="#2C3539")

dict_input = ctk.CTkTextbox(dict_tab, height=100, font=("Lato", 17), corner_radius=15)
dict_input.pack(padx=10, pady=10, fill="both")
dict_input.insert("1.0", "Enter a word...")
dict_input.configure(fg_color="grey", border_width=2, border_color="#00ADB5")
dict_input.bind("<FocusIn>", remover_placeholder)
dict_input.bind("<FocusOut>", addr_placeholder)

ctk.CTkButton(dict_tab, text="🔍 Search", command=search_word, fg_color="#4682B4", corner_radius=15, font=("Lato", 17)).pack(pady=15)


dict_output = ctk.CTkTextbox(dict_tab, height=320, font=("Arial", 16), wrap="word", corner_radius=15)
dict_output.pack(fill="both", expand=True, padx=10, pady=(20, 20))

about_label = ctk.CTkLabel(
    root,
    text="AI Study Assistant\nVersion 1.5\n By Gaurav",
    font=("Lato", 11),
    anchor="e",
    fg_color="transparent",  # Set text color transparent
    bg_color="transparent"   # Set background color transparent
)
about_label.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")



def clean_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"_([^_]*)_", r"\1", text)
    return text.strip()

def generate_content(text, task):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"{task}\n{text}")
        return clean_text(response.text)
    except Exception as e:
        return f"Error: {str(e)}"

def generate_notes():
    input_text = text_input.get("1.0", "end").strip()
    notes_output.delete("1.0", "end")
    notes_output.insert("end", generate_content(input_text, "enerate highly detailed and structured notes. Ensure the notes cover all key points, explanations, diagrams, examples, and contextual information. Break down complex concepts into simple, easy-to-understand sections. Include definitions and bullet points where necessary. Add relevant examples, use cases, and practical applications to enhance understanding. Maintain clarity, conciseness, and logical flow. If the text contains technical terms, provide explanations and possible real-world connections. Ensure the notes are well-organized and formatted for efficient studying. Do not include any concluding statements, learning tips, additional practice advice, or references to external resources. Keep the notes strictly factual and content-focused. Don't give any intro and outro."))

def generate_questions():
    notes_text = notes_output.get("1.0", "end").strip()
    if notes_text:
        questions_output.delete("1.0", "end")
        generated_questions = generate_content(notes_text, "Generate minimum 20 well structured multiple-choice questions and provide answer key in last with only option number not full answer. Don't give any intro and outro.")
        questions_output.insert("1.0", generated_questions)
    else:
        questions_output.insert("1.0", "Please generate notes first before creating questions.")

def generate_summary():
    notes_text = notes_output.get("1.0", "end").strip()
    if notes_text:
        summary_output.delete("1.0", "end")
        summary_output.insert("end", generate_content(notes_text, "Summarize in a clear, concise, and structured manner using bullet points. Capture only the key ideas, main arguments, and important details while eliminating redundant or less significant information. Ensure the summary retains the core meaning of the text while being easy to read and understand. Use short, precise sentences and maintain logical flow. If the text includes data, key figures, or important names, include them in the summary while keeping it brief and to the point. Don't give any intro and outro."))
    else:
        summary_output.insert("end", "Please generate notes first before creating a summary.")

def export_to_pdf():
    notes = notes_output.get("1.0", "end").strip()
    questions = questions_output.get("1.0", "end").strip()
    summary = summary_output.get("1.0", "end").strip()

    if not notes and not questions and not summary:
        messagebox.showwarning("Export Error", "No content to export!")
        return

    pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not pdf_filename:
        return

    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=18)

        if notes:
            pdf.cell(200, 10, "Notes", ln=True, align="L")
            pdf.set_font("Arial", size=14)
            pdf.multi_cell(0, 8, notes + "\n\n")

        if questions:
            pdf.set_font("Arial", style="B", size=18)
            pdf.cell(200, 10, "Questions", ln=True, align="L")
            pdf.set_font("Arial", size=14)
            pdf.multi_cell(0, 8, questions + "\n\n")

        if summary:
            pdf.set_font("Arial", style="B", size=18)
            pdf.cell(200, 10, "Summary", ln=True, align="L")
            pdf.set_font("Arial", size=14)
            pdf.multi_cell(0, 8, summary + "\n\n")

        pdf.output(pdf_filename, 'F')
        messagebox.showinfo("Success", f"PDF saved successfully!\n{pdf_filename}")

    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to save PDF: {str(e)}")

def add_placeholder(event):
    if text_input.get("1.0", "end").strip() == "":
        text_input.insert("1.0", "Enter your text here...")
        text_input.configure(fg_color="#2A2A2A")

def remove_placeholder(event):
    if text_input.get("1.0", "end").strip() == "Enter your text here...":
        text_input.delete("1.0", "end")
        text_input.configure(fg_color="#2C3539")

text_input = ctk.CTkTextbox(study_tab, height=100, font=("Arial", 18), corner_radius=15)
text_input.pack(padx=10, pady=10, fill="both")
text_input.insert("1.0", "Enter your text here...")
text_input.configure(fg_color="grey", border_width=2, border_color="#00ADB5")
text_input.bind("<FocusIn>", remove_placeholder)
text_input.bind("<FocusOut>", add_placeholder)


button_frame = ctk.CTkFrame(study_tab, fg_color="transparent")
button_frame.pack(pady=5)

ctk.CTkButton(button_frame, text="Generate Notes", command=generate_notes, fg_color="#4682B4", corner_radius=15, hover_color="#2a3439", font=("Lato", 17)).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkButton(button_frame, text="Generate Questions", command=generate_questions, fg_color="#4682B4", corner_radius=15, hover_color="#2a3439", font=("Lato", 17)).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkButton(button_frame, text="Generate Summary", command=generate_summary, fg_color="#4682B4", corner_radius=15, hover_color="#2a3439", font=("Lato", 17)).grid(row=0, column=2, padx=10, pady=5)

output_frame = ctk.CTkFrame(study_tab)
output_frame.pack(pady=10, padx=10, fill="both", expand=True)

#original_img = Image.open("backgroung _up.jpg")

#def resize_bg(event):
    #resized_img = original_img.resize((event.width, event.height), Image.Resampling.LANCZOS)
    #bg_ctk_img = ctk.CTkImage(light_image=resized_img, size=(event.width, event.height))
    #bg_label.configure(image=bg_ctk_img)
    #bg_label.image = bg_ctk_img

bg_label = ctk.CTkLabel(output_frame, text="")
bg_label.place(relwidth=1, relheight=1)
output_frame.bind("<Configure>")

output_frame.columnconfigure((0, 1, 2), weight=1)
output_frame.rowconfigure(1, weight=1)

ctk.CTkLabel(output_frame, text="Notes", font=("Lato", 18, "bold")).grid(row=0, column=0, padx=10, pady=5)
notes_output = ctk.CTkTextbox(output_frame, font=("Lato", 18), corner_radius=15)
notes_output.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

ctk.CTkLabel(output_frame, text="Questions", font=("Lato", 18, "bold")).grid(row=0, column=1, padx=10, pady=5)
questions_output = ctk.CTkTextbox(output_frame, font=("Lato", 18), corner_radius=15)
questions_output.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

ctk.CTkLabel(output_frame, text="Summary", font=("Lato", 18, "bold")).grid(row=0, column=2, padx=10, pady=5)
summary_output = ctk.CTkTextbox(output_frame, font=("Lato", 18), corner_radius=15)
summary_output.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

btn_frame = ctk.CTkFrame(study_tab, fg_color="transparent")
btn_frame.pack(pady=10)
ctk.CTkButton(btn_frame, text="Export To PDF", command=export_to_pdf, fg_color="#dd4444", corner_radius=10, hover_color="#2a3439", font=("Lato", 18)).grid(row=0, column=0, padx=10)


planner_widgets = []

#ctk.CTkLabel(planner_tab, text="Enter Subjects & Duration", font=("Lato", 18, "bold")).pack()

def addrr_placeholder(event):
    if study_input.get("1.0", "end").strip() == "":
        study_input.insert("1.0", "Enter topic and duration...")
        study_input.configure(fg_color="#2A2A2A")

def removerr_placeholder(event):
    if study_input.get("1.0", "end").strip() == "Enter topic and duration...":
        study_input.delete("1.0", "end")
        study_input.configure(fg_color="#2C3539")

study_input = ctk.CTkTextbox(planner_tab, height=100, font=("Lato", 17), corner_radius=15)
study_input.pack(padx=10, pady=10, fill="both")
study_input.insert("1.0", "Enter topic and duration...")
study_input.configure(fg_color="grey", border_width=2, border_color="#00ADB5")
study_input.bind("<FocusIn>", removerr_placeholder)
study_input.bind("<FocusOut>", addrr_placeholder)



planner_btn_frame = ctk.CTkFrame(planner_tab, fg_color="transparent")
planner_btn_frame.pack(pady=10)

ctk.CTkButton(planner_btn_frame, text="Generate Plan", command=lambda: generate_study_plan(), fg_color="#4682B4", hover_color="#2a3439", font=("Lato", 17), corner_radius=15).pack(side="left", padx=10)
ctk.CTkButton(planner_btn_frame, text="💾 Save Tasks", command=lambda: save_tasks(), fg_color="#4682B4", hover_color="#2a3439", font=("Lato", 17), corner_radius=15).pack(side="left", padx=10)
ctk.CTkButton(planner_btn_frame, text="📂 Load Tasks", command=lambda: load_tasks(), fg_color="#4682B4", hover_color="#2a3439", font=("Lato", 17), corner_radius=15).pack(side="left", padx=10)

task_frame_wrapper = ctk.CTkFrame(planner_tab, fg_color="#2b2b2b", corner_radius=15)
task_frame_wrapper.pack(fill="both", expand=True, padx=10, pady=(0, 20))

task_title = ctk.CTkLabel(task_frame_wrapper, text="Generated Tasks", font=("Lato", 18, "bold"), anchor="center", corner_radius=15)
task_title.pack(padx=10, pady=(10, 0), anchor="center")

task_scroll_frame = ctk.CTkScrollableFrame(task_frame_wrapper, height=350, fg_color="#1e1e1e", corner_radius=15)
task_scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

task_container = task_scroll_frame

def display_tasks(tasks):
    clear_tasks_ui()
    for task_item in tasks:
        if isinstance(task_item, str):
            task_text = task_item
            status = "Undone"
        else:
            task_text, status = task_item["task"], task_item["status"]

        frame = ctk.CTkFrame(task_container, fg_color="#1f1f1f")
        frame.pack(fill="x", pady=2, padx=5)

        task_label = ctk.CTkLabel(frame, text=task_text, font=("Lato", 17), wraplength=500, anchor="w")
        task_label.pack(side="left", padx=10, pady=5, expand=True)

        status_btn = ctk.CTkButton(frame, width=100)
        status_btn.pack(side="right", padx=10)
        make_toggle_button(status_btn, status)

        planner_widgets.append({"label": task_label, "button": status_btn})

def toggle_status(button):
    current = button.cget("text")
    if current == "Undone":
        button.configure(text="Done", fg_color="#228B22", hover_color="#1e6820", corner_radius=15)
    else:
        button.configure(text="Undone", fg_color="#8B0000", hover_color="#5A0000", corner_radius=15)

def make_toggle_button(btn, stat):
    btn.configure(
        command=lambda: toggle_status(btn),
        text=stat,
        fg_color="#228B22" if stat == "Done" else "#8B0000",
        hover_color="#1e6820" if stat == "Done" else "#5A0000",
        corner_radius=15
    )

def clear_tasks_ui():
    for widget in task_container.winfo_children():
        widget.destroy()
    planner_widgets.clear()

def generate_study_plan():
    input_text = study_input.get("1.0", "end").strip()
    clear_tasks_ui()
    if input_text:
        #plan = generate_content(input_text, "Generate a day-wise study plan for the following subjects and time durations. Divide the available time efficiently across the days based on #subject difficulty and coverage needs. Do not include any additional explanation, notes and tips — only provide the plan in a clear and day-wise format.")
        plan = generate_content(input_text, "Generate a day-wise and numeric order task-wise like 1, study plan for the following topic spanning mentioned days, Divide the available time efficiently across the days based on subject difficulty and coverage needs, Output ONLY the study plan with no additional explanations, introductions, conclusions, notes, or tips.")
        tasks = [line.strip() for line in plan.split("\n") if line.strip()]
        display_tasks(tasks)
    else:
        messagebox.showwarning("Input Missing", "Please enter some subject/topic and duration.")

def save_tasks():
    if not planner_widgets:
        messagebox.showwarning("Nothing to Save", "No tasks to save!")
        return
    task_list = []
    for widget in planner_widgets:
        task_text = widget["label"].cget("text")
        status = widget["button"].cget("text")
        task_list.append({"task": task_text, "status": status})

    filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, "w") as f:
                json.dump(task_list, f, indent=4)
            messagebox.showinfo("Success", "Tasks saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

def load_tasks():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, "r") as f:
                loaded_tasks = json.load(f)
            display_tasks(loaded_tasks)
            messagebox.showinfo("Loaded", "Tasks loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()

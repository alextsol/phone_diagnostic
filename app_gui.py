# app_gui.py
import tkinter as tk
from tkinter import messagebox
from diagnostic_logic import guess_diagnosis, diagnoses, check_symptoms


class DiagnosticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Diagnostic Tool")
        self.root.geometry("640x320")

        # User input frame
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.input_frame, width=50)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Phone Model:").grid(row=1, column=0)
        self.phone_model_entry = tk.Entry(self.input_frame, width=50)
        self.phone_model_entry.grid(row=1, column=1)

        self.next_button = tk.Button(self.input_frame, text="Next", command=self.start_diagnosis)
        self.next_button.grid(row=2, column=0, columnspan=2)

        # Symptom question frame
        self.question_frame = tk.Frame(root)
        
        # Display info frame
        self.display_info_frame = tk.Frame(root)

        # Answer buttons frame
        self.answer_frame = tk.Frame(root)

        self.yes_button = tk.Button(self.answer_frame, text="Yes", command=lambda: self.record_response(True))
        self.no_button = tk.Button(self.answer_frame, text="No", command=lambda: self.record_response(False))

        self.diagnosis_label = tk.Label(root, text="", font=("Helvetica", 16), fg="red")

        self.symptoms_iter = iter(diagnoses.items())
        self.symptom_responses = {}

    def start_diagnosis(self):
        self.name_entry.grid_remove()
        self.phone_model_entry.grid_remove()
        self.next_button.grid_remove()

        # Display user info
        tk.Label(self.display_info_frame, text="Name:").grid(row=0, column=0, sticky="w")
        tk.Label(self.display_info_frame, text=self.name_entry.get()).grid(row=0, column=1, sticky="w")
        tk.Label(self.display_info_frame, text="Phone Model:").grid(row=1, column=0, sticky="w")
        tk.Label(self.display_info_frame, text=self.phone_model_entry.get()).grid(row=1, column=1, sticky="w")
        self.display_info_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Setup question frame
        self.question_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.symptom_label = tk.Label(self.question_frame, text="", font=("Helvetica", 16), wraplength=600)
        self.symptom_label.pack(side="top", fill="x")

        # Setup answer frame
        self.answer_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Configure columns for central alignment of buttons
        self.answer_frame.columnconfigure(0, weight=1)
        self.answer_frame.columnconfigure(1, weight=1)
        self.answer_frame.columnconfigure(2, weight=1)
    
        # Place buttons in central columns
        self.yes_button.grid(row=0, column=1)
        self.no_button.grid(row=0, column=2)

        self.diagnosis_label.grid(row=4, column=0, columnspan=2)

        self.ask_next_symptom()

    def ask_next_symptom(self):
        try:
            self.current_diagnosis, self.current_symptoms = next(self.symptoms_iter)
            self.symptom_label.config(text=f"Does your phone have the symptom: {self.current_symptoms[0]}?")
            # Display 'Yes' and 'No' buttons
            self.yes_button.grid(row=4, column=0)
            self.no_button.grid(row=4, column=1)
        except StopIteration:
            self.show_diagnosis()

    def record_response(self, response):
        symptom = self.current_symptoms.pop(0)
        self.symptom_responses[symptom] = response

        if not self.current_symptoms:
            if check_symptoms(self.symptom_responses, self.current_diagnosis):
                self.show_diagnosis()
                return
            self.symptom_responses = {}
            self.current_diagnosis, self.current_symptoms = next(self.symptoms_iter, (None, None))
            if self.current_diagnosis is None:
                self.show_diagnosis()
            else:
                self.ask_next_symptom()
        else:
            self.symptom_label.config(text=f"Does your phone have the symptom: {self.current_symptoms[0]}?")

    def show_diagnosis(self):
        # Use a pop-up message box for the final diagnosis
        final_diagnosis = guess_diagnosis(self.symptom_responses)
        messagebox.showinfo("Final Diagnosis", final_diagnosis)

        # Clean up for next diagnosis or exit
        self.display_info_frame.grid_remove()
        self.answer_frame.grid_remove()
        self.diagnosis_label.grid_remove()
        # Reset the iterator and responses for the next use
        self.symptoms_iter = iter(diagnoses.items())
        self.symptom_responses = {}

def run_app():
    root = tk.Tk()
    app = DiagnosticApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
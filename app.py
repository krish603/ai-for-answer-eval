import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF for PDF text extraction
from sentence_transformers import SentenceTransformer, util
import os

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text.strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text: {str(e)}")
        return ""

def calculate_similarity(student_text, model_text):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode([student_text, model_text], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    return round(similarity * 10, 2)  # Convert similarity score to marks out of 10

def upload_student_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        student_text.set(extract_text_from_pdf(file_path))

def upload_model_answer():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        model_text.set(extract_text_from_pdf(file_path))

def evaluate_assignment():
    student_answer = student_text.get()
    model_answer = model_text.get()
    if not student_answer or not model_answer:
        messagebox.showwarning("Warning", "Please upload both student assignment and model answer.")
        return
    score = calculate_similarity(student_answer, model_answer)
    result_var.set(f"Marks: {score}/10")

def generate_report():
    report_path = "evaluation_report.txt"
    with open(report_path, "w") as f:
        f.write(f"Student Marks: {result_var.get()}\n")
    messagebox.showinfo("Success", f"Report saved at {os.path.abspath(report_path)}")

# GUI Setup
root = tk.Tk()
root.title("AI-Based Answer Evaluation System")
root.geometry("500x400")

student_text = tk.StringVar()
model_text = tk.StringVar()
result_var = tk.StringVar()

tk.Label(root, text="Upload Student Assignment (PDF)").pack()
tk.Button(root, text="Upload", command=upload_student_pdf).pack()

tk.Label(root, text="Upload Model Answer (PDF)").pack()
tk.Button(root, text="Upload", command=upload_model_answer).pack()

tk.Button(root, text="Evaluate", command=evaluate_assignment).pack()
tk.Label(root, textvariable=result_var, font=("Arial", 12)).pack()

tk.Button(root, text="Generate Report", command=generate_report).pack()

root.mainloop()
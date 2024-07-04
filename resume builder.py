import tkinter as tk
from tkinter import messagebox, filedialog

class ResumeBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")
        self.root.geometry("600x500")

        # Create and organize GUI components
        self.create_widgets()

    def create_widgets(self):
        # Name
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Contact Information
        self.contact_label = tk.Label(self.root, text="Contact Information:")
        self.contact_label.grid(row=1, column=0, padx=10, pady=5)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Education
        self.education_label = tk.Label(self.root, text="Education:")
        self.education_label.grid(row=2, column=0, padx=10, pady=5)
        self.education_text = tk.Text(self.root, height=5, width=40)
        self.education_text.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Work Experience
        self.experience_label = tk.Label(self.root, text="Work Experience:")
        self.experience_label.grid(row=3, column=0, padx=10, pady=5)
        self.experience_text = tk.Text(self.root, height=5, width=40)
        self.experience_text.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Skills
        self.skills_label = tk.Label(self.root, text="Skills:")
        self.skills_label.grid(row=4, column=0, padx=10, pady=5)
        self.skills_text = tk.Text(self.root, height=5, width=40)
        self.skills_text.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Save and Clear Buttons
        self.save_button = tk.Button(self.root, text="Save Resume", command=self.save_resume)
        self.save_button.grid(row=5, column=0, padx=10, pady=5)
        self.clear_button = tk.Button(self.root, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=5, column=1, padx=10, pady=5)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.grid(row=5, column=2, padx=10, pady=5)

    def save_resume(self):
        # Save resume data to a text file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(f"Name: {self.name_entry.get()}\n")
                file.write(f"Contact Information: {self.contact_entry.get()}\n\n")
                file.write(f"Education:\n{self.education_text.get('1.0', 'end')}\n\n")
                file.write(f"Work Experience:\n{self.experience_text.get('1.0', 'end')}\n\n")
                file.write(f"Skills:\n{self.skills_text.get('1.0', 'end')}")
            messagebox.showinfo("Save Resume", "Resume saved successfully!")

    def clear_fields(self):
        # Clear all input fields
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.education_text.delete('1.0', tk.END)
        self.experience_text.delete('1.0', tk.END)
        self.skills_text.delete('1.0', tk.END)
        messagebox.showinfo("Clear Fields", "Fields cleared successfully!")

    def exit_application(self):
        # Exit the application
        if messagebox.askyesno("Exit Application", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilderApp(root)
    root.mainloop()

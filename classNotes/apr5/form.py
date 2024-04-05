import tkinter as tk
from tkinter import messagebox

class SimpleForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Height Calculator")

        tk.Label(self, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Height (in ft):").grid(row=1, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)


        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def submit_form(self):
        name = self.name_entry.get()
        height = self.height_entry.get()

        if name.strip() == "" or height.strip() == "":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showinfo("Submission Successful", f"{name} is {height} ft tall")


if __name__ == "__main__":
    app = SimpleForm()
    app.mainloop()

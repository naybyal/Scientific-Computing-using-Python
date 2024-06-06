import tkinter as tk

def calculate():
    try:
        value = float(meter_entry.get())
        feet_label.config(text=f"{round(value * 3.28084, 2)} feet")
    except ValueError:
        pass

root = tk.Tk()
root.title("Meters to Feet")

meter_label = tk.Label(root, text="Meters:")
meter_label.pack()

meter_entry = tk.Entry(root)
meter_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

feet_label = tk.Label(root, text="")
feet_label.pack()

root.mainloop()

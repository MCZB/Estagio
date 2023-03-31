import tkinter as tk

def reverse_string(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str

def on_click():
    string = entry.get()
    reversed_str = reverse_string(string)
    label.config(text=reversed_str)

root = tk.Tk()
root.title("Inverter String")

frame = tk.Frame(root)
frame.pack(padx=30, pady=30)

label = tk.Label(frame, text="")
label.pack(pady=10)

entry = tk.Entry(frame)
entry.pack(pady=10)

button = tk.Button(frame, text="Inverter", command=on_click)
button.pack()

root.mainloop()

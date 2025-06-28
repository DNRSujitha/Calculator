import tkinter as tk

reset_next = False  # Flag to clear entry on next input

def click(event):
    global reset_next
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            reset_next = True
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            reset_next = True
    elif text == "C":
        entry.delete(0, tk.END)
        reset_next = False
    else:
        if reset_next:
            entry.delete(0, tk.END)
            reset_next = False
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="#2E2E2E")

# Entry widget for display
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.FLAT,
                 bg="#1C1C1C", fg="white", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Button creation
for row in buttons:
    frame = tk.Frame(root, bg="#2E2E2E")
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", fg="white", bg="#3E3E3E",
                      activebackground="#4E4E4E", borderwidth=0, relief=tk.FLAT)
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        b.bind("<Button-1>", click)

root.mainloop()

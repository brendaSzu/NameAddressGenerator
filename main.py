import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_entries():
    text_display.delete('1.0', tk.END)
    count = int(quantity_var.get())

    for _ in range(count):
        entry = f"{fake.name()}\n{fake.address()}\n\n"
        text_display.insert(tk.END, entry + ("-"*30) + "\n\n")
    
def save_to_file():
    # Get the current content of the text box
    content = text_display.get('1.0', tk.END).strip()
    
    if not content:
        messagebox.showwarning("Empty", "Generate some names first!")
        return
    
    # Open a "Save As" dialog box
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        initialfile="Practice_Names.txt"
    )

    if file_path:
        with open(file_path, 'w') as f:
            f.write(content)
        messagebox.showinfo("Success", f"Saved to: {file_path}")
        
# Main Window
root = tk.Tk()
root.title("Calligraphy Practice Name and Address Generator")
root.geometry("500x700")

# Header
tk.Label(root, text="Practice Entry Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Controls Frame
ctrl_frame = tk.Frame(root)
ctrl_frame.pack(pady=10)

tk.Label(ctrl_frame, text ="Count:").grid(row=0, column=0, padx=5)
quantity_var = tk.StringVar(value="5")
tk.Spinbox(ctrl_frame, from_=1, to=50, textvariable=quantity_var, width=5).grid(row=0, column=1, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Generate", command=generate_entries, bg="#2ecc71", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Save to File", command=save_to_file, bg="#3498db", fg="white", width=10).pack(side=tk.LEFT, padx=5)

# Scrollable Results
text_display = tk.Text(root, height=25, width=55, font=("Courier", 10))
text_display.pack(pady=10, padx=10)

root.mainloop()

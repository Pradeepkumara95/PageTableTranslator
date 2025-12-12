# EEX5564 - Computer Architecture and Operating Systems 
# Mini Project 2024-25 
# Group A 
# Page Table Translator 
# Name: M.P.Pushpa Kumara
# Reg No: 422514886
# s No: s18003202

#--------------------Page Table Translator--------------------
import tkinter as tk
from tkinter import messagebox

# ---------- Translation Logic ----------
def translate_address(logical_address, page_size, page_table):
    page_number = logical_address // page_size
    offset = logical_address % page_size

    if page_number >= len(page_table):
        return (
            logical_address, page_number, offset, "-", "-",
            "Page Fault: Page number outside logical range"
        )

    frame = page_table[page_number]

    if frame == -1:
        return (
            logical_address, page_number, offset, "-", "-",
            "Page Fault Occurred"
        )

    physical_address = frame * page_size + offset
    return (logical_address, page_number, offset, frame, physical_address, "OK")


# ---------- GUI Logic ----------

# Global list for page table entries
page_table_entries = []

def generate_page_mapping_inputs(event=None):
    for widget in mapping_frame.winfo_children():
        if widget != mapping_title_label:
            widget.destroy()

    try:
        num_pages = int(pages_var.get())
        if not (1 <= num_pages <= 8):
            return
    except ValueError:
        return

    global page_table_entries
    page_table_entries = []

    for i in range(num_pages):
        row = i // 2 + 1  # two columns
        col = (i % 2) * 2
        tk.Label(mapping_frame, text=f"Page {i}:", anchor="w", bg="#d4f0e0").grid(row=row, column=col, sticky="w", padx=5, pady=2)
        entry = tk.Entry(mapping_frame, width=10, bg="#f0fff0")
        entry.grid(row=row, column=col + 1, pady=2, padx=5)
        page_table_entries.append(entry)


def run_translation():
    # Validate Page Size
    try:
        page_size = int(page_size_var.get())
        if page_size not in (512, 1024):
            messagebox.showerror("Error", "Page size must 512 or 1024.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid page size.")
        return

    # Validate Number of Pages
    try:
        num_pages = int(pages_var.get())
        if not (1 <= num_pages <= 8):
            messagebox.showerror("Error", "Pages must be 1–8.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid number of pages.")
        return

    # Validate Number of Frames
    try:
        num_frames = int(frames_var.get())
        if not (4 <= num_frames <= 6):
            messagebox.showerror("Error", "Frames must be 4–6.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid frame count.")
        return

    # Read page table frames
    page_table = []
    for e in page_table_entries:
        val = e.get().strip()
        if val == "":
            v = -1  # default page fault
        else:
            try:
                v = int(val)
            except ValueError:
                messagebox.showerror("Error", "Invalid page mapping.")
                return

        if v not in range(num_frames) and v != -1:
            messagebox.showerror("Error", f"Frames must be between 0–{num_frames-1} or -1.")
            return

        page_table.append(v)

    # Read logical addresses
    logical_addresses = []
    for box in logical_input_boxes:
        val = box.get().strip()
        if val != "":
            try:
                logical_addresses.append(int(val))
            except ValueError:
                messagebox.showerror("Error", "Invalid logical address.")
                return

    if len(logical_addresses) == 0:
        messagebox.showerror("Error", "Enter at least 1 logical address.")
        return

    # Clear output
    output_box.delete(1.0, tk.END)

    # Perform translation
    for addr in logical_addresses:
        result = translate_address(addr, page_size, page_table)
        text = (
            f"Logical Address : {result[0]}\n"
            f"Page Number     : {result[1]}\n"
            f"Offset          : {result[2]}\n"
            f"Frame Number    : {result[3]}\n"
            f"Physical Address: {result[4]}\n"
            f"Status          : {result[5]}\n"
            f"{'-'*40}\n"
        )
        output_box.insert(tk.END, text)


# ---------- GUI — MAIN WINDOW ----------

root = tk.Tk()
root.title("Page Table Translator")
root.geometry("1000x650")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="PAGE TABLE TRANSLATOR", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

copyright_label = tk.Label(root, text="OUSL-EEX5563-Computer Architecture and Operating Systems - Mini Project 2024-25. By M.P. Pushpa Kumara_422514886.",
                           font=("Arial", 10), bg="#f0f0f0", fg="gray")
copyright_label.pack(side="bottom", pady=5)

# MAIN FRAME
main_frame = tk.Frame(root, bg="#f7e6f0")
main_frame.pack(pady=5, fill="both", expand=True)

# Left Frame Scrollable
input_frame = tk.Frame(main_frame, bg="#e0f7fa")
input_frame.pack(side="left", fill="y", padx=10)

# Input Data Title
input_title_label = tk.Label(input_frame, text="INPUT DATA", font=("Arial", 14, "bold"), bg="#c8f7d6")
input_title_label.pack(fill="x", pady=5)

canvas = tk.Canvas(input_frame, width=450, height=550, bg="#e0f7fa")
scrollbar = tk.Scrollbar(input_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#e0f7fa")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left")
scrollbar.pack(side="right", fill="y")

# Input Fields
tk.Label(scrollable_frame, text="Page Size (512 or 1024):", bg="#e0f7fa").grid(row=0, column=0, sticky="w", padx=10, pady=5)
page_size_var = tk.Entry(scrollable_frame, width=12, bg="#f0fff0")
page_size_var.grid(row=0, column=1, pady=5)

tk.Label(scrollable_frame, text="Number of Pages (1–8):", bg="#e0f7fa").grid(row=1, column=0, sticky="w", padx=10, pady=5)
pages_var = tk.Entry(scrollable_frame, width=12, bg="#f0fff0")
pages_var.grid(row=1, column=1, pady=5)
pages_var.bind("<KeyRelease>", generate_page_mapping_inputs)

tk.Label(scrollable_frame, text="Physical Frames (4–6):", bg="#e0f7fa").grid(row=2, column=0, sticky="w", padx=10, pady=5)
frames_var = tk.Entry(scrollable_frame, width=12, bg="#f0fff0")
frames_var.grid(row=2, column=1, pady=5)

# Page Mapping Frame
mapping_frame = tk.Frame(scrollable_frame, bd=1, relief="solid", padx=10, pady=10, bg="#d4f0e0")
mapping_frame.grid(row=3, column=0, columnspan=4, pady=10, padx=10, sticky="w")

mapping_title_label = tk.Label(mapping_frame, text="PAGE to FRAME Mapping", font=("Arial", 12, "bold"), bg="#d4f0e0")
mapping_title_label.grid(row=0, column=0, columnspan=4, pady=3, sticky="ew")

# Logical Addresses
logical_input_boxes = []
tk.Label(scrollable_frame, text="Logical Addresses", font=("Arial", 11, "bold"), bg="#e0f7fa").grid(
    row=4, column=0, sticky="w", padx=10, pady=5
)

logic_frame = tk.Frame(scrollable_frame, bg="#e0f7fa")
logic_frame.grid(row=5, column=0, columnspan=5, pady=10)

for i in range(2):
    for j in range(5):
        entry = tk.Entry(logic_frame, width=10, bg="#f0fff0")
        entry.grid(row=i, column=j, padx=5, pady=5)
        logical_input_boxes.append(entry)

# Translate Button
tk.Button(scrollable_frame, text=" TRANSLATE ", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
          width=20, command=run_translation).grid(row=7, column=0, columnspan=2, pady=10)

# Right Frame Output
output_frame = tk.Frame(main_frame, bg="#f9f9f9")
output_frame.pack(side="right", fill="both", expand=True, padx=10)

output_title_label = tk.Label(output_frame, text="OUTPUT AREA", font=("Arial", 14, "bold"), bg="#ffe6cc")
output_title_label.pack(fill="x", pady=5)

output_box = tk.Text(output_frame, height=30, width=60, font=("Courier", 10), bg="#fffbea")
output_box.pack(side="left", fill="both", expand=True)

scrollbar_output = tk.Scrollbar(output_frame, command=output_box.yview)
scrollbar_output.pack(side="right", fill="y")
output_box.config(yscrollcommand=scrollbar_output.set)

# Start GUI
root.mainloop()

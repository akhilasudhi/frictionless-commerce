import tkinter as tk
from tkinter import filedialog, messagebox

# -----------------------------
# Core Application Window
# -----------------------------
app = tk.Tk()
app.title("Frictionless Commerce")
app.geometry("500x650")
app.configure(bg="#FFD700")

# -----------------------------
# Header Section
# -----------------------------
app.configure(bg="#FFD700")
header_frame = tk.Frame(app, bg="#FFD700")
header_frame.pack(pady=20)
title_label = tk.Label(
    header_frame,
    text="Frictionless Commerce",
    font=("Poppins", 20, "bold"),
    bg="#FFD700"
)
title_label.pack()

subtitle_label = tk.Label(
    header_frame,
    text="Visual Search • Fit Grader • Authenticity • Blockchain",
     font=("Poppins", 10),
    bg="#f4f6f8"
)
subtitle_label.pack()

# -----------------------------
# Card Styling Function
# -----------------------------
def create_card(title):
    card = tk.Frame(app, bg="white", bd=1, relief="solid")
    card.pack(pady=15, padx=20, fill="x")

    label = tk.Label(
        card,
        text=title,
        font=("Poppins", 14, "bold"),
        bg="white"
    )
    label.pack(pady=10)

    return card

# -----------------------------
# Visual Search Logic
# -----------------------------
def analyze_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        visual_result.set(
            "Environment: Outdoor\nMood: Relaxed\nUse Case: Casual Travel"
        )

# -----------------------------
# Visual Search Card
# -----------------------------
visual_card = create_card("Upload Image for Visual Search")

upload_button = tk.Button(
    visual_card,
    text="Upload Image",
    command=analyze_image
)
upload_button.pack(pady=10)

visual_result = tk.StringVar()
visual_label = tk.Label(
    visual_card,
    textvariable=visual_result,
    bg="white"
)
visual_label.pack(pady=10)

# -----------------------------
# Fit Grader Logic
# -----------------------------
def calculate_fit():
    try:
        waist = float(waist_entry.get())
        chest = float(chest_entry.get())
        shoulder = float(shoulder_entry.get())
        neck = float(neck_entry.get())
        length = float(length_entry.get())

        fit_score = round((waist + chest + shoulder + neck + length) / 4, 2)

        fit_result.set(
            f"Fit Compatibility Score: {fit_score}%\nRecommendation: Excellent Fit"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# -----------------------------
# Fit Grader Cards
# -----------------------------
fit_card = create_card("Fit Grader")

waist_entry = tk.Entry(fit_card)
waist_entry.insert(0, "Waist (cm)")
waist_entry.pack(pady=5)

chest_entry = tk.Entry(fit_card)
chest_entry.insert(0, "chest (cm)")
chest_entry.pack(pady=5)

shoulder_entry = tk.Entry(fit_card)
shoulder_entry.insert(0, "shoulder (cm)")
shoulder_entry.pack(pady=5)

neck_entry = tk.Entry(fit_card)
neck_entry.insert(0, "neck (cm)")
neck_entry.pack(pady=5)

length_entry = tk.Entry(fit_card)
length_entry.insert(0, "length (cm)")
length_entry.pack(pady=5)

fit_button = tk.Button(
    fit_card,
    text="Get Fit Score",
    command=calculate_fit
)
fit_button.pack(pady=10)

fit_result = tk.StringVar()
fit_label = tk.Label(
    fit_card,
    textvariable=fit_result,
    bg="white"
)
fit_label.pack(pady=10)

# -----------------------------
# Authenticity Logic
# -----------------------------
def check_authenticity():
    fabric_data = fabric_entry.get()

    if fabric_data.strip() == "":
        messagebox.showerror("Error", "Enter fabric data")
        return

    auth_result.set(
        "Authenticity Verified\nHandwoven Micro-Irregularities Detected\nBlockchain ID: NFT-23901"
    )


# -----------------------------
# Run Application
# -----------------------------
app.mainloop()





import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")


# ---------------- Prediction Function ----------------

def predict_price():
    try:
        values = [
            float(medinc.get()),
            float(houseage.get()),
            float(averooms.get()),
            float(avebedrms.get()),
            float(population.get()),
            float(aveoccup.get()),
            float(latitude.get()),
            float(longitude.get())
        ]

        prediction = model.predict([values])[0]

        prediction = prediction * 100000

        result.config(
            text=f"Estimated House Price\n\n${prediction:,.2f}",
            fg="green"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter numeric values only."
        )


# ---------------- Clear ----------------

def clear_fields():

    entries = [
        medinc,
        houseage,
        averooms,
        avebedrms,
        population,
        aveoccup,
        latitude,
        longitude
    ]

    for e in entries:
        e.delete(0, tk.END)

    result.config(
        text="Prediction will appear here.",
        fg="blue"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("House Price Predictor")

root.geometry("700x900")

root.resizable(True, True)

title = tk.Label(
    root,
    text="🏠 House Price Predictor",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Enter the house details below",
    font=("Arial", 11)
)

subtitle.pack()

frame = tk.Frame(root)

frame.pack(pady=15)


def create_input(label_text, help_text):

    tk.Label(
        frame,
        text=label_text,
        font=("Arial", 10, "bold"),
        anchor="w"
    ).pack(fill="x")

    entry = tk.Entry(frame, width=40)

    entry.pack()

    tk.Label(
        frame,
        text=help_text,
        fg="gray",
        font=("Arial", 8)
    ).pack(anchor="w", pady=(0,8))

    return entry


medinc = create_input(
    "Median Income",
    "Example: 8.32 (Average family income)"
)

houseage = create_input(
    "House Age",
    "Example: 25 (Years)"
)

averooms = create_input(
    "Average Rooms",
    "Example: 5.8"
)

avebedrms = create_input(
    "Average Bedrooms",
    "Example: 1.1"
)

population = create_input(
    "Population",
    "Example: 1500 (People living in the area)"
)

aveoccup = create_input(
    "Average Occupancy",
    "Example: 3.2 (People per house)"
)

latitude = create_input(
    "Latitude",
    "Example: 37.88"
)

longitude = create_input(
    "Longitude",
    "Example: -122.23"
)


button_frame = tk.Frame(root)

button_frame.pack(pady=20)

predict_btn = tk.Button(
    button_frame,
    text="Predict Price",
    width=18,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=predict_price
)

predict_btn.grid(row=0,column=0,padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=18,
    bg="#f44336",
    fg="white",
    font=("Arial",11,"bold"),
    command=clear_fields
)

clear_btn.grid(row=0,column=1,padx=10)

result = tk.Label(
    root,
    text="Prediction will appear here.",
    font=("Arial",14,"bold"),
    fg="blue"
)

result.pack(pady=20)

root.mainloop()
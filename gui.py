import tkinter as tk
from tkinter import messagebox

def display_recommendation():
    recommendation = get_trading_recommendation(weighted_values)
    messagebox.showinfo("Trading Recommendation", recommendation)

root = tk.Tk()
root.title("Stock Trading Recommendation")
root.geometry("300x200")

recommendation_button = tk.Button(root, text="Get Recommendation", command=display_recommendation)
recommendation_button.pack(pady=50)

root.mainloop()


import tkinter as tk
from tkinter import messagebox
from recommendations import get_trading_recommendation

def display_recommendation():
    recommendation = get_trading_recommendation()
    messagebox.showinfo("Trading Recommendation", recommendation)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Trading Recommendation")
    root.geometry("300x200")

    recommendation_button = tk.Button(root, text="Get Recommendation", command=display_recommendation)
    recommendation_button.pack(pady=50)

    root.mainloop()


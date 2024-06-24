import tkinter as tk
from tkinter import ttk
import pygetwindow as gw

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Capture")
        
        self.label = tk.Label(root, text="Select an application:")
        self.label.pack(pady=10)
        
        self.apps = self.get_applications()
        self.selected_app = tk.StringVar()
        
        self.dropdown = ttk.Combobox(root, textvariable=self.selected_app)
        self.dropdown['values'] = self.apps
        self.dropdown.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Capture", command=self.start_capture)
        self.start_button.pack(pady=10)

    def get_applications(self):
        # Получение списка активных окон
        windows = gw.getAllTitles()
        return [win for win in windows if win]

    def start_capture(self):
        selected_app = self.selected_app.get()
        if selected_app:
            print(f"Starting capture for: {selected_app}")
            # Здесь нужно добавить логику для захвата аудио из выбранного приложения
        else:
            print("No application selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
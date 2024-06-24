import pyaudio
import tkinter as tk
from tkinter import ttk
import pygetwindow as gw
import threading

class App:
    def init(self, root):
        self.root = root
        self.root.title("Audio Capture")
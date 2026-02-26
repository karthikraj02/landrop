import subprocess
import threading
import tkinter as tk
from tkinter import messagebox

def start_receiver():
    subprocess.Popen(["python", "receiver.py"])

def send_message():
    ip = ip_entry.get()
    msg = msg_entry.get()
    subprocess.Popen(["python", "sender.py", ip, f"MSG:{msg}"])

root = tk.Tk()
root.title("LANdrop GUI")
root.geometry("400x200")

tk.Label(root, text="Receiver IP:").pack(pady=5)
ip_entry = tk.Entry(root, width=20)
ip_entry.insert(0, "127.0.0.1")
ip_entry.pack(pady=5)

tk.Label(root, text="Message:").pack(pady=5)
msg_entry = tk.Entry(root, width=30)
msg_entry.pack(pady=5)

tk.Button(root, text="Start Receiver", command=start_receiver, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Send Message", command=send_message, bg="blue", fg="white").pack(pady=5)

root.mainloop()

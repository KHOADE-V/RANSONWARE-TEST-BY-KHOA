#!/usr/bin/env python3
"""Safe visual-only security incident screen demo.

This program does not access, encrypt, modify, or delete user files.
It does not disable desktop controls or prevent the window from closing.
"""

import tkinter as tk
from tkinter import ttk


BG = "#090b10"
PANEL = "#141923"
RED = "#ff4d5a"
TEXT = "#e7eaf0"
MUTED = "#9aa4b2"


def main() -> None:
    root = tk.Tk()
    root.title("Khoa — Visual Security Demo")
    root.configure(bg=BG)
    root.minsize(760, 500)
    root.geometry("980x620")

    # Keep the demo in a regular, movable window.
    root.resizable(True, True)

    outer = tk.Frame(root, bg=BG, padx=28, pady=24)
    outer.pack(fill="both", expand=True)

    demo_tag = tk.Label(
        outer,
        text="SIMULAÇÃO VISUAL • NENHUM ARQUIVO FOI ALTERADO",
        bg="#202b3a",
        fg="#8fd3ff",
        font=("TkDefaultFont", 10, "bold"),
        padx=12,
        pady=8,
    )
    demo_tag.pack(anchor="center", pady=(0, 20))

    title = tk.Label(
        outer,
        text="SECURITY INCIDENT",
        bg=BG,
        fg=RED,
        font=("TkFixedFont", 25, "bold"),
    )
    title.pack(pady=(0, 8))

    subtitle = tk.Label(
        outer,
        text="Interface fictícia para demonstração e estudo de UI",
        bg=BG,
        fg=MUTED,
        font=("TkDefaultFont", 11),
    )
    subtitle.pack(pady=(0, 22))

    panel = tk.Frame(outer, bg=PANEL, padx=26, pady=24, highlightthickness=1,
                     highlightbackground="#303949")
    panel.pack(fill="both", expand=True)

    heading = tk.Label(
        panel,
        text="YOUR FILES ARE SAFE",
        bg=PANEL,
        fg="#8fe0a5",
        font=("TkFixedFont", 19, "bold"),
    )
    heading.pack(anchor="w", pady=(0, 14))

    message = (
        "This is a visual-only ransomware-style screen simulation.\n\n"
        "It does not scan your folders, encrypt files, or make changes\n"
        "to your computer. No payment or recovery action is required."
    )
    body = tk.Label(
        panel,
        text=message,
        bg=PANEL,
        fg=TEXT,
        justify="left",
        font=("TkFixedFont", 11),
    )
    body.pack(anchor="w", pady=(0, 24))

    status = tk.Label(
        panel,
        text="DEMO STATUS: SAFE • FILE SYSTEM: UNTOUCHED",
        bg=PANEL,
        fg="#8fe0a5",
        font=("TkFixedFont", 10, "bold"),
    )
    status.pack(anchor="w", pady=(0, 22))

    close_button = tk.Button(
        panel,
        text="Close demo",
        command=root.destroy,
        bg=RED,
        fg="white",
        activebackground="#e13b49",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=10,
        font=("TkDefaultFont", 11, "bold"),
        cursor="hand2",
    )
    close_button.pack(anchor="w")

    footer = tk.Label(
        outer,
        text="Press ESC or use the window close button to exit at any time.",
        bg=BG,
        fg=MUTED,
        font=("TkDefaultFont", 9),
    )
    footer.pack(pady=(16, 0))

    root.bind("<Escape>", lambda _event: root.destroy())
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    close_button.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()

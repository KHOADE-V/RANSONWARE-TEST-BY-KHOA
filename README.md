# Ransomware Visual Simulator — Khoa

> **Educational visual demo only.** This project does not encrypt, modify, delete, upload, or lock any files or system resources.

A small Tkinter interface that imitates the *appearance* of a security incident screen for demonstrations and interface experiments.

## Requirements

- Python 3.10 or newer
- Tkinter (included with the standard Windows installer from python.org; on Debian, install it with `python3-tk`)

No third-party Python packages are required.

## Run on Windows

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
2. During installation, enable **Add Python to PATH**. Keep the standard **Tcl/Tk and IDLE** feature selected.
3. Download this repository and extract the ZIP, or clone it with Git.
4. Open the extracted project folder.
5. Double-click `run_windows.bat`.

You can also run it manually from PowerShell or Command Prompt:

```powershell
py -3 --version
py -3 ransomware_sim.py
```

If the `py` command is unavailable, try:

```powershell
python --version
python ransomware_sim.py
```

## Run on Debian

Open a terminal in the project folder and run:

```bash
sudo apt update
sudo apt install python3 python3-tk
python3 ransomware_sim.py
```

If you downloaded the repository as a ZIP:

```bash
cd ~/Downloads
unzip RANSONWARE-TEST-BY-KHOA-main.zip
cd RANSONWARE-TEST-BY-KHOA-main
python3 ransomware_sim.py
```

The extracted folder name may vary; use `ls` to check it.

## Exit

- Click **Close demo**.
- Press **Esc**.
- Use the normal window close button.

The window is intentionally not forced into fullscreen and never blocks normal desktop controls.

## Safety notes

- No file-system scanning or encryption.
- No persistence, startup changes, privilege requests, or network connections.
- No payment address or real decryption flow.
- The displayed warning is fictional and the interface labels itself as a simulation.

Use only on your own machine and explain that it is a demo before showing it to others.

## License

Personal/educational project. Add a license file if you want to specify reuse terms.

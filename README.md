# Project Name: Python Mouse Tracker

**Description:**

This Python project utilizes the `pynput` library to continuously monitor and display the real-time coordinates of your mouse cursor on the screen. It's a valuable tool for tasks that require precise mouse positioning or for understanding user interaction patterns.

**Features:**

- **Real-time Tracking:** Captures mouse coordinates as they change.
- **Clear Output:** Displays coordinates in a user-friendly format (X, Y).
- **Optional Loop:** Ensures the program stays active while tracking.
- **Optional Stopping:** Provides a commented-out line to stop the listener if needed (uncomment `listener.stop()`).

**License:**

MIT License

**Installation:**

**Prerequisites:**

1. **Ensure you have Python (version 3.x recommended) installed on your system.** You can check by running `python --version` or `python3 --version` in your terminal.
   - If you don't have Python, download and install it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Clone the Repository:**
   - Open a terminal or command prompt and navigate to the directory where you want to clone the project.
   - Use the following command to clone this repository (replace `https://github.com/your-username/python-mouse-tracker` with the actual URL of your repository):

```bash
git clone https://github.com/akumathedyn123/python-mouse-axis-tracker-xy
```


**Install Dependencies:**
Navigate to the cloned project directory:
```bash
cd python-mouse-axis-tracker-xy
```

**Install the required library using pip:**
```bash
pip install pynput
```

**Usage:**

**Run the Script:**
From the project directory, execute the following command to start tracking your mouse coordinates:
```bash
python main.py
```


The program will continuously display the updated mouse coordinates in your terminal window until you interrupt it (Ctrl+C).
Optional Stopping:

If you want to stop tracking the mouse movements before you interrupt the program with Ctrl+C, uncomment the following line in the main.py file:

```python
#listener.stop()
```

## Contributing:

We welcome contributions to this project! Feel free to fork the repository, make your changes, and submit a pull request.

## Additional Notes:

This is a basic example. You can extend it to perform additional actions based on mouse movement events (e.g., logging coordinates to a file, triggering other functionalities).
For more advanced usage of the pynput library, refer to its official documentation: https://pynput.readthedocs.io/en/latest/

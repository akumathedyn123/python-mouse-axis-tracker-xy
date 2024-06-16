import pynput

# Function to display the coordinates
def on_move(x, y):
    print(f"Mouse Position: ({x}, {y})")

# Create a listener object
listener = pynput.mouse.Listener(on_move=on_move)

# Start listening for mouse movements
listener.start()

# Keep the program running until you interrupt it (Ctrl+C)
while True:
    pass

# Optional: Stop listening when necessary
# listener.stop()

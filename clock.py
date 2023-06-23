import time

while True:
    # Clear the screen (optional, works in some terminals)
    print("\033c", end="")

    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Display the current time
    print(f"Current Time: {current_time}")

    # Wait for 1 second before updating the time
    time.sleep(1)

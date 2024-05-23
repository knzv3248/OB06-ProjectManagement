from pynput import keyboard
import time

def measure_keypress_duration():
    press_time = None
    release_time = None

    def on_press(key):
        nonlocal press_time
        press_time = time.time()
        # print(f"Key {key} pressed at {press_time}")

    def on_release(key):
        nonlocal release_time
        release_time = time.time()
        # print(f"Key {key} released at {release_time}")
        # Stop listener
        return False

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if press_time is not None and release_time is not None:
        duration = (release_time - press_time) * 1000  # Convert to milliseconds
        return duration
    else:
        return None

# Пример использования функции
duration = measure_keypress_duration()
if duration is not None:
    print(f"Duration of key press: {duration} milliseconds")
else:
    print("No key press detected")



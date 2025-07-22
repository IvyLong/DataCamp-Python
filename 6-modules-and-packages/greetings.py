# greetings.py
import sys
def say_hello(name):
    """Print a hello message to the given name."""
    print(f"Hello, {name}!")

def say_goodbye(name):
    """Print a goodbye message to the given name."""
    print(f"Goodbye, {name}!")

def get_greeting(name, time_of_day="day"):
    """Return a greeting based on time of day."""
    greetings_map = {
        "morning": f"Good morning, {name}!",
        "afternoon": f"Good afternoon, {name}!",
        "evening": f"Good evening, {name}!",
        "day": f"Hello, {name}!"
    }
    return greetings_map.get(time_of_day, f"Hello, {name}!")

# Module-level variable
DEFAULT_NAME = "World"

if __name__ == "__main__":
    # This code runs only when the module is executed directly
    print("Testing greetings module:")
    say_hello("Alice")
    say_goodbye("Bob")

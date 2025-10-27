"""
Demonstrates common standard library modules:
- json: For serializing and deserializing data
- datetime: For working with dates and times
"""

import json
import datetime

def demonstrate_json():
    """Shows how to dump and load JSON data."""
    print("--- JSON Module Demo ---")

    # A Python dictionary (similar to a JSON object)
    user_data = {
        "id": 123,
        "name": "Bob",
        "active": True,
        "skills": ["Python", "Docker", "Git"]
    }

    # 1. Serialize: Convert Python dict to a JSON string
    # `indent=2` makes it human-readable
    json_string = json.dumps(user_data, indent=2)
    print("Python dict serialized to JSON string:\n", json_string)

    # 2. Deserialize: Convert JSON string back to a Python dict
    loaded_data = json.loads(json_string)
    print(f"\nJSON string deserialized back to Python dict:")
    print(f"  Name: {loaded_data['name']}")
    print(f"  Skills: {loaded_data['skills']}")

    # Check that the type is now a dict
    print(f"  Type of loaded data: {type(loaded_data)}")

def demonstrate_datetime():
    """Shows how to work with dates and times."""
    print("\n--- Datetime Module Demo ---")

    # Get the current date and time
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

    # Get just the current date
    today = datetime.date.today()
    print(f"Today's date: {today}")

    # Formatting a date into a string (strftime)
    formatted = now.strftime("%Y-%m-%d %H:%M:%S (%A)")
    print(f"Formatted time: {formatted}")

    # Parsing a string into a datetime object (strptime)
    date_string = "2025-01-31"
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    print(f"Parsed date: {parsed_date}")

    # Time deltas
    ten_days_from_now = now + datetime.timedelta(days=10)
    print(f"Ten days from now: {ten_days_from_now.strftime('%Y-%m-%d')}")

def run_demo():
    """Runs all demonstrations in this module."""
    demonstrate_json()
    demonstrate_datetime()

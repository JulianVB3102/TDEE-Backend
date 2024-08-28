import json
import os

def save_user_data(filename, user_data):
    """
    Save user data to a file in JSON format.
    
    Parameters:
    filename (str): The name of the file where data will be saved.
    user_data (dict): A dictionary containing user data to be saved.
    
    Returns:
    None
    """
    # Check if file exists; if not, create it and write an empty list
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            json.dump([], file)
    
    # Read the existing data from the file
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Append new user data to the existing data
    data.append(user_data)
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"User data has been successfully saved to {filename}.")

def main():
    """
    Main function to gather user data and save it to a file.
    """
    # Collect user input
    weight = float(input("Enter your weight in pounds (lbs): "))
    height = float(input("Enter your height in inches: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male/female): ").strip()
    activity_level_desc = input("Enter your activity level (sedentary, light, moderate, active, very active): ").strip()
    tdee = float(input("Enter your TDEE value: "))
    
    # Prepare the user data dictionary
    user_data = {
        'weight': weight,
        'height': height,
        'age': age,
        'gender': gender,
        'activity_level': activity_level_desc,
        'tdee': tdee
    }
    
    # Specify the filename
    filename = 'user_data.json'
    
    # Save the user data to the file
    save_user_data(filename, user_data)

if __name__ == "__main__":
    main()

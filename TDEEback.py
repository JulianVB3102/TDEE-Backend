# Import libraries
# In this case, math is imported for rounding purposes
import math

def calculate_bmr(weight, height, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation.
    The formula has been adjusted for imperial measurements.
    
    Parameters:
    weight (float): Weight in pounds
    height (float): Height in inches
    age (int): Age in years
    gender (str): 'male' or 'female'
    
    Returns:
    float: BMR value
    """
    if gender.lower() == 'male':
        bmr = 4.536 * weight + 15.88 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 4.536 * weight + 15.88 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    
    return bmr

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure (TDEE).
    
    Parameters:
    bmr (float): Basal Metabolic Rate
    activity_level (float): Activity level multiplier
    
    Returns:
    float: TDEE value
    """
    tdee = bmr * activity_level
    return round(tdee, 2)

def get_activity_multiplier(activity_level):
    """
    Get the activity level multiplier based on the user's lifestyle.
    
    Parameters:
    activity_level (str): Description of the activity level
    
    Returns:
    float: Corresponding activity multiplier
    """
    activity_levels = {
        'sedentary': 1.2,        # Little to no exercise
        'light': 1.375,          # Light exercise/sports 1-3 days/week
        'moderate': 1.55,        # Moderate exercise/sports 3-5 days/week
        'active': 1.725,         # Hard exercise/sports 6-7 days a week
        'very active': 1.9       # Very hard exercise, physical job, or training twice a day
    }
    
    return activity_levels.get(activity_level.lower(), 1.2)

def main():
    """
    Main function to calculate TDEE
    
    Gathers input from the user, calculates BMR, then uses it to calculate TDEE
    """
    # Collect user input
    print("Welcome to the TDEE Calculator using the Mifflin-St Jeor Equation (Imperial Units)")
    
    weight = float(input("Enter your weight in pounds (lbs): "))
    height = float(input("Enter your height in inches: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male/female): ").strip()
    
    # Validate gender input
    if gender.lower() not in ['male', 'female']:
        print("Invalid gender input. Please enter 'male' or 'female'.")
        return
    
    # Get activity level
    activity_level_desc = input("Enter your activity level (sedentary, light, moderate, active, very active): ").strip()
    activity_level = get_activity_multiplier(activity_level_desc)
    
    # Calculate BMR
    bmr = calculate_bmr(weight, height, age, gender)
    
    # Calculate TDEE
    tdee = calculate_tdee(bmr, activity_level)
    
    # Output the result
    print(f"\nYour Total Daily Energy Expenditure (TDEE) is approximately: {tdee} calories/day")

if __name__ == "__main__":
    main()

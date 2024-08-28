# TDEE Calculator and User Data Logger

This project provides a simple Python application to calculate Total Daily Energy Expenditure (TDEE) using the Mifflin-St Jeor equation and log user data to a file for record-keeping.

## Features

- **TDEE Calculation**: Calculates TDEE based on user inputs (weight, height, age, gender, and activity level) using the Mifflin-St Jeor equation.
- **Imperial Measurements**: The calculator works with imperial units (pounds for weight and inches for height).
- **User Data Logging**: Saves the user's data (weight, height, age, gender, activity level, and TDEE) to a JSON file for future reference.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository or download the files.
2. Ensure you have Python 3 installed on your machine.

### Usage

#### TDEE Calculator

1. Run the `tdee_calculator.py` script.
2. Enter your weight in pounds, height in inches, age, gender, and activity level when prompted.
3. The script will calculate your TDEE and display it.

#### User Data Logger

1. Run the `save_user_data.py` script.
2. Enter your details as prompted (weight, height, age, gender, activity level, and TDEE).
3. The data will be saved to `user_data.json`.

#### Example Commands

```sh
python tdee_calculator.py

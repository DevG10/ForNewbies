from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    try:
        # Get user input for birthdate
        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        
        # Calculate and print the user's age
        age = calculate_age(birthdate)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()

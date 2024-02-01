def create_user_profile():
    print("Please provide some basic information about yourself.")
    name = input("Enter your name: ").strip()
    phone_model = input("Enter your phone model: ").strip()
    # Add more fields if necessary

    return {
        "name": name,
        "phone_model": phone_model
    }

def display_user_profile(profile):
    print("\nUser Profile:")
    for key, value in profile.items():
        print(f"{key.title()}: {value}")

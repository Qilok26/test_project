# Week 01 Lab: Standard 

def age_restrictions(age: int):
    """Return a list of messages based on age rules."""
    messages = []
    if age < 13:
        messages.append("You cannot sit in the passenger seat of a car.")
    if age < 18:
        messages.append("You cannot vote.")
    if age < 25:
        messages.append("You cannot rent a car.")
    if age > 35:
        messages.append("You are getting old...")
    return messages


def create_user():
    """Create a new user dictionary."""
    user = {}
    user["name"] = input("Enter your name: ")
    user["age"] = int(input("Enter your age: "))
    multilingual = input("Are you multilingual? (yes/no): ").strip().lower()

    languages = []  

    if multilingual in ("yes"):
        
        while True:
            n_str = input("How many languages do you speak? ").strip()
            if not n_str.isdigit():
                print("Please enter a whole number (e.g., 2).")
                continue
            num_languages = int(n_str)

            if num_languages < 2:
                print("You know less than two languages, lying is bad.")
                multilingual = "no"    # downgrade to no
            else:
                for i in range(num_languages):
                    lang = input(f"Enter language #{i+1}: ").strip()
                    languages.append(lang)
            break  # we were in a while-loop, so break is legal here

    # handle the 'no' path (including the downgraded case)
    if multilingual in ("no", "n"):
        desired = input("What language would you like to learn? ").strip()
        languages = [f"Would like to learn: {desired}"]

    # finally store on the user dict
    user["languages"] = languages

    # Greeting
    print("Hello {user['name']}, welcome to my programm")

    # Age rules
    restrictions = age_restrictions(user["age"])
    for msg in restrictions:
        print("-", msg)

    # Language feedback
    print("Languages:", ", ".join(user["languages"]))
    return user


def main():
    users = []

    while True:
        choice = input("\nDo you want to create a new user? (yes/no/select/delete/quit): ").strip().lower()

        if choice == "yes":
            user = create_user()
            users.append(user)

        elif choice == "select":
            if not users:
                print("No users available yet.")
                continue
            for i, user in enumerate(users):
                print(f"{i+1}. {user['name']}")
            idx = int(input("Select a user by number: ")) - 1
            if 0 <= idx < len(users):
                print(" Selected User Info:")
                print(users[idx])
            else:
                print("Invalid selection.")

        elif choice == "delete":
            if not users:
                print("No users to delete.")
                continue
            for i, user in enumerate(users):
                print(f"{i+1}. {user['name']}")
            idx = int(input("Which user do you want to delete? Enter number: ")) - 1
            if 0 <= idx < len(users):
                deleted = users.pop(idx)
                print("User {deleted['name']} deleted.")
            else:
                print("Invalid selection.")

        elif choice == "no":
            print("Okay, no new user created.")

        elif choice == "quit":
            print("\nAll Users Collected:")
            for user in users:
                print(user)
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please type yes/no/select/delete/quit.")


if __name__ == "__main__":
    main()

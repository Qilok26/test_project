import json
import random
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()
DATA_FILE = "users.json"


def load_users():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)



def age_progression(age: int):
    milestones = {
        16: "Drive a car ",
        18: "Vote ",
        21: "Drink alcohol  (in US)",
        25: "Rent a car ",
        65: "Retire "
    }

    console.print("\n[bold cyan]Life Privileges Based on Age[/bold cyan]")

    if age < 13:
        console.print("[red]You cannot sit in the front passenger seat of a car.[/red]")
    if age > 35:
        console.print("[yellow]You're getting old... [/yellow]")

    with Progress() as progress:
        task = progress.add_task("Checking privileges...", total=len(milestones))
        for milestone, event in milestones.items():
            if age >= milestone:
                console.print(f"[green]✓ {event}[/green]")
            else:
                console.print(f"[red]✗ {event}[/red] (available at {milestone})")
            progress.advance(task)


def handle_languages(multilingual: str):
    if multilingual == "yes":
        # Ask number of languages
        while True:
            n_str = console.input("How many languages do you speak? ").strip()
            if not n_str.isdigit():
                console.print("[red]Please enter a whole number (e.g., 2).[/red]")
                continue
            num = int(n_str)
            break

        languages = []
        if num < 2:
            console.print("[yellow]Hmm... you said you're multilingual but only listed one language.[/yellow]")
            console.print("[red]Let's move you to the learning plan instead![/red]")
            return handle_languages("no")
        else:
            for i in range(num):
                lang = console.input(f"Enter language #{i+1}: ")
                languages.append(lang)
            return sorted(languages)

    else:
        desired = console.input("What language would you like to learn? ").strip().capitalize()
        study_hours = random.randint(3, 10)
        console.print(f"[yellow]Learning Plan:[/yellow] Study {desired} for {study_hours} hours per week.")

        translations = {
            "English": {"Hello": ["Hello", "Goodbye", "Thanks"], "correct": "Hello"},
            "Spanish": {"Hello": ["Hola", "Adiós", "Gracias"], "correct": "Hola"},
            "Russian": {"Hello": ["Привет", "Пока", "Спасибо"], "correct": "Привет"},
        }

        if desired in translations:
            console.print(f"\n[bold cyan]Quick {desired} Quiz![/bold cyan]")
            phrase = "Hello"
            options = translations[desired][phrase]
            correct = translations[desired]["correct"]

            console.print(f"What is the correct translation of '{phrase}' in {desired}?")
            for i, opt in enumerate(options, 1):
                console.print(f"{i}. {opt}")

            choice = console.input("Your choice (1/2/3): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= 3:
                if options[int(choice)-1] == correct:
                    console.print("[green]Correct! 🎉[/green]")
                else:
                    console.print(f"[red]Not quite. The correct answer is '{correct}'.[/red]")
            else:
                console.print("[red]Invalid choice. Skipping quiz.[/red]")

        return [f"Learning {desired}"]



def create_user():
    user = {}
    user["name"] = console.input("Enter your name: ")
    user["age"] = int(console.input("Enter your age: "))
    multilingual = console.input("Are you multilingual? (yes/no): ").strip().lower()

    user["languages"] = handle_languages(multilingual)

    user["password"] = console.input("Set a password for this user: ")

    console.print(f"\n[bold green]Hello {user['name']}![/bold green] Welcome to the program 🎉")
    age_progression(user["age"])

    table = Table(title="Languages")
    table.add_column("Spoken / Learning", style="magenta")
    for lang in user["languages"]:
        table.add_row(lang)
    console.print(table)

    return user


def main():
    users = load_users()

    while True:
        choice = console.input("\nDo you want to [green]create[/green] a new user, [cyan]select[/cyan], [red]delete[/red], or [bold]quit[/bold]? ").strip().lower()

        if choice == "create":
            user = create_user()
            users.append(user)
            save_users(users)

        elif choice == "select":
            if not users:
                console.print("[red]No users available yet.[/red]")
                continue

            table = Table(title="Saved Users")
            table.add_column("Index", style="cyan")
            table.add_column("Name", style="yellow")
            for i, user in enumerate(users):
                table.add_row(str(i+1), user["name"])
            console.print(table)

            idx = int(console.input("Select a user by number: ")) - 1
            if 0 <= idx < len(users):
                selected_user = users[idx]
                console.print(f"[bold cyan]User Info:[/bold cyan]")
                console.print(f"Name: {selected_user['name']}")
                console.print(f"Age: {selected_user['age']}")
                console.print(f"Languages: {', '.join(selected_user['languages'])}")

                
                admin_try = console.input("Are you an admin? Enter password (or leave blank to skip): ")
                if admin_try == "banana":
                    console.print(f"[yellow]User password: {selected_user['password']}[/yellow]")
                else:
                    console.print("[dim]Password hidden (admin access required).[/dim]")

            else:
                console.print("[red]Invalid selection.[/red]")


        elif choice == "delete":
            if not users:
                console.print("[red]No users to delete.[/red]")
                continue
            for i, user in enumerate(users):
                console.print(f"{i+1}. {user['name']}")
            idx = int(console.input("Which user do you want to delete? Enter number: ")) - 1
            if 0 <= idx < len(users):
                password_try = console.input(f"Enter password for {users[idx]['name']}: ")
                if password_try == users[idx]["password"]:
                    deleted = users.pop(idx)
                    save_users(users)
                    console.print(f"[red]User {deleted['name']} deleted.[/red]")
                else:
                    console.print("[red]Incorrect password. User not deleted.[/red]")
            else:
                console.print("[red]Invalid selection.[/red]")

        elif choice == "quit":
            console.print("\n[bold cyan]All Users Collected:[/bold cyan]")
            console.print(users)
            console.print("[green]Program ended.[/green]")
            break

        else:
            console.print("[red]Invalid choice. Please type create/select/delete/quit.[/red]")

if __name__ == "__main__":
    main()
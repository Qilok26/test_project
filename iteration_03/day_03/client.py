import requests

BASE_URL = "http://127.0.0.1:5000"

def get_single_joke():
    response = requests.get(f"{BASE_URL}/api/joke")
    if response.ok:
        joke = response.json()
        print("Here's a joke for you:")
        print(f"{joke['setup']} - {joke['punchline']}")
    else:
        print("Error fetching a joke.")

def get_multiple_jokes(n):
    response = requests.get(f"{BASE_URL}/api/jokes/{n}")
    if response.ok:
        jokes = response.json()
        print(f"\nHere are {n} jokes for you:")
        for i, joke in enumerate(jokes, 1):
            print(f"{i}. {joke['setup']} - {joke['punchline']}")
    else:
        print(f"Error fetching {n} jokes.")

if __name__ == "__main__":
    get_single_joke()
    get_multiple_jokes(3)
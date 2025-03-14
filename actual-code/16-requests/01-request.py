import requests

try:
    response = requests.get("https://api.github.com/users/doingandlearning")
    response.raise_for_status()  # non-200 status codes, you have trigger an error!
    print(response)
    response_dict = response.json()
    print(f"The username {response_dict['login']} is called {response_dict['name']}")
except Exception as e:
    print(e)


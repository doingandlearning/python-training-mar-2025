import requests

data = {'title': 'New Post', 'body': 'This is a great new post!'}

# Headers!
headers = {'Authorization': 'Bearer my_token'}  # identification!

response = requests.post("https://jsonplaceholder.typicode.com/posts",
                         json=data,
                         headers=headers
                         )
print(response.json())  # 201 - Created

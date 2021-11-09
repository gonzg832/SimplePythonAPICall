import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint # + query

response = requests.get(url)
breeds = response.json()["message"]

# get a list ofa ll breeds from the API call
all_breeds = breeds.keys()

# loop and print out each key
for breed in all_breeds:
  print(breed)

# get a list of all subbreeds of a breed with at least 3 sub_breeds 
terrier_subbreeds = breeds["terrier"]
input("\nPress enter to get all terrier subbreeds")
for sub in terrier_subbreeds:
  print(sub)

# display all bulldog subbreeds
bulldog_subbreeds = breeds["bulldog"]
input("\nPress enter to get all bulldog subbreeds")
for sub in bulldog_subbreeds:
  print(sub)
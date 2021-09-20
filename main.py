import requests
from datetime import datetime

USERNAME = "richiepatel"
TOKEN = "qwertyuiop"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATES USER ACCOUNT IN API
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------------------------------------------------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config_params = {
    "id": "",
    "name": "CAT preparation Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# CREATES GRAPH FOR TRACKING HABIT (EMPTY)
# response2 = requests.post(url=graph_endpoint, json=graph_config_params, headers=headers)
# print(response2.text)

# -------------------------------------------------- #
today = datetime.now()
# print(today.strftime("%Y%m%d"))

plotting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
plotting_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": f"{input('How many hours you have done CAT preparation?:  ')}",
}

# PLOT AS PER OUR WORK DONE TODAY
response3 = requests.post(url=plotting_pixel_endpoint, json=plotting_pixel_params, headers=headers)
print(response3.text)

# ----------------------------------------------------------- #
date = "20210919"
updating_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
updating_pixel_params = {
    "quantity": "0",
}

# UPDATE / EDIT PLOTS PREVIOUSLY MADE
# response4 = requests.put(url=updating_pixel_endpoint, json=updating_pixel_params, headers=headers)
# print(response4.text)

# ------------------------------------------------------------ #
deleting_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# DELETE WHOLE PLOT DONE ON DATE
# response5 = requests.delete(url=deleting_pixel_endpoint, headers=headers)
# print(response5.text)

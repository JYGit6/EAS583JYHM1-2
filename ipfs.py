import requests
import json

project_id = "be2ef85d1a72415da3a281ecd351f9f8"
project_secret = "T7mYAPaDeaUPnmkFDv0sZh42UKsE7/YC0THa9ZtqUwicN2+O96nNAA"

endpoint = "https://ipfs.infura.io:5001/api/v0/cat?arg={be2ef85d1a72415da3a281ecd351f9f8}"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	url = f"{endpoint}/add"
	params = {"pin":"true"}
	files = {"file": ("data.json", json_data, "application/json")}
	response = requests.post(
		url, params=params, files=files,
		auth=(project_id, project_secret), timeout=60)
	response.raise_for_status()
	
	result = response.json()
	cid = result["Hash"]

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	url = f"{endpoint}/cat"
	params = {"arg":cid}

	response = requests.post(
		url, params=params,
		auth=(project_id, project_secret), timeout=60)
	response.raise_for_status()

	data = json.loads(response.text)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

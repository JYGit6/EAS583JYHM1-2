import requests
import json

JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIxZTEwNWE5MC1hMmUyLTRiZDgtYjAwYy02MTUzNWFhYTA1NzkiLCJlbWFpbCI6Imp5YW42QGVuZ2luZWVyaW5nLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiI3OTNmYmUzNWJiNzBkMWEwNWVjMiIsInNjb3BlZEtleVNlY3JldCI6ImRlYTFmNWYzNDU1MzE1MWNmZGUzMzlhMjE0ZTQ5OTQ2MzE5MDY1Y2IyMjg3MGRjMGEzZmQ5YjM2NmQ0NWUzMDYiLCJleHAiOjE4MjM1Nzc1ODR9.30ZGJKig5QdxfXtWabY7RC1vvHqHE2xSnFJTbMc4pIE"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {"Authorization": f"Bearer {JWT}",
	"Content-Type": "application/json"}
	response = requests.post(
		url, headers=headers, json={"pinataContent": data}, timeout=60)
	response.raise_for_status()
	
	cid = response.json()["IpfsHash"]

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url, timeout=60)
	response.raise_for_status()

	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

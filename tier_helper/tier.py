import json
import requests

def pull_api_json(endpoint, filepath):
	data = get_url(endpoint)

	write_file(filepath, data)

def get_url(url: str):
	response = requests.get(url)

	return response.text

def write_file(filename, data):
	if type(data) == type([]):
		data = json.dumps(data)

	with open(filename, 'w') as f:
		f.write(data)

def read_tiers(filepath, pet_tier, food_tier):
	with open(filepath) as f:
		data = json.load(f)

		pets = data['pets']
		foods = data['foods']

		for pet in pets:
			pet = pets[pet]
			name = pet['name']
			tier = pet['tier']

			if type(tier) == int:
				tier -= 1
				pet_tier[tier].append(name)

		for food in foods:
			food = foods[food]
			name = food['name']
			tier = food['tier']

			if type(tier) == int:
				tier -= 1
				food_tier[tier].append(name)

	return [pet_tier, food_tier]

def generate_tiers():
	DATA_FILEPATH = './data/api.json'
	DATA_ENDPOINT = 'https://superauto.pet/api.json'

	tiers = 6
	pet_tier = [[] * tiers for i in range(tiers)]
	food_tier = [[] * tiers for i in range(tiers)]

	# pull_api_json(DATA_ENDPOINT, DATA_FILEPATH)

	pet_tier, food_tier = read_tiers(DATA_FILEPATH, pet_tier, food_tier)

	TIER_ANIMAL = './data/animals.json'
	TIER_FOOD = './data/foods.json'

	write_file(TIER_ANIMAL, pet_tier)
	write_file(TIER_FOOD, food_tier)

if __name__ == "__main__":
	generate_tiers()
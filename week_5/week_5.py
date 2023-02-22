#week_5 homework

import json

nationality_data = {}


with open('Artworks.json') as file:
	artworks_json = json.load(file)
	for artwork in artworks_json:
		nationalities = artwork['Nationality']
		for nat in nationalities:
			if nat in nationality_data:
			 nationality_data[nat].append(artwork)
			else:
			 nationality_data[nat] = []
			 nationality_data[nat].append(artwork)
			
for nat in nationality_data:
 with open(f'res/{nat}.json', 'w') as out_file:
 	json.dump(nationality_data[nat],out_file, indent=2)


#   import json

#res = []
#with open('pets.json') as file:
#	json_file = json.load(file)
#	for pet in json_file:
#		if pet['Type'] == 'cat':
#			res.append(pet)
#			print(pet)

#with open('cats.json', 'w') as write_file:
#	json.dump(res,write_file,indent=2)

#import json

#with open('Documents/info664exercises/week_5/Artworks.json') as file:
#	json_file = json.load(file)
#	for Nationality in json_file
	
#res = []
#with open('nationality.json, 'w') as 

#	json.dump(res,write_file,indent=2)
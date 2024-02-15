import requests
from bs4 import *
import csv


with open('cleaned_pudding_data.csv', 'r') as csvfile:
	with open('pudding_movie_dialogue.csv', 'w') as dialogueout:
		writer = csv.writer(dialogueout)
		writer.writerow(['link', 'script'])
		movielist = csv.DictReader(csvfile)
		for row in movielist:
			#get link from row
			movie = requests.get(row['link'])
			parsedmovie = BeautifulSoup(movie.text, "html.parser")
			writer.writerow([row['link'], parsedmovie.get_text()[:1000]])



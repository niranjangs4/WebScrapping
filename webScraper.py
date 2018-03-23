# Developed By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 12/sep/2017


from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import re
import matplotlib.pyplot as plt

### this is not complete code contact 7019832930
class Webscraper:
	def __init__(self, url):
		self.url = url
		self.tags_each_place = []
		self.more_pages()

	def more_pages(self):

		data = get(self.url)
		f1 = open('all_things.txt', 'w')
		soup = BeautifulSoup(data.content, "html.parser")
		print("CURRENT PAGE URL IS:", self.url)
		states = soup.find_all("div", class_="col-md-12 activities-and-listings")
		cities = soup.find_all("div", class_="col-md-12 activities-and-listings")
		states = list([self.url + state.get('href') + '/things-to-do' for i in states for state in
		               i.find_all('a', href=re.compile('^/states/'))])
		all_links = []
		for each_state in cities, states:
			for all_place in each_state:
				all_links.append(all_place)
				file = all_place.split('/')[-2]
				f1.write(str(all_place + '\r\n'))
				f2 = open('-links-things-to-do.txt', 'w')
				f3 = open('-links-with-category-and-count.txt', 'w')

				print("current page " + all_place)

				each_place_url = get(all_place)
				soup = BeautifulSoup(each_place_url.content, "html.parser")
				catogaries = soup.find_all("div", class_="filter-xor")

				total_bot = []
				activity = []
				countplace = []
				for catogary_href in catogaries:
					f3.write(str(catogary_href) + '\r\n')
					tags_each_place = self.url + catogary_href.find('a').get('href')
					f2.write(str(tags_each_place + '\r\n'))
					activity.append(category)
					count_places = catogary_href.text.split(' ')[-1].split('(')[-1].split(')
					countplace.append(int(count_places))
					city = tags_each_place.split('/')[4].replace('-', ' ').title()
					each_tags = get(tags_each_place)
					print('tags each place', tags_each_place)
					soup = BeautifulSoup(each_tags.content, "html.parser")
					place_name_tags = soup.find_all("li", class_="grid-item case02")
					# f4 = open(f'{city}-{category}.txt', 'w')
					brought_count = []
					for place_details in place_name_tags:
						place = place_details.find("div", class_="name")
						# f4.write(str(place.text) + "\r\n")
						if "Featured" not in place:
							brought = place_details.find("span", class_="sold")
							if brought != None:
								brought_count.append(int(brought_co))

					total_bot.append(sum(brought_count))
				print(activity, countplace, total_bot)

				for i in range(len(total_bot)):
					if total_bot[i] == 0:
						total_bot[i] = 1

				dataset = list((activity, countplace, total_bot))
				df = pd.DataFrame(data=dataset, columns=['Activities', 'Total_Count', 'Total_Bought'])

				df['efficieny'] = 100 * (df['Total_Bought'] - df['Total_Count']) / df['Total_Bought']

				print(df)
				labels = activity
				cat = total_bot
				plt.pie(cat, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
				plt.title(city, bbox={'facecolor': '0.8', 'pad': 5})
				plt.draw()
				plt.savefig(city+'.png')
				plt.clf()
				df.to_csv(city+".csv")
				print("\n")
Webscraper("===============")



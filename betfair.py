from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv




def rem(word, character):
	newword = ''
	for i in word:
		if i != character:
			newword = newword + i
	return newword

quote_page ='https://www.betfair.com/sport/football'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

#print(soup)

#matcher = re.compile('^.display-decimal-price$')
#scrap_global = soup.find_all(class_="avb-col avb-col-markets")
scrap_teams = soup.find_all(class_="team-name")
scrap_times = soup.find_all(class_="date ui-countdown")
#print(scrap_global)
#scrap_prices = soup.select("#selection sel-0 ")
#print(scrap_prices)
teams = []
decimal_prices = []
times = []

e = 0
sub_list = []

spans = soup.select('span')
str_spans = [str(s) for s in spans]
str_prices = []
prices = []

for s in spans:

	if (str(s).find('decimal-price'))!= -1:
		prices.append(s)
		str_prices.append(str(s))

#print(str_prices)
#print(prices)
#print(len(prices))
#print(str_spans[0])
#print(type(str_spans[0]))
#print(type("hello"))
#print(str_spans[0])
#print(str_spans[0][1])

#print(str_spans)
#print(type(str_spans[0]))
#print(str_spans[0].find("span"))

a = 0
sub_list2 = []
print(str_prices[2][0:45])
print(str_prices[3][0:45])
print(str_prices[4][0:45])
for i in range(0, len(str_prices) - 2):

	if str_prices[i][0:45] == str_prices[i+1][0:45] and str_prices[i][0:45] == str_prices[i+2][0:45]:
		decimal_prices.append([rem(prices[i].getText(), '\n'), rem(prices[i+1].getText(), '\n'), rem(prices[i+2].getText(), '\n')])
	else:
		continue

print(decimal_prices)
print(len(decimal_prices))		
#print(str_spans[:50])
#print(str_spans[8])
#list_of_prices = [s for s in str_spans if re.match(s, "decimal-price")]
#spans = soup.find_all('span')
#print(list_of_prices)

for i in scrap_teams:
	sub_list.append(rem(i.getText(), '\n'))
	e = e + 1
	if e%2 == 0:
		teams.append(sub_list)
		sub_list = []
#print(teams)
#print(len(teams))
for k in scrap_times:
	times.append(k.getText())

#print(times)
print(len(teams))
print(len(times))

a = 0
sub_list2 = []

"""for k in spans:
	sub_list2.append(k.getText())
	a = a + 1
	if a%3 == 0:
		decimal_prices.append(sub_list2)
		sub_list2 = []
"""

#print(scrap_global[0].find_all(class_ = "date ui-countdown"))
#print(decimal_prices)

while len(teams) > len(times):
	times = ["already started"] + times 


with open('data_betfair.csv', 'w', encoding = 'utf-8') as csv_file:
    article_writer = csv.writer(csv_file)
    fieldnames= ['team1_name', 'team2_name', 'game_time', 'best_ratio_team1', 'best_ratio_team1_betting_site', 'best_ratio_draw', 'best_ratio_draw_betting_site', 'best_ratio_team2', 'best_ratio_team2_betting_site']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()   
    for k in range (len(teams)):
    	writer.writerow({'team1_name': rem(teams[k][0], '\n'), 'team2_name': rem(teams[k][1], '\n'), 'game_time': rem(times[k], '\n'), 'best_ratio_team1': rem(decimal_prices[k][0], '\n'), 'best_ratio_team1_betting_site': 'betfair', 'best_ratio_draw': rem(decimal_prices[k][1], '\n'), 'best_ratio_draw_betting_site': 'betfair', 'best_ratio_team2': rem(decimal_prices[k][2], '\n'), 'best_ratio_team2_betting_site': 'betfair'} )


print("done")
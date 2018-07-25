import requests
import bs4
if __name__=='__main__':
	url = "http://travelyaari.com/offers"
	page = requests.get(url)
	print page
	soup = bs4.BeautifulSoup(page.content, 'lxml')
	rwdata=soup.find(name='section',attrs={'class':'wrapper'})
	#rwdata=soup.find(name='section',attrs={'class':'y-site-footer-image'})
	print rwdata

from cinemas.models import Movie
from django.utils import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import bs4

headers = {
    'Referer': '',
}

LOCATION_JAKARTA = "JAKARTA"
url_movies_playing_now = 'http://www.21cineplex.com/nowplaying'
url_cinemas_info = 'http://www.21cineplex.com/cinemas'
cinemaS = {}

IMAX = "IMAX"
XXI = "XXI"
PREMIERE = "PREMIERE"
NO_CLASS = "NO CLASS"

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=23, minutes=35)
def get_movies_playing_now():
    print("MILKENTTTTTTTTT")
    global url_movies_playing_now
    Movie.objects.all().delete()
    while(url_movies_playing_now):
        title = []
        description = []
        #Create BeatifulSoup Object with url link
        s = requests.get(url_movies_playing_now, headers=headers)
        soup = bs4.BeautifulSoup(s.text, "html.parser")
        movies = soup.find_all('ul', class_='w462')[0]
        
        #Find Movie's title
        for movie_title in movies.find_all('h3'):
            title.append(movie_title.text)
        #Find Movie's description
        for movie_description in soup.find_all('ul',
                                               class_='w462')[0].find_all('p'):
            description.append(movie_description.text.replace(" [More]","."))
        
        for t, d in zip(title, description):
            m = Movie(movie_title=t, movie_description=d)
            m.save()

		#Go to the next page to find more movies
        paging = soup.find( class_='pagenating').find_all('a', class_=lambda x:
                                                          x != "inactive")
        href = ""
        for p in paging:
            if "next" in p.text.lower():
                href = p['href']
        url_movies_playing_now = href



sched.start()
def get_movie_class(group):
	if IMAX in str(group.findAll('a')):
		return IMAX
	elif XXI in str(group.findAll('a')):
		return IMAX
	elif PREMIERE in str(group.findAll('a')):
		return IMAX
	else:
		return ""

def get_showtimes(cinema_url):
	s = requests.get(cinema_url, headers=headers)
	soup = bs4.BeautifulSoup(s.text)
	groups = soup.findAll('div', id='makan')
	movies_showtimes = []
	for group in groups:		
		movie_type = get_movie_class(group)
		movie_elements = group.findAll('tr', {'class':['dark', 'light']})

		for movie_element in movie_elements:
			if len(movie_element.contents) == 3 :
				showtimes =  movie_element.contents[1].text.split()
				movie = movie_element.contents[0].text
				movies_showtimes.append((movie, showtimes,movie_type))

	return movies_showtimes

def normalize(cinema_name):
	if IMAX in cinema_name:
		cinema_type = IMAX
	elif XXI in cinema_name:
		cinema_type = XXI
	elif PREMIERE in cinema_name:
		cinema_type = PREMIERE
	else:
		cinema_type = ""

	name = cinema_name.replace(cinema_type,"").strip()

	if not cinema_type:
		name = name + " " + NO_CLASS
	return name

def is_not_duplicate_cinemas(name):
	if name not in cinemaS:
		cinemaS[name] = True
		return True
	else:
		return False

def find_jakarta_cinema(cinema_details, cinema_names, website_links):
	cinema_details_list = cinema_details.contents
	try:
		if len(cinema_details_list) == 2:
			contents_list = cinema_details_list[0].contents

			while contents_list:
				content = contents_list.pop()

				if content.name == 'a' and 'href'in content.attrs:
					web = content.attrs['href']

				if content.name == "span" and content.string.upper() == LOCATION_JAKARTA:
					cinema_name = normalize(content.previous_sibling.previous_sibling.string)
					if is_not_duplicate_cinemas(cinema_name):
						cinema_names.append(cinema_name)
						website_links.append(web)
					return

				if content.name == "span" and content.string.upper() != LOCATION_JAKARTA:
					return

				elif len(contents_list) != 3:
					contents_list = content.contents
		else:
			print(cinema_details.prettify())
			raise AttributeError("List size is not 2. Suppose to contain only phone number and contents.")

	except AttributeError:
		print(cinema_details.prettify())
		raise  AttributeError

def find_showtime_in_jakarta_cinemas():
	#Create BeatifulSoup Object with url link
	s = requests.get(url_cinemas_info, headers=headers)
	soup = bs4.BeautifulSoup(s.text, "html.parser")

	names, websites = [], []
	#Find cinemas with light colored labels (due to UI))
	for cinema_light in soup.find('table', class_='table-cinema').find_all('tr',class_="light"):
		find_jakarta_cinema(cinema_light, names, websites)
    #Find cinemas with dark colored labels (due to UI)
	for cinema_dark in soup.find('table', class_='table-cinema').find_all('tr',class_="dark"):
		find_jakarta_cinema(cinema_dark, names, websites)

    #Get showtimes for each cinemas
	for link, cinema_name in zip(websites,names):
		movies_showtimes = get_showtimes(link)
		print("Movies playing for " +  cinema_name + " :")
		for movie_showtime in movies_showtimes:
			print("Title: " + movie_showtime[0])
			for time in movie_showtime[1]:
				print(time + "   " + movie_showtime[2])

def my_scheduled_job():
    m = Movie(movie_title="movie " + str(timezone.now()))
    m.save()



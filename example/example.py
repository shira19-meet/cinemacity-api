import sys
sys.path.append('../')

from cinemacity import CinemaCity
from cinemacity import SITES

cinemaCity = CinemaCity('RO')
presentation = cinemaCity.get_presentation_for_site(SITES['RO']['IASI_IULIUS_MALL'])

cinema = presentation.sites[0]
print 'Cinema\n-----'
print 'Name: %s' % cinema.name
print 'Code: %s' % cinema.id
print 'Type: %s' % cinema.type

movies = cinema.movies
for movie in movies:
    print '\n%s\n-----' % movie.title
    for date, showings in movie.schedule.iteritems():
        print '%s: %s' % (date, ', '.join([showing.time for showing in showings]))

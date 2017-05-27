from itertools import groupby
from operator import attrgetter

from .mixin import StringMixin

class Presentation(StringMixin):
    def __init__(self, data):
        self.languages = data.get('languages')
        self.cached = data.get('cached')
        self.sites = map(Site, data.get('sites'))
        self.venueTypes = data.get('venueTypes')

class Site(StringMixin):
    def __init__(self, data):
        self.ticketsURL = data.get('tu')
        self.id = data.get('si')
        self.name = data.get('sn')
        self.type = data.get('vt')
        self.movies = map(Movie, data.get('fe'))

class Movie(StringMixin):
    def __init__(self, data):
        self.title = data.get('fn')
        self.ol = data.get('ol')
        self.code = data.get('dc')
        self.showings = sorted(map(Showing, data.get('pr')), key=attrgetter('date', 'time'))

    @property
    def schedule(self):
        return { k:list(v) for k, v in groupby(self.showings, key=attrgetter('date')) }

class Showing(StringMixin):
    def __init__(self, data):
        self.date = data.get('dt').split(' ')[0]
        self.time = data.get('tm')
        self.language = data.get('vt')
        self.subtitle = data.get('sb')

import requests

from .model import *

class CinemaCity():

    def __init__(self, country = 'ro'):
        self.country = country

    def get_presentation_for_site(self, siteId):
        '''
        Get presentation for specific cinema.
        '''
        return self.get_presentation({ 'subSiteId': siteId })

    def get_presentation(self, payload={}):
        '''
        Get presentation for all cinemas in country.
        '''
        response = requests.get(self.build_url('presentationsJSON'), params=payload)
        return Presentation(response.json())

    def build_url(self, endpoint):
        '''
        Get country specific url.
        '''
        return 'http://cinemacity.' + self.country + '/' + endpoint

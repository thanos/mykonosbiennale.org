from django.test import TestCase
from festival.models import Artist

NAME = 'Walter M. Watter'
class ArtImageNamersCase(TestCase):
    def setUp(self):
        Artist.objects.create(name = NAME, festival='2015')

    def test_headshotNamer(self):
        artist = Artist.objects.get(name=NAME)
        class A:
            name='Mary M.D Harek'
            festival = '2015 - Antidote & All'
        print headshotNamer(A(), 'X.jepg')


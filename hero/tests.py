from django.test import TestCase, Client
from .models import Hero

# Create your tests here.
class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batmman')
        Hero.objects.create(name='Ironman')
    
    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_hero_id(self):
        client = Client()
        response = client.get('/hero/10/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('10', response.content.decode())

    def test_visit_counter(self):
        client = Client()
        for i in ['1', '2']:
            response = client.get('/hero/')
            self.assertIn(i, response.content.decode())

from django.test import TestCase, Client

class Tests(TestCase):

    def test_d_less_than_zero(self):
        c = Client()
        response = c.get('/quadratic?a=1&b=2&c=3')
        self.assertEqual(response.json(), [])
    
    def test_d_equal_to_zero(self):
        c = Client()
        response = c.get('/quadratic?a=1&b=2&c=1')
        self.assertEqual(len(response.json()), 1)
    
    def test_d_greater_than_zero(self):
        c = Client()
        response = c.get('/quadratic?a=4&b=7&c=3')
        self.assertEqual(len(response.json()), 2)
    
    def test_roots(self):
        c = Client()
        response = c.get('/quadratic?a=1&b=6&c=0')
        self.assertEqual(response.json(), [0, -6])
# Gravity-web/app/tests/test_app.py

import unittest
from app.app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello, World!')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>About</h2>', response.data)

    def test_contact_get(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Contact</h2>', response.data)

    def test_contact_post(self):
        response = self.app.post('/contact', data={
            'name': 'John Doe',
            'message': 'Hello, this is a test message.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertIn(b'Your message has been sent successfully!', response.data)

    def test_contact_post_missing_fields(self):
        response = self.app.post('/contact', data={
            'name': '',
            'message': ''
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertIn(b'All fields are required!', response.data)

    def test_404_error(self):
        response = self.app.get('/nonexistentpage')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Page not found', response.data)

    def test_500_error(self):
        # To test this, you need to create a route that raises an exception
        # For the purpose of this example, we'll simulate it
        @app.route('/error')
        def error():
            raise Exception('This is a test error')

        response = self.app.get('/error')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Internal Server Error', response.data)

if __name__ == '__main__':
    unittest.main()

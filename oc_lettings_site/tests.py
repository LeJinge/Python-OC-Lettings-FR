from django.test import TestCase, Client


class TestErrorPages(TestCase):
    def setUp(self):
        self.client = Client()

    def test_404(self):
        response = self.client.get('/non_existent_route')
        self.assertEqual(response.status_code, 404)

    def test_500(self):
        with self.assertRaises(Exception) as context:
            self.client.get('/trigger-500/')
        self.assertTrue('Ceci est une erreur délibérée pour tester la gestion des erreurs 500.' in str(context.exception))

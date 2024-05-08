from django.test import TestCase, Client


class TestErrorPages(TestCase):
    def setUp(self):
        """
        Méthode de configuration pour les tests.

        Cette méthode est appelée avant chaque test. Elle initialise le client de test.
        """
        self.client = Client()

    def test_404(self):
        """
        Test pour la page d'erreur 404.

        Ce test fait une requête GET vers une URL non existante et vérifie que le code de statut de la réponse est 404.
        """
        response = self.client.get('/non_existent_route')
        self.assertEqual(response.status_code, 404)

    def test_500(self):
        """
        Test pour la page d'erreur 500.

        Ce test fait une requête GET vers une URL qui déclenche une erreur 500 et vérifie que l'erreur est bien levée.
        """
        with self.assertRaises(Exception) as context:
            self.client.get('/trigger-500/')
        self.assertTrue('Ceci est une erreur délibérée pour tester la gestion des erreurs 500.' in str(context.exception))

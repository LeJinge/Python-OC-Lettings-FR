"""
lettings/tests.py

Ce module contient les tests unitaires, d'intégration et fonctionnels pour l'application lettings.
"""

import unittest

from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from lettings.models import Address, Letting


# Create your tests here.
# ===================================================
# Tests Unitaires
# ===================================================

# Test unitaire pour les modèles Address et Letting
class AddressModelTest(TestCase):
    """
    Classe de tests pour le modèle Address.
    """
    def test_string_representation(self):
        """
        Teste la représentation sous forme de chaîne de caractères du modèle Address.
        """
        address = Address(
            number=123,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=90210,
            country_iso_code="USA"
        )
        self.assertEqual(str(address), "123 Main Street")

    def test_verbose_name_plural(self):
        """
        Teste le nom au pluriel du modèle Address dans le module administration.
        """
        field_label = Address._meta.verbose_name_plural
        self.assertEqual(field_label, 'Adresses')


class LettingModelTest(TestCase):
    """
    Classe de tests pour le modèle Letting.
    """
    def test_string_representation(self):
        """
        Teste la représentation sous forme de chaîne de caractères du modèle Letting.
        """
        address = Address(
            number=123,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=90210,
            country_iso_code="USA"
        )
        letting = Letting(title="Sample Letting", address=address)
        self.assertEqual(str(letting), "Sample Letting")


class LettingsIndexViewTest(TestCase):
    """
    Classe de tests pour la vue de l'index des lettings.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        number_of_lettings = 5
        for letting_num in range(number_of_lettings):
            address = Address.objects.create(
                number=letting_num,
                street="Main Street",
                city="City",
                state="ST",
                zip_code=10000 + letting_num,
                country_iso_code="USA"
            )
            Letting.objects.create(title=f'Letting {letting_num}', address=address)

    def test_view_url_exists_at_desired_location(self):
        """
        Teste si l'URL de la vue existe à l'emplacement souhaité.
        """
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Teste si l'URL de la vue est accessible par son nom.
        """
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Teste si la vue utilise le bon modèle.
        """
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/lettings_index.html')


class LettingDetailViewTest(TestCase):
    """
    Classe de tests pour la vue de détail d'un letting.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        address = Address.objects.create(
            number=1,
            street="Main Street",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="USA"
        )
        Letting.objects.create(title='Test Letting', address=address)

    def test_view_url_exists_at_desired_location(self):
        """
        Teste si l'URL de la vue existe à l'emplacement souhaité.
        """
        response = self.client.get('/lettings/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Teste si l'URL de la vue est accessible par son nom.
        """
        response = self.client.get(reverse('lettings:lettings_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Teste si la vue utilise le bon modèle.
        """
        response = self.client.get(reverse('lettings:lettings_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_404_on_nonexistent_letting(self):
        """
        Teste si une erreur 404 est renvoyée lorsqu'un letting inexistant est demandé.
        """
        response = self.client.get(reverse('lettings:lettings_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


# ===================================================
# Tests d'Intégration
# ===================================================

class LettingsIntegrationTest(TestCase):
    """
    Classe de tests d'intégration pour les lettings.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        # Créez des données initiales pour les tests
        cls.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="City",
            state="ST",
            zip_code=90210,
            country_iso_code="USA"
        )
        cls.letting = Letting.objects.create(title="Test Letting", address=cls.address)

    def setUp(self):
        """
        Méthode de configuration des tests.
        """
        self.client = Client()

    def test_lettings_index_view_displays_lettings(self):
        """
        Teste si la vue de l'index des lettings affiche les lettings.
        """
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")  # Vérifie si le listing est présent dans la réponse

    def test_letting_detail_view_displays_details(self):
        """
        Teste si la vue de détail d'un letting affiche les détails.
        """
        response = self.client.get(reverse('lettings:lettings_detail', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "123 Main Street")

    def test_nonexistent_letting(self):
        """
        Teste si une erreur est renvoyée lorsqu'un letting inexistant est demandé.
        """
        response = self.client.get(reverse('lettings:lettings_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


# ===================================================
# Tests Fonctionnels
# ===================================================

class LettingsFunctionalTest(unittest.TestCase):
    """
    Classe de tests fonctionnels pour les lettings.
    """
    @classmethod
    def setUpClass(cls):
        """
        Méthode de configuration de la classe de tests.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        """
        Méthode de nettoyage de la classe de tests.
        """
        cls.driver.quit()

    def test_lettings_workflow(self):
        """
        Teste le flux de travail des lettings.
        """
        # 1. J'arrive sur la page d'accueil
        self.driver.get("http://localhost:8000/")

        # Vérifier que l'accueil affiche correctement
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Lettings"))
        )

        # 2. J'accède à la page letting
        lettings_link = self.driver.find_element(By.LINK_TEXT, "Lettings")
        lettings_link.click()

        # Vérifier la présence des listings
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-group-item"))
        )

        # 3. Je clique sur le premier letting de la liste
        first_letting = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item a")
        first_letting.click()

        # 4. Je vérifie les données obtenues
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header-ui-title"))
        )
        title = self.driver.find_element(By.CLASS_NAME, "page-header-ui-title").text
        self.assertIn("Joshua Tree Green Haus /w Hot Tub", title)

        # Vérifier les détails de l'adresse
        details = self.driver.find_elements(By.CSS_SELECTOR, ".card-body p")
        address_details = [detail.text for detail in details]

        expected_details = [
            "7217 Bedford Street",
            "Brunswick, GA 31525",
            "USA",
        ]

        self.assertEqual(address_details, expected_details)


class AdminInterfaceTest(LettingsFunctionalTest):
    """
    Classe de tests pour l'interface d'administration.
    """
    def setUp(self):
        """
        Méthode de configuration des tests.
        """
        super().setUp()
        self.admin_url = "http://localhost:8000/admin/"

    def admin_login(self):
        """
        Méthode pour se connecter à l'interface d'administration.
        """
        self.driver.get(self.admin_url)
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        username_input.send_keys("admin")  # Remplacez par votre nom d'utilisateur admin
        password_input.send_keys("Abc1234")  # Remplacez par votre mot de passe admin
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def verify_admin_interface(self):
        """
        Méthode pour vérifier l'interface d'administration.
        """
        self.admin_login()

        # Vérifier la présence du texte "Adresses"
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Adresses")))
            address_link = self.driver.find_element(By.LINK_TEXT, "Adresses")
            self.assertIsNotNone(address_link)
        except TimeoutException:
            self.fail("Failed to find 'Adresses' link text")

        # Vérifier l'absence du texte "Addresss"
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.LINK_TEXT, "Addresss")


# Exécuter les tests uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()

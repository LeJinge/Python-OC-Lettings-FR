from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


# Create your tests here.
# ===================================================
# Tests Unitaires
# ===================================================
class ProfileModelTest(TestCase):
    """
    Classe de tests pour le modèle Profile.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        user = User.objects.create_user(username="TestUser", password="TestPassword")
        Profile.objects.create(user=user, favorite_city="TestCity")

    def test_profile_content(self):
        """
        Teste le contenu du modèle Profile.
        """
        profile = Profile.objects.get(id=1)
        expected_user = f'{profile.user}'
        expected_favorite_city = f'{profile.favorite_city}'
        self.assertEqual(expected_user, 'TestUser')
        self.assertEqual(expected_favorite_city, 'TestCity')


class ProfileViewTest(TestCase):
    """
    Classe de tests pour les vues de l'application profiles.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        user = User.objects.create_user(username="TestUser", password="TestPassword")
        Profile.objects.create(user=user, favorite_city="TestCity")

    def test_view_url_exists_at_desired_location(self):
        """
        Teste si l'URL de la vue existe à l'emplacement souhaité.
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Teste si l'URL de la vue est accessible par son nom.
        """
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Teste si la vue utilise le bon modèle.
        """
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles_index.html')


# ===================================================
# Tests d'Intégration
# ===================================================
class ProfilesIntegrationTest(TestCase):
    """
    Classe de tests d'intégration pour l'application profiles.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Méthode de configuration des données de test.
        """
        user = User.objects.create_user(username="TestUser", password="TestPassword")
        cls.profile = Profile.objects.create(user=user, favorite_city="TestCity")

    def setUp(self):
        """
        Méthode de configuration des tests.
        """
        self.client = Client()

    def test_profiles_index_view_displays_profiles(self):
        """
        Teste si la vue de l'index des profiles affiche les profiles.
        """
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")  # Vérifie si le profil est présent dans la réponse

    def test_profile_detail_view_displays_details(self):
        """
        Teste si la vue de détail d'un profil affiche les détails.
        """
        response = self.client.get(reverse('profiles:profile_detail', args=[self.profile.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")
        self.assertContains(response, "TestCity")

    def test_nonexistent_profile(self):
        """
        Teste si une erreur est renvoyée lorsqu'un profil inexistant est demandé.
        """
        response = self.client.get(reverse('profiles:profile_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


# ===================================================
# Tests Fonctionnels
# ===================================================
class ProfilesFunctionalTest(unittest.TestCase):
    """
    Classe de tests fonctionnels pour les profiles.
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

    def test_profiles_workflow(self):
        """
        Teste le flux de travail des profiles.
        """
        # 1. J'arrive sur la page d'accueil
        self.driver.get("http://localhost:8000/")

        # Vérifier que l'accueil affiche correctement
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Profiles"))
        )

        # 2. J'accède à la page profiles
        profiles_link = self.driver.find_element(By.LINK_TEXT, "Profiles")
        profiles_link.click()

        # Vérifier la présence des profiles
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-group-item"))
        )

        # 3. Je clique sur le profile "HeadlinesGazer"
        headlinesgazer_profile = self.driver.find_element(By.LINK_TEXT, "HeadlinesGazer")
        headlinesgazer_profile.click()

        # 4. Je vérifie les données obtenues
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header-ui-title"))
        )
        title = self.driver.find_element(By.CLASS_NAME, "page-header-ui-title").text
        self.assertIn("HeadlinesGazer", title)

        # 5. Je vérifie les détails du profile
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Jamie')]"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Lal')]"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'jssssss33@acee9.live')]"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Buenos Aires')]"))
        )

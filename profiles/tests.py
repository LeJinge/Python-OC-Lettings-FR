from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create your tests here.
# ===================================================
# Tests Unitaires
# ===================================================
class ProfileModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create(username="jdoe")
        profile = Profile.objects.create(user=user, favorite_city="Paris")
        self.assertEqual(str(profile), "jdoe")


class ProfilesIndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créez des données initiales pour les tests
        number_of_profiles = 5
        for i in range(number_of_profiles):
            user = User.objects.create(username=f'user{i}')
            Profile.objects.create(user=user, favorite_city="City")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles_index.html')


class ProfileDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="jdoe")
        cls.profile = Profile.objects.create(user=user, favorite_city="Paris")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[self.profile.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[self.profile.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_404_on_nonexistent_profile(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


# ===================================================
# Tests d'Intégration
# ===================================================
class ProfilesIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="jdoe")
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def setUp(self):
        self.client = Client()

    def test_profiles_index_view_displays_profiles(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "jdoe")

    def test_profile_detail_view_displays_details(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[self.profile.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "jdoe")
        self.assertContains(response, "Paris")

    def test_nonexistent_profile(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


# ===================================================
# Tests Fonctionnels
# ===================================================
class ProfilesFunctionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurez le navigateur pour les tests sans interface graphique
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_profiles_workflow(self):
        # 1. J'arrive sur la page d'accueil
        self.driver.get("http://localhost:8000/")

        # Naviguer vers la page Profiles
        profiles_link = self.driver.find_element(By.LINK_TEXT, "Profiles")
        profiles_link.click()

        # 2. Cliquer sur le premier lien HeadlinesGazer
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".list-group-item a"))
        )
        first_profile = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item a")
        first_profile.click()

        # 3. Vérifier les détails du profil HeadlinesGazer
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header-ui-title"))
        )
        title = self.driver.find_element(By.CLASS_NAME, "page-header-ui-title").text
        self.assertEqual(title, "HeadlinesGazer")

        details = self.driver.find_elements(By.CSS_SELECTOR, ".profile-detail p")
        details_text = [detail.text for detail in details]

        details = self.driver.find_elements(By.CSS_SELECTOR, ".card-body p")
        details_text = [detail.text for detail in details]

        expected_details = [
            "First name : Jamie",
            "Last name : Lal",
            "Email : jssssss33@acee9.live",
            "Favorite city : Buenos Aires",
        ]

        self.assertEqual(details_text, expected_details)


# Exécuter les tests uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()

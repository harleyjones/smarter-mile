from django.test import TestCase
from about.models import About

# Create your tests here.
class AboutTestCase(TestCase):
    def setUp(self):
        About.objects.create(
            title="John Doe",
            content="john@example.com",
            updated_on="2026, 3, 20, 15, 26, 33, 55533"
        )

    def test_about_instance(self):
        """Test that the About instance is created correctly"""
        about = About.objects.get(title="John Doe")
        self.assertEqual(about.content, "john@example.com")
        self.assertEqual(about.updated_on, "2026, 3, 20, 15, 26, 33, 55533")
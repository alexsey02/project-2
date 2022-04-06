import email
from msilib.schema import Class
from unicodedata import name
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password = 'Someadminpasword77',
        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email = 'user@test.com',
            password = 'Someuserpassword55',
            name = 'Test user full name',
        )
    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.accertContains(res , self.user.name)
        self.accertContains(res, self.user.email)
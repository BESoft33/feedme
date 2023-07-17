from django.test import TestCase
from .backends import EmailOrPhoneAuthentication
from django.contrib.auth import authenticate
from applications.user_handler.models import User


class EmailOrPhoneAuthenticationTest(TestCase):

    def setUp(self):
        # Create a test user with the specified email
        self.email = 'bhattarais009@gmail.com'
        self.password = 'testpassword'
        self.email_user = User.objects.create_user(
            email=self.email,
            password=self.password
        )

        # Create a test user with the specified email
        self.phone = '9803788148'
        self.phone_user = User.objects.create_user(
            phone=self.phone,
            password=self.password
        )

        
    #========================================================================
    # User creation Test
    def test_user_created_with_phone(self):
        self.assertIsNotNone(self.phone_user)

    def test_user_created_with_email(self):
        self.assertIsNotNone(self.email_user)
    #=========================================================================
    # User exists test
    def test_user_exists(self, email='bhattarais009@gmail.com'):
        user = User.objects.get(email = email)
        self.assertIsInstance(user, User)

    def test_phone_user_exists(self, phone='9803788148'):
        user = User.objects.get(phone=phone)
        self.assertIsInstance(user, User)
    
    #=========================================================================
    # Email Authentication credentials test

    def test_password_correct_email_incorrect(self):
        user = authenticate(email='bhattarais009@gmail.com', password= 'testpassword')
        self.assertIsNone(user)

    def test_password_correct_email_incorrect(self):
        user = authenticate(email='bhattarais@gmail.com', password= 'testpassword')
        self.assertIsNone(user)
    
    def test_password_incorrect_email_incorrect(self):
        user = authenticate(email='bhattarais@gmail.com', password='incorrect-password')
        self.assertIsNone(user)

    def test_password_correct_email_correct(self):
        user = authenticate(email='bhattarais009@gmail.com', password='testpassword')
        self.assertIsInstance(user, User)

    def test_password_email_not_provided(self):
        user = authenticate(email=None, password= 'incorrect_password')
        self.assertIsNone(user)

    def test_password_not_provided(self):
        user = authenticate(email='bhattarais009@gmail.com', password=None)
        self.assertIsNone(user)

    # ============================================================================
    # Phone Authentication credentials test

    def test_phone_correct_password_incorrect(self):
        user = authenticate(phone='9803788148', password='incorrect-password')
        self.assertIsNone(user)

    def test_phone_correct_password_correct(self):
        user = authenticate(phone='9803788148', password='testpassword')
        self.assertIsInstance(user, User)

    def test_phone_incorrect_password_correct(self):
        user = authenticate(phone='9866045808', password='testpassword')
        self.assertIsNone(user)

    def test_phone_incorrect_password_incorrect(self):
        user = authenticate(phone='9866045808', password='incorrect-password')
        self.assertIsNone(user)
    
    # ================================================================================
    # Test User Role
    def test_user_is_staff(self):
        user = User.objects.get(phone='9803788148')
        is_staff = user.is_staff
        self.assertFalse(is_staff)



from django.test import TestCase
from django.urls import reverse
from website.models import Customer, Product, Order, OrderDetails


class WebsiteViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.test_user = Customer.objects.create_user(
            username='testuser@gmail.com', email='test@example.com', password='testpassword')

        # Create some test products
        self.product1 = Product.objects.create(
            name_en='Product 1', name_ar='منتج 1', unit_price=10.0, stock_quantity=100)
        self.product2 = Product.objects.create(
            name_en='Product 2', name_ar='منتج 2', unit_price=20.0, stock_quantity=50)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/login.html')

    def test_store_view(self):
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/store.html')

    def test_cart_view_unauthenticated(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/cart.html')
        self.assertEqual(len(response.context['items']), 0)

    def test_cart_view_authenticated(self):
        self.client.login(
            username='testuser@gmail.com@gmail.com', password='testpassword')
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/cart.html')

    def test_checkout_view(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/store.html')

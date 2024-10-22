from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuItemSerializer  # Adjust the import based on your app structure


class MenuItemViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.menu_item = MenuItem.objects.create(title="Test Dish", description="Delicious test dish", price=10.99, inventory=100)

    def test_menu_item_list(self):
        response = self.client.get(reverse('menuitem-list'))  # Update with your actual URL name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        data = {
            "title": "New Dish",
            "description": "Tasty new dish",
            "price": 12.99,
            "inventory": 50
        }
        response = self.client.post(reverse('menuitem-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_menu_items(self):
        # Create additional menu items for testing
        MenuItem.objects.create(title="Pizza", description="Cheesy pizza", price=8.99, inventory=20)
        MenuItem.objects.create(title="Burger", description="Juicy burger", price=9.99, inventory=30)

        response = self.client.get(reverse('menuitem-list'))  # Update with your actual URL name

        # Serialize the data to compare with the response
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class BookingViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_booking(self):
        data = {
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "phone_number": "1234567890",
            "booking_date": "2024-10-22",
            "number_of_people": 4,
            "special_requests": "None"
        }
        response = self.client.post(reverse('booking-list'), data, format='json')  # Update with your actual URL name
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

from django.test import TestCase
from .models import MenuItem, Booking

class MenuItemModelTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Test Dish", description="Delicious test dish", price=10.99, inventory=100)

    def test_get_item(self):
        item = MenuItem.objects.get(title="Test Dish")
        self.assertEqual(item.get_item(), "Test Dish : 10.99")

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(
            customer_name="John Doe",
            customer_email="john@example.com",
            phone_number="1234567890",
            booking_date="2024-10-22",
            number_of_people=4,
            special_requests="None"
        )

    def test_str_representation(self):
        booking = Booking.objects.get(customer_name="John Doe")
        self.assertEqual(str(booking), "Booking for John Doe on 2024-10-22 00:00")

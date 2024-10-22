from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    booking_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date.strftime('%Y-%m-%d %H:%M')}"
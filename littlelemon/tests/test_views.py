from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):

    def setUp(self) -> None:
        Menu.objects.create(Id = 1, Title = 'Check1', Price = 123, Inventory = 311)
        Menu.objects.create(Id = 2, Title = 'check2', Price = 342.65, Inventory = 23)
        return super().setUp()
    
    def test_getall(self):
        obj = Menu.objects.all()
        ser = MenuSerializer(obj, many=True)
        self.assertEqual(ser.data[1]['Inventory'], 23)
        

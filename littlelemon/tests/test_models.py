from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):

    def test_get_item_from_menu_model(self):
        #with self.assertRaises(Exception):
        obj = Menu.objects.create(Id = 1, Title = 'Check', Price = 456.5, Inventory = 111)
        #print(str(obj))
        self.assertEqual(obj.Price, 456.5)
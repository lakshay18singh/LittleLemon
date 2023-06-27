from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):

    def setUp(self) -> None:
        Menu.objects.create(Id = 1, Title = 'Check', Price = 456.5, Inventory = 111)
        return super().setUp()

    def test_check_Price_can_be_float(self):
        obj = Menu.objects.all()
        #print(obj[0])
        #self.assert_(True)
        self.assertEqual(obj[0].Price, 456.5)

    def test_the_str_method(self):
        obj = Menu.objects.all()
        self.assertEqual(str(obj[0]), 'Check : 456.50')
        self.assert_(True)
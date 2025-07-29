from rest_framework.test import APITestCase
from rest_framework import status
from .models import Menu
import logging

logging.disable(logging.ERROR)


class MenuAPITest(APITestCase):

    def setUp(self):
        pass

    def test_create_menu_item(self):
        """
        Asegura que podemos crear un nuevo elemento de menú.
        """
        data = {'name': 'Pizza Margherita',
                'description': 'Clásica pizza con tomate y mozzarella',
                'status': True}
        response = self.client.post('/api/food-drinks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().name, 'Pizza Margherita')
        self.assertEqual(response.data['status'], True)

    def test_create_menu_item_missing_name(self):
        """
        Asegura que no podemos crear un elemento de menú sin name.
        """
        data = {'description': 'Bebida carbonatada', 'status': True}
        response = self.client.post('/api/food-drinks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data['detail'])
        self.assertEqual(response.data['detail']['name'][0],
                         'This field is required.')

    def test_get_all_menu_items(self):
        """
        Asegura que podemos obtener todos los elementos del menú.
        """
        Menu.objects.create(name='Café Espresso', status=True)
        Menu.objects.create(name='Té Chai', status=False)
        response = self.client.get('/api/food-drinks/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Café Espresso')
        self.assertEqual(response.data[1]['name'], 'Té Chai')

    def test_get_menu_item_by_id(self):
        """
        Asegura que podemos obtener un elemento de menú por su ID.
        """
        item = Menu.objects.create(name='Ensalada César', status=True)
        response = self.client.get(f'/api/food-drinks/{item.id}/',
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Ensalada César')

    def test_get_menu_item_not_found(self):
        """
        Asegura que obtenemos 404 si el elemento de menú no existe.
        """
        response = self.client.get('/api/food-drinks/123/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_update_menu_item(self):
        """
        Asegura que podemos actualizar un elemento de menú existente por id.
        """
        item = Menu.objects.create(name='Pasta Carbonara', status=True)
        updated_data = {'name': 'Pasta Carbonara Vegana', 'status': False}
        response = self.client.put(f'/api/food-drinks/{item.id}/',
                                   updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, 'Pasta Carbonara Vegana')
        self.assertFalse(item.status)
        self.assertEqual(response.data['status'], False)

    def test_delete_menu_item(self):
        """
        Asegura que podemos eliminar un elemento de menú por id.
        """
        item = Menu.objects.create(name='Sopa de Verduras', status=True)
        response = self.client.delete(f'/api/food-drinks/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)

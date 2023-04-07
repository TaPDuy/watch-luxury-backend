from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from watchLuxuryAPI.utils import response_code as rescode
from users.models import User
from users.serializers import UserSerializer
from products.models import Product
from products.serializers import ProductSerializer

from .models import Favorite
from .serializers import FavoriteSerializer


DATA_TEST_MSG = 'Incorrect return data'
API_CODE_TEST_MSG = 'Incorrect API response code'
HTTP_CODE_TEST_MSG = 'Incorrect response code'

client = APIClient()
client.force_authenticate(user=User.objects.get(username='admin'))


class FavoritesTestCase(TestCase):

    # ----- Get favorite -----
    def test_get_user_favorite_products(self):
        response = client.get(reverse('favorite_products', kwargs={'id': 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS, API_CODE_TEST_MSG)
        
        user = User.objects.get(pk=2)
        serializer = ProductSerializer(user.favorites, many=True)
        
        self.assertEqual(response.data['data'], serializer.data, DATA_TEST_MSG)


    def test_get_user_favorite_products_failed(self):
        response = client.get(reverse('favorite_products', kwargs={'id': 3})) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_NOT_FOUND, API_CODE_TEST_MSG)


    def test_get_product_favorited_users(self):
        response = client.get(reverse('favorite_users', kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS, API_CODE_TEST_MSG)
        
        product = Product.objects.get(pk=1)
        serializer = UserSerializer(product.favorited_by, many=True)
        
        self.assertEqual(response.data['data'], serializer.data, DATA_TEST_MSG)


    def test_get_product_favorited_users_fail(self):
        response = client.get(reverse('favorite_users', kwargs={'id': 69})) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_NOT_FOUND, API_CODE_TEST_MSG)


    def test_get_all_favorites(self):
        response = client.get(reverse('favorite'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS)

        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many=True)

        self.assertEqual(response.data['data'], serializer.data)


    def test_get_favorites_by_user(self):
        response = client.get(reverse('favorite') + '?user=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS)
        
        favorites = Favorite.objects.filter(user=2)
        serializer = FavoriteSerializer(favorites, many=True)

        self.assertEqual(response.data['data'], serializer.data)


    def test_get_favorites_by_product(self):
        response = client.get(reverse('favorite') + '?product=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS)
        
        favorites = Favorite.objects.filter(product=2)
        serializer = FavoriteSerializer(favorites, many=True)

        self.assertEqual(response.data['data'], serializer.data)


    def test_get_favorites_by_user_and_product(self):
        response = client.get(reverse('favorite') + '?user=2&product=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS)
        
        favorites = Favorite.objects.filter(user=2, product=2)
        serializer = FavoriteSerializer(favorites, many=True)

        self.assertEqual(response.data['data'], serializer.data)
    

    # ----- Add favorite -----
    def test_add_favorite(self):
        response = client.post(reverse('favorite'), {
            'user': 1,
            'product': 2
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS, API_CODE_TEST_MSG)

        favorite = Favorite.objects.filter(user=1, product=2)
        self.assertNotEqual(favorite.count(), 0, "Data wasn't added")
        
        self.assertEqual(response.data['data'], FavoriteSerializer(favorite.first()).data, DATA_TEST_MSG)


    def test_add_favorite_not_found(self):
        response = client.post(reverse('favorite'), {
            'user': 1,
            'product': 6
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_NOT_FOUND, API_CODE_TEST_MSG)


    def test_add_favorite_already_added(self):
        response = client.post(reverse('favorite'), {
            'user': 1,
            'product': 2
        }, format='json')
        response = client.post(reverse('favorite'), {
            'user': 1,
            'product': 2
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_GENERIC_ERROR, API_CODE_TEST_MSG)


    # ----- Remove favorite -----
    def test_remove_favorite(self):
        response = client.delete(reverse('favorite'), {
            'user': 2,
            'product': 2
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_SUCCESS, API_CODE_TEST_MSG)

        favorite = Favorite.objects.filter(user=2, product=2)
        self.assertEqual(favorite.count(), 0, "Data wasn't removed")
        

    def test_remove_favorite_not_found(self):
        response = client.delete(reverse('favorite'), {
            'user': 1,
            'product': 6
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_NOT_FOUND, API_CODE_TEST_MSG)


    def test_remove_favorite_already_removed(self):
        response = client.delete(reverse('favorite'), {
            'user': 2,
            'product': 2
        }, format='json')
        response = client.delete(reverse('favorite'), {
            'user': 2,
            'product': 2
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, HTTP_CODE_TEST_MSG)
        self.assertEqual(response.data['code'], rescode.API_GENERIC_ERROR, API_CODE_TEST_MSG)


    # ----- Setup & Teardown -----
    def setUp(self) -> None:
        User.objects.create(
            username='person_1',
            first_name='Person',
            last_name='1',
            email='person1@gmail.com',
            address="Person 1's place",
            phone_number='0123456789'
        )
        User.objects.create(
            username='person_2',
            first_name='Person',
            last_name='2',
            email='person2@gmail.com',
            address="Person 2's place",
            phone_number='0123456789'
        )

        Product.objects.create(
            name='Product 1',
            description="Product 1's descriptions",
            brand="Brand",
            image="/media/products/-piaget-altiplano-g0a44112-manual-watch-956.jpg",
            price=100000
        )
        Product.objects.create(
            name='Product 2',
            description="Product 2's descriptions",
            brand="Brand",
            image="/media/products/-piaget-altiplano-g0a44112-manual-watch-956.jpg",
            price=200000
        )
        Product.objects.create(
            name='Product 3',
            description="Product 3's descriptions",
            brand="Brand",
            image="/media/products/-piaget-altiplano-g0a44112-manual-watch-956.jpg",
            price=300000
        )

        Favorite.objects.create(
            user=User.objects.get(pk=1),
            product=Product.objects.get(pk=1)
        )
        Favorite.objects.create(
            user=User.objects.get(pk=2),
            product=Product.objects.get(pk=1)
        )
        Favorite.objects.create(
            user=User.objects.get(pk=2),
            product=Product.objects.get(pk=2)
        )
        Favorite.objects.create(
            user=User.objects.get(pk=2),
            product=Product.objects.get(pk=3)
        )
    

    def tearDown(self) -> None:
        pass

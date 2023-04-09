from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from watchLuxuryAPI.utils import response_code as rescode

from .models import User
from .serializers import UserSerializer


client = APIClient()


class GetUsersTestCase(TestCase):

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
    
    def tearDown(self) -> None:
        pass
    
    def test_get_all_users(self):
        response = client.get(reverse('users'))

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        self.assertEqual(response.data['data'], serializer.data, 'Mismatch return data')
        self.assertEqual(response.data['code'], rescode.API_SUCCESS, 'Processing failed')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Request unsuccessful')

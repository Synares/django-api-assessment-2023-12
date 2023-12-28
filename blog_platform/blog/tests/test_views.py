from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import PostFactory


class PostListCreateViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='jasim', password='12345')
        token_url = reverse('api_token_auth')
        response = self.client.post(token_url, {'username': 'jasim', 'password': '12345'})
        self.token = response.data['token']

        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token

        self.url = reverse('post-list-create')

    def test_get_list_of_posts(self):
        PostFactory.create_batch(3, author=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_post(self):
        post_data = {
            'title': 'Valid Title',
            'content': 'This is some valid content.',
            'author': self.user.id
        }
        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], post_data['title'])
        self.assertEqual(response.data['content'], post_data['content'])
        self.assertEqual(response.data['author'], post_data['author'])

from django.test import TestCase

from .factories import PostFactory, UserFactory
from ..serializers import PostSerializer


class TestPostSerializer(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.post = PostFactory.create(author=self.user)

    def test_post_serializer_valid_data(self):
        post_serializer = PostSerializer(self.post)
        post_serialized_data = post_serializer.data
        self.assertEqual(post_serialized_data.get('title'), self.post.title)
        self.assertEqual(post_serialized_data.get('content'), self.post.content)
        self.assertEqual(post_serialized_data.get('author'), self.post.author.id)

    def test_post_serializer_invalid_data(self):
        invalid_data = {
            'title': 'Hi',
            'content': 'Testing',
            'author': self.user.id
        }

        serializer = PostSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

        self.assertIn('title', serializer.errors)
        self.assertEqual(serializer.errors['title'][0], "Title must be at least 5 characters long.")
        self.assertIn('content', serializer.errors)
        self.assertEqual(serializer.errors['content'][0], "Content must be at least 10 characters long.")

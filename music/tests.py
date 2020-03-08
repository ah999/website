from django.test import TestCase
from .models import Album
class PostModelTest(TestCase):
    def setUp(self):
        Album.objects.create(text='just a test')
    def test_text_content(self):
        album=Album.objects.get(id=1)
        expected_object_name = f'{album.text}'
        self.assertEqual(expected_object_name, 'just a test')

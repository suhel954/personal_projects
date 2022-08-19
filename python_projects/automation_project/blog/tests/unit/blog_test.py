from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b1 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b1.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_post(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b1 = Blog('My Day', 'Rolf')
        b1.posts = ['test', 'another']

        self.assertEqual(b.__repr__(),'Test by Test Author (1 post)')
        self.assertEqual(b1.__repr__(), 'My Day by Rolf (2 posts)')


 
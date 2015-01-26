from step07.tutorial.views import WikiViews

__author__ = 'josip'

import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from tutorial.views import hello_world

        request = testing.DummyRequest()
        inst = WikiViews(request)
        response = inst.wiki_view()
        self.assertEqual(response['title'], 'Welcome to the Wiki')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        settings = {}
        app = main(settings)
        from webtest import TestApp
        self.testApp = TestApp(app)

    def testIt(self):
        res = self.testApp.get('/', status=200)
        self.assertIn(b'Welcome', res.body)
        res = self.testApp.get('/add', status=200)
        self.assertIn(b'Add Wiki Page', res.body)
        res = self.testApp.get('/100', status=200)
        self.assertIn(b'100', res.body)
        res = self.testApp.get('/100/edit', status=200)
        self.assertIn(b'Edit', res.body)
        res = self.testApp.get('/100/delete', status=302)
        self.assertIn(b'Found', res.body)


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
        response = hello_world(request)
        self.assertEqual(response["title"], "Hello World")


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        settings = {}
        app = main(settings)
        from webtest import TestApp
        self.testApp = TestApp(app)

    def testIt(self):
        res = self.testApp.get("/", status=200)
        self.assertIn(b"Hello", res.body)


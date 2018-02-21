from django.test import TestCase

# Create your tests here.
import unittest
from django.test import Client
import json

class HelloWorldViewTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        key="msg"
        value ="hello-world"
        key2 = "msg2"
        value2 = "hello-world2"

        request_dict = {key:value,key2:value2}
        response = self.client.get('/api/v1/echo/',request_dict)
        self.assertEqual(response.status_code, 200)
        resp_dict = json.loads(response.content) 

        self.assertEqual(resp_dict, request_dict)


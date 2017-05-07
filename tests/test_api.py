#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = 'Florents Tselai'

import json

import requests

LOCAL_HOST = "http://localhost:5000"

import unittest


class ApiResponseCase(unittest.TestCase):

    def setUp(self):
        self.car_req = requests.get(LOCAL_HOST + "/api/car/" + "7991175")

    def test_car_api(self):
        car_dict = json.loads(self.car_req.text)

        self.assertEqual(car_dict['bhp'], 120)
        self.assertEqual(car_dict['engine'], 1600)
        self.assertEqual(len(car_dict['images']), 58)
        self.assertEqual(car_dict['postal_code'], 73100)

if __name__ == '__main__':
    unittest.main()

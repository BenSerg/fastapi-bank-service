import unittest
from fastapi.testclient import TestClient
from main import app


class TestCalculateEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_valid_calculate(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 12,
            "amount": 10000,
            "rate": 5.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_invalid_periods_low(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 0,
            "amount": 10000,
            "rate": 5.0
        })
        self.assertEqual(response.status_code, 422)

    def test_invalid_periods_high(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 61,
            "amount": 10000,
            "rate": 5.0
        })
        self.assertEqual(response.status_code, 422)

    def test_invalid_amount_low(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 12,
            "amount": 5000,
            "rate": 5.0
        })
        self.assertEqual(response.status_code, 422)

    def test_invalid_amount_high(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 12,
            "amount": 1000001,
            "rate": 5.0
        })
        self.assertEqual(response.status_code, 422)

    def test_invalid_rate_low(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 12,
            "amount": 10000,
            "rate": 0
        })
        self.assertEqual(response.status_code, 422)

    def test_invalid_rate_high(self):
        response = self.client.post("/calculate", json={
            "date": "01.01.2023",
            "periods": 12,
            "amount": 10000,
            "rate": 9
        })
        self.assertEqual(response.status_code, 422)

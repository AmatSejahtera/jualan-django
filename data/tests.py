from django.test import TestCase


class DataPageTests(TestCase):
    def test_barang_page_loads(self):
        response = self.client.get('/barang/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Halaman Beranda')

    def test_products_page_loads(self):
        response = self.client.get('/barang/products/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Halaman Product')

    def test_customer_page_loads(self):
        response = self.client.get('/barang/customer/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Halaman Customer')

import unittest

from kelvin_rizky_app import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_total_harga_barang(self):
        self.shopping_cart = ShoppingCart() # Membuat variabel penampung fungsi ShoppingCart
        self.shopping_cart.MenambahBarang() # Menambahkan barang "Ayam" dengan harga 30000
        self.shopping_cart.MenambahBarang() # Menambahkan barang "Sapi" dengan harga 50000
        TotalHarga = self.shopping_cart.TotalHargaBarang() # Membuat variabel untuk menampung 
                                                           # fungsi TotalHargaBarang untuk 
                                                           # menjumlahkan harga pada barang-barang belanja
        self.assertEqual(TotalHarga, 80000)


if __name__ == "__main__":
    # cara running test
    unittest.main()

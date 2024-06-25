'''
=================================================
Graded Challenge 1

Nama  : Kelvin Rizky Novsa
Batch : RMT-028

Program Shopping Cart adalah program yang dibuat untuk user 
(atau dalam hal ini customer) untuk dapat menambahkan barang yang akan dibeli,
menghapus barang yang akan dibeli, melihat barang-barang di keranjang yang akan
dibeli, dan menjumlahkan total harga barang yang akan dibeli.
=================================================
'''

class CartItem:
  '''
    class CartItem bertujuan untuk membuat objek keranjang 
    belanja customer yang ingin berbelanja di Toko.
 '''
  def __init__(self,name,price):
    '''
    fungsi ini dibuatkan untuk mendefinisikan nama dan harga barang belanja
    setiap customer di Toko.

    Contoh penggunaan :
    CartItem1 = CartItem("Ayam", 10000)
    print(CartItem1)

    Output = "Ayam", 10000
    '''
    self.name = name
    self.price = price


class ShoppingCart:
  '''
    class ShoppingCart bertujuan untuk merepresentasikan keranjang belanja
    yang ada di toko.
  '''
  def __init__(self):
    '''
    fungsi ini bertujuan hanya untuk membuat list barang yang berguna 
    sebagai penampung data yang diinput user ketika ingin berbelanja.
    kemudian adanya self total bertujuan sebagai penampung nilai total harga 
    belanja yang ada di keranjang di fungsi TotalHargaBarang.

    Contoh  :
    listBarang = ["Ayam", 30000, "Sapi", 50000]
    Total Harga = 60000
    self.total = 60000
    '''
    self.listBarang = []
    self.total = 0

  def MenambahBarang(self):
    '''
    fungsi ini bertujuan untuk menambahkan barang berserta harga barang
    di dalam keranjang. Kemudian data tersebut disimpan kedalam list barang 
    
    Contoh Output  :
    Masukkan nama barang : Ayam
    Masukkan harga : 30000
    Barang (Ayam), sudah disimpan dalam keranjang

    '''
    name = input("Masukkan nama barang : ")
    price = input("Masukkan harga: ")

    barangUpdate = CartItem(name,price)
    print(f'Barang "{name}", sudah disimpan dalam keranjang')
    return self.listBarang.append(barangUpdate)
    
  def LihatItem(self):
     '''
    fungsi ini bertujuan untuk melihat barang ataupun barang-barang berserta
    dengan harga yang akan dibeli oleh customer yang sudah diinput di dalam 
    fungsi Menambahkan Barang

    Contoh Output : 
    Barang di keranjang :
    1. Ayam - 30000
    2. Ikan - 20000
     
     '''
     print('Barang di keranjang\n')
     for index, item in enumerate(self.listBarang):
        print(f'{index + 1}. {item.name} - {item.price}')  

  def MembuangBarang(self):
    '''
    fungsi ini bertujuan untuk membuang nama barang yang ada dikeranjang

    Contoh Output : 
    Barang di keranjang :
    1. Ayam - 30000
    2. Ikan - 20000
    
    Masukkan nama barang yang akan dihapus : Ayam
    Barang Ayam berhasil dihapus di keranjang belanja
    
    '''
    self.LihatItem()
    buangBarang = input("Masukkan nama barang yang ingin dihapus : ")
    

    for item in self.listBarang:
       if item.name == buangBarang:
          self.listBarang.remove(item)
          print (f'Barang "{buangBarang}" berhasil dihapus di keranjang belanja.')
          break

  def TotalHargaBarang(self):
     '''
     fungsi ini bertujuan untuk menjumlah harga barang yang ada di keranjang
     belanja

    Contoh Output : 
    Total Harga: 50000
     '''
     TotalHarga = 0
     ubahData = 0
     for item in self.listBarang:
        ubahData = int(item.price)
        TotalHarga += ubahData
     self.total = TotalHarga
     return self.total
    
        
  def main(self):
    '''
    fungsi ini bertujuan untuk menampilkan interface menu didalam terminal
    kepada user (customer) untuk dapat berbelanja sesuai dengan barang dan harga
    yang diinput
    '''
    while True:
    
        print("Selamat Datang di Keranjang Belanja Toko Kelvin Jaya")
        print("\n")

        print("Menu : \n1. Menambahkan Barang\n2. Hapus Barang\n3. Tampilkan Barang di Keranjang\n4. Lihat Total Belanja\n5. Exit")
        print("\n\n")
        selectedMenu = input('Pilihan: ')


        if selectedMenu == '1':
            self.MenambahBarang()
        
        elif selectedMenu == '2':
            self.MembuangBarang()
        
        elif selectedMenu == '3':
            self.LihatItem()

        elif selectedMenu == '4':
            self.TotalHargaBarang()
            print('Total belanja : ', self.total)
    
        elif selectedMenu == '5':
            print('Sampai Jumpa! Terima kasih sudah belanja di Toko Kelvin!')
            break

        else:
            print("Pilihannya salah. Coba lagi ya.")



if __name__ == "__main__": # menambahkan idiom agar program hanya dapat dijalan di file dimana program dibuat
    listBaru = ShoppingCart() # Menampung fungsi shopping cart
    listBaru.main() # Digunakan untuk menampilkan interface menu untuk user


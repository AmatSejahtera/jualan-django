# Dokumentasi Project Jualan

## 1. Gambaran umum

Project ini adalah aplikasi web sederhana menggunakan Django. Aplikasi memiliki halaman dashboard, produk, dan customer. Saat ini halaman-halaman tersebut masih berupa kerangka tampilan; belum ada model data produk/customer atau proses pengelolaan data melalui database yang didefinisikan di aplikasi `data`.

## 2. Struktur folder dan file

```text
jualan/
├── manage.py
├── db.sqlite3
├── README.md
├── jualan/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── data/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        └── data/
            ├── customer.html
            ├── dashboard.html
            ├── main.html
            ├── navbar.html
            └── products.html
```

### Folder dan file utama

- **`manage.py`** — pintu masuk untuk menjalankan perintah Django, seperti menjalankan server lokal, tes, dan migrasi database.
- **`db.sqlite3`** — file database SQLite yang digunakan project. File ini dapat menyimpan data aplikasi dan tidak sebaiknya dibagikan jika berisi data pribadi.
- **`jualan/`** — konfigurasi inti project Django.
  - **`__init__.py`** — menandai folder sebagai package Python.
  - **`settings.py`** — pengaturan project, termasuk aplikasi terpasang, middleware, template, database, bahasa, zona waktu, dan konfigurasi file statis. Konfigurasi saat ini memakai SQLite dan mengaktifkan mode debug untuk pengembangan.
  - **`urls.py`** — URL utama project. URL admin diarahkan ke Django Admin, sedangkan URL lainnya diteruskan ke `data.urls`.
  - **`asgi.py`** — titik masuk untuk menjalankan aplikasi melalui server ASGI.
  - **`wsgi.py`** — titik masuk untuk menjalankan aplikasi melalui server WSGI.
- **`data/`** — aplikasi Django yang menampung halaman dan fitur jualan.
  - **`__init__.py`** — menandai folder sebagai package Python.
  - **`apps.py`** — konfigurasi identitas aplikasi `data`.
  - **`models.py`** — tempat mendefinisikan struktur data/tabel. Saat ini belum ada model aplikasi yang didefinisikan.
  - **`views.py`** — menyiapkan respons halaman. `home` menampilkan dashboard, `product` menampilkan halaman produk, dan `customer` menampilkan halaman customer.
  - **`urls.py`** — menghubungkan alamat halaman aplikasi ke fungsi di `views.py`.
  - **`admin.py`** — tempat mendaftarkan model agar dapat dikelola melalui Django Admin. Saat ini belum ada model yang didaftarkan.
  - **`tests.py`** — berisi tes untuk memeriksa respons halaman. Alamat yang diuji saat ini belum sesuai dengan konfigurasi URL aplikasi.
  - **`migrations/`** — tempat Django menyimpan riwayat perubahan struktur database. Saat ini hanya terdapat `__init__.py`; belum ada file migrasi untuk model aplikasi.
  - **`templates/data/`** — berisi template HTML yang digunakan untuk menampilkan halaman.
    - **`main.html`** — kerangka HTML utama dan blok `content` yang dapat diisi template turunan.
    - **`navbar.html`** — berisi kerangka/penanda navbar, tetapi belum digunakan atau dipanggil dari template lain.
    - **`dashboard.html`** — disiapkan sebagai template dashboard, tetapi saat ini kosong.
    - **`products.html`** — template halaman produk; mewarisi `main.html` dan menampilkan nilai `title`.
    - **`customer.html`** — template halaman customer; mewarisi `main.html` dan menampilkan nilai `title`.

## 3. Alur kerja aplikasi

1. Pengguna membuka alamat aplikasi di browser.
2. Django menerima permintaan melalui konfigurasi URL utama pada `jualan/urls.py`.
3. Untuk halaman selain admin, Django meneruskan permintaan ke daftar URL dalam `data/urls.py`.
4. `data/urls.py` memilih fungsi yang sesuai di `data/views.py`:
   - `/` → `home`
   - `/products/` → `product`
   - `/customer/` → `customer`
5. Fungsi view menyiapkan context, termasuk judul halaman, lalu meminta Django merender template HTML.
6. Template halaman dapat mewarisi kerangka `main.html`, lalu Django mengirimkan hasil HTML kepada browser.

Alamat admin tersedia pada `/admin/`. Fungsinya berasal dari Django Admin bawaan.

## 4. Alur data saat ini

- Belum ada model khusus untuk produk maupun customer pada `data/models.py`.
- Belum ada proses create, read, update, atau delete (CRUD) yang terlihat pada aplikasi `data`.
- Database SQLite telah dikonfigurasi pada `settings.py`; keberadaan database belum berarti data produk/customer sudah terhubung dengan halaman.
- Tampilan template saat ini masih berupa kerangka dan judul, bukan daftar data yang berasal dari database.

## 5. Cara menjalankan project

1. Buka terminal pada folder utama project.
2. Pastikan Python dan Django yang dibutuhkan project tersedia di lingkungan pengembangan.
3. Jalankan server pengembangan dengan perintah `python manage.py runserver`.
4. Buka alamat lokal yang ditampilkan oleh Django di terminal, biasanya `http://127.0.0.1:8000/`.
5. Untuk membuka halaman yang tersedia, gunakan alamat root, `/products/`, atau `/customer/`. Halaman admin tersedia di `/admin/` jika akun admin sudah disiapkan.

## 6. Kondisi dan catatan yang perlu diperhatikan

- **Template produk tidak cocok dengan nama file yang tersedia.** View `product` meminta template `data/product.html`, sedangkan file yang ada bernama `data/products.html`. Karena itu halaman `/products/` berpotensi gagal dirender sampai nama template dan pemanggilannya diselaraskan.
- **Template dashboard kosong.** View `home` mengirim judul ke `data/dashboard.html`, tetapi file tersebut belum berisi markup untuk menampilkan judul atau konten.
- **Alamat pada tes tidak cocok dengan URL saat ini.** Tes meminta `/barang/`, `/barang/products/`, dan `/barang/customer/`, sementara URL yang dikonfigurasi adalah `/`, `/products/`, dan `/customer/`. Tes juga mengharapkan teks “Halaman Beranda”, yang belum tampak pada template dashboard saat ini.
- **Navbar belum dipakai.** File `navbar.html` tersedia, tetapi kerangka `main.html` belum memasukkannya.
- **Belum ada migrasi model aplikasi.** Folder migrations belum memuat perubahan struktur database untuk model aplikasi `data`.
- **Pengaturan keamanan masih untuk pengembangan.** Mode debug aktif dan secret key pengembangan tersimpan di pengaturan. Jangan menyalin atau membagikan nilai secret key; sebelum deployment, gunakan secret yang dikelola secara aman dan pengaturan produksi yang sesuai.

Catatan di atas menjelaskan kondisi file yang tersedia saat dokumentasi dibuat; dokumentasi ini tidak mengubah kode aplikasi.

## 7. Ringkasan

Project sudah memiliki kerangka Django, konfigurasi database SQLite, pemetaan URL, tiga fungsi view, dan beberapa template halaman. Alur dasarnya adalah **URL → view → template → respons browser**. Fitur pengelolaan data belum diimplementasikan, dan beberapa ketidaksesuaian di bagian catatan perlu dibereskan agar semua halaman serta tes berjalan sesuai harapan.

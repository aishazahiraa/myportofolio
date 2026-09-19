Nama : Aisha Ibnaty Zahira

NPM : 2506624726

Kelas : PBP C

Latihan branch Git

### Tugas 1

1. Pada website ini saya menggunakan elemen semantik HTML5 seperti `<section>` untuk memisahkan bagian About Me dan Experience. Penggunaan `<section>` membantu membuat struktur HTML menjadi lebih jelas karena setiap bagian halaman memiliki isi dan fungsi yang berbeda. sehingga website tidak akan terlihat sangat menumpuk dan berantakan. Selain itu, kode juga menjadi lebih mudah dibaca dan diatur.

2. Ketika mengatur CSS agar website tetap responsive, saya cukup kesulitan
dalam menyesuaikan warna dan layout. Beberapa kali warna yang sudah saya
ubah di CSS tidak langsung berubah pada website sehingga saya harus mengecek
kembali kode dan melakukan refresh beberapa kali. Hal yang sama juga terjadi
saat mengatur layout karena hasilnya terkadang tidak langsung sesuai dengan
yang saya inginkan. Untuk tampilan mobile, saya lebih memprioritaskan
keterbacaan dan mengubah beberapa elemen yang berdampingan pada desktop
menjadi tersusun secara vertikal agar tetap nyaman dilihat.

3. Karena website ini masih berupa static web, informasi yang ditampilkan masih harus diubah secara langsung melalui file HTML jika ingin diperbarui. Website juga belum dapat menerima atau mengolah data dari pengguna. Pada pengembangan berikutnya, saya ingin menambahkan fitur dinamis seperti form kontak atau bagian portfolio yang datanya dapat diperbarui tanpa harus mengubah HTML secara langsung. Saya juga ingin menambahkan fitur lin yang bisa membuat website saya lebih interaktif, sehingga tidak hanya berisi tentang informasi satu arah.

### AI Disclosure
Saya menggunakan ChatGPT sebagai alat bantu untuk memahami instruksi tugas,
memberikan saran dalam pengembangan HTML dan CSS, membantu apabila ada 
masalah pada tampilan website, serta membantu proses Git dan deployment. Saya juga
menggunakan AI untuk meminta saran. Prompt yang saya berikan umumnya berupa pertanyaan mengenai langkah pengerjaan, masalah yang saya temui, dan bagian kode yang ingin diperbaiki. Saran dari AI tetap saya coba, periksa, dan sesuaikan kembali dengan kebutuhan website saya.

### Tugas 2

1. Ketika pengguna membuka suatu URL pada website, Django akan mengecek
`urls.py` untuk mencari URL yang sesuai.

Setelah ditemukan, Django akan menjalankan fungsi yang ada di `views.py`.
View kemudian dapat mengambil data yang dibutuhkan dari Model.

Data tersebut lalu dikirim oleh View ke Template dan ditampilkan
dalam bentuk halaman HTML kepada pengguna.

Secara sederhana, alurnya adalah:

URL → View → Model → View → Template → User


2. Data lebih baik disimpan di Model karena lebih mudah untuk ditambah,
diubah, atau dihapus tanpa harus mengubah kode HTML.

Selain itu, Template hanya bertugas untuk menampilkan data yang
diberikan oleh View.

Contohnya pada halaman More About Me, data hobbies, education,
dan fun facts disimpan di database kemudian ditampilkan menggunakan
loop pada Django Template.


3.`makemigrations` digunakan untuk membuat file migration berdasarkan
perubahan yang kita lakukan pada Model.

Sedangkan `migrate` digunakan untuk menerapkan file migration tersebut
ke database.

Jadi, `makemigrations` membuat rencana perubahan database,
sedangkan `migrate` menjalankan perubahan tersebut pada database.
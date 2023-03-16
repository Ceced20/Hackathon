Ini adalah project hackathon Ceced

Ini adalah kode untuk membuat sebuah chatbot sederhana menggunakan Python dan Natural Language Toolkit (NLTK). Chatbot dapat menjawab pertanyaan seputar cuaca, sinonim, antonim, dan informasi dasar tentang dirinya.

Kode ini menggunakan modul-modul Python seperti random untuk memilih jawaban acak, re untuk mencocokkan pola dalam teks, requests untuk mengambil data dari API OpenWeatherMap, dan nltk untuk memproses teks dan mendapatkan sinonim dan antonim dari sebuah kata menggunakan WordNet.

Pertama, ada variabel patterns yang berisi pola dan respons yang akan digunakan oleh chatbot. Pola dapat dibaca sebagai ungkapan reguler (regular expression) yang akan dicocokkan dengan masukan pengguna. Setiap pola memiliki satu atau beberapa respons yang dapat dipilih secara acak oleh chatbot.

Kemudian, ada fungsi match_pattern yang mencocokkan masukan pengguna dengan setiap pola di patterns dan mengembalikan respons yang sesuai. Jika pola yang cocok adalah tentang cuaca, maka fungsi akan memanggil API OpenWeatherMap untuk mendapatkan data cuaca untuk kota yang dimaksud. Jika pola yang cocok adalah tentang sinonim atau antonim, maka fungsi akan menggunakan WordNet untuk mendapatkan sinonim dan antonim dari kata yang dimaksud.

Terakhir, ada fungsi chat yang memulai obrolan dengan chatbot dan terus meminta masukan pengguna sampai pengguna memilih untuk keluar dengan mengetik 'quit'.

Untuk menjalankan program ini, Anda perlu mengunduh paket WordNet terlebih dahulu menggunakan nltk.download('wordnet'). Setelah itu, Anda dapat menjalankan program ini dengan mengetik python chatbot.py di terminal atau dalam lingkungan pengembangan seperti Jupyter Notebook.

Semoga ini dapat membantu menjelaskan bagaimana chatbot ini dibuat dengan menggunakan Python dan NLTK!



Cara memakai Chat bot yang bernama CygnusChat adalah Anda harus melakukan beberapa step berikut'

Download python 3.11.2

Buka Command Prompt Dengan cara Win+R Dan ketik "CMD" lalu enter

lalu ketik "pip install nltk"

lalu ketik "py Hackathon.py"

aksi tersebut bisa di lakukan di terminal Pycharm, CMD, Terminal Visual Code studio

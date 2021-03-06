# MASTERW6B-FRSBot V3.0
## NEW UPDATES: 
- Bisa digunakan banyak user dalam satu kali running program
- Menggunakan Multhithreading untuk melakukan pemilihan semua Matkul secara Parallel
- Menggunakan Multhiprocessing untuk menjalankan FRSBot untuk semua User secara Parallel
- Trigger setelah Login untuk memulai Job
### !!! Lakukan Semua langkah pada terminal dan directory yang terdapat semua file dari Repo ini !!!

<br />

**1. Clone Repo :**
```
git clone https://github.com/wildangbudhi/MASTERW6B-FRSBot.git
```

**2. Download Python3 :**
```
https://www.python.org/downloads/
```

**3. Download Node.JS :**
```
https://nodejs.org/en/download/
```

**4. Update pip for Python :**
```
pip install --upgrade pip
```
&nbsp;&nbsp; **or**
```
python -m pip install --upgrade pip
```
&nbsp;&nbsp; **or**
```
python3 -m pip install --upgrade pip
```
&nbsp;&nbsp; **or**
```
py -m pip install --upgrade pip
```

**5. Install Python Module :**
```
pip install -r requirementspip.txt
```

**6. Install Node.JS Module :**
```
npm i node-jsencrypt
```
**7. Edit file 'user.json' :**
- contoh format untuk satu user :
```json
{
    "Nama mu dongs":
    {
        "nrp": "0511174000xxxx",
        "password": "Password mu dongs"
    }
}
```
- contoh format untuk banyak user (dicontohkan 3 user) :
```json
{
    "Susilo":
    {
        "nrp": "0511174000xxxx",
        "password": "Passworddwwcnauoc"
    },

    "Joko Purnomo":
    {
        "nrp": "0511174000xxxx",
        "password": "Passworddwwcnauoc"
    },
    
     "Purwanto":
    {
        "nrp": "0511174000xxxx",
        "password": "Passworddwwcnauoc"
    }
}
```

**8. Edit file 'matkul.json' :**
- contoh format 1 user 6 matkul :
```json
{
    "Susilo":
    [
        {
            "nama": "Sistem Operasi",
            "kelas": "B"
        },
        {
            "nama": "Probabilitas dan Statistik",
            "kelas": "A"
        },
        {
            "nama": "Manajemen Basis Data",
            "kelas": "F"
        },
        {
            "nama": "Kecerdasan Buatan",
            "kelas": "A"
        },
        {
            "nama": "Analisis dan Perancangan Sistem Informasi",
            "kelas": "B"
        },
        {
            "nama": "Perancangan dan Analisis Algoritma",
            "kelas": "B"
        }
    ]
}
```
- contoh format 2 user 5 matkul :
```json
{
    "Susilo":
    [
        {
            "nama": "Sistem Operasi",
            "kelas": "B"
        },
        {
            "nama": "Probabilitas dan Statistik",
            "kelas": "A"
        },
        {
            "nama": "Manajemen Basis Data",
            "kelas": "F"
        },
        {
            "nama": "Kecerdasan Buatan",
            "kelas": "A"
        },
        {
            "nama": "Analisis dan Perancangan Sistem Informasi",
            "kelas": "B"
        },
        {
            "nama": "Perancangan dan Analisis Algoritma",
            "kelas": "B"
        }
    ],

    "Joko Purnomo":
    [
        {
            "nama": "Sistem Operasi",
            "kelas": "Z"
        },
        {
            "nama": "Probabilitas dan Statistik",
            "kelas": "A"
        },
        {
            "nama": "Manajemen Basis Data",
            "kelas": "F"
        },
        {
            "nama": "Kecerdasan Buatan",
            "kelas": "A"
        },
        {
            "nama": "Analisis dan Perancangan Sistem Informasi",
            "kelas": "B"
        },
        {
            "nama": "Perancangan dan Analisis Algoritma",
            "kelas": "B"
        }
    ]
}
```
- Jumlah Matkul tiap User tidak harus sama, bisa berbeda. Namun jumlah user di file 'matkul.json' harus sama dengan jumlah user di file 'user.json'

**9. Run Program :**
```
python main.py
```
&nbsp;&nbsp; **or**
```
python3 main.py
```
&nbsp;&nbsp; **or**
```
py main.py
```

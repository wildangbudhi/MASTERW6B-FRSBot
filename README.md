# MASTERW6B-FRSBot V2.0
## NEW UPDATES: Bisa digunakan banyak user dalam satu kali running program
### !!! Lakukan Download atau Clone semua data pada Repo ini terlebih dahulu !!!
### !!! Lakukan Semua langkah - lankah di dalam terminal dan directory yang terdapat semua file dari Repo ini !!!

<br />

**1. Download Python3 :**
```
https://www.python.org/downloads/
```

**2. Download Node.JS :**
```
https://nodejs.org/en/download/
```

**3. Update pip for Python :**
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

**4. Install Python Module :**
```
pip install -r requirementspip.txt
```

**5. Install Node.JS Module :**
```
npm i jsencrypt
```
**6. Edit file 'user.json' :**
- contoh format untuk satu user :
```
{
    "Nama mu dongs":
    {
        "nrp": "0511174000xxxx",
        "password": "Password mu dongs"
    }
}
```
- contoh format untuk banyak user (dicontohkan 3 user) :
```
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

**7. Edit file 'matkul.json' :**
- contoh format 1 user 6 matkul :
```
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
```
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

**8. Run Program :**
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

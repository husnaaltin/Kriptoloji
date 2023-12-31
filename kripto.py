import tkinter as tk
from tkinter import messagebox
import math
import hashlib
import random

def ozel_sifreleme(mesaj, anahtar):
    sifrelenmis_mesaj = ""

    for karakter, anahtar_karakter in zip(mesaj, anahtar):
        sifrelenmis_mesaj += karakter[:2]
        dinamik_bolum = surec(karakter, anahtar_karakter)
        sifrelenmis_mesaj += dinamik_bolum
        sifrelenmis_mesaj += karakter[-2:]

    return sifrelenmis_mesaj

def ozel_coz(mesaj, anahtar):
    cozulmus_mesaj = ""

    for i in range(0, len(mesaj), 8):
        cozulmus_bolum = surec_ters(mesaj[i:i+8], anahtar)
        cozulmus_mesaj += cozulmus_bolum

    return cozulmus_mesaj

def surec(karakter, anahtar_karakter):
    pi_sayisi = str(math.pi).replace(".", "")
    fibonacci_dizisi = fibonacci_dizisi_olustur(len(karakter) * 10)

    sonuc = ""
    for pi_hanesi, fib_terim, anahtar_hanesi in zip(pi_sayisi, fibonacci_dizisi, anahtar_karakter):
        sonuc += str((int(pi_hanesi) * fib_terim + int(anahtar_hanesi)) % 10)

    rastgele_sayi = random.randint(1, 100)
    sonuc = str((int(sonuc) + rastgele_sayi) % 10)

    sifreli_sonuc = hashlib.sha256(sonuc.encode()).hexdigest()

    return sifreli_sonuc

def surec_ters(sifreli_bolum, anahtar_karakter):
    sifreli_sonuc = hashlib.sha256(sifreli_bolum.encode()).hexdigest()
    rastgele_sayi = random.randint(1, 100)
    ters_sonuc = str((int(sifreli_sonuc, 16) - rastgele_sayi) % 10)

    cozulmus_sonuc = ""
    for i, anahtar_hanesi in enumerate(anahtar_karakter):
        if i < len(ters_sonuc):
            cozulmus_sonuc += str((int(ters_sonuc[i]) - int(anahtar_hanesi)) % 10)

    return cozulmus_sonuc

def fibonacci_dizisi_olustur(uzunluk):
    fibonacci_dizisi = [0, 1]
    while len(fibonacci_dizisi) < uzunluk:
        sonraki_terim = fibonacci_dizisi[-1] + fibonacci_dizisi[-2]
        fibonacci_dizisi.append(sonraki_terim)
    return fibonacci_dizisi

def sifreleme_butonu_tikla():
    orijinal_veri = giris_veri.get()
    sifreleme_anahtari = giris_anahtar.get()

    if orijinal_veri and sifreleme_anahtari:
        sifrelenmis_sonuc = ozel_sifreleme(orijinal_veri, sifreleme_anahtari)
        sonuc_degiskeni.set("Şifrelenmiş Veri: " + sifrelenmis_sonuc)
    else:
        messagebox.showerror("Hata", "Lütfen veriyi ve anahtarı girin.")

def cozme_butonu_tikla():
    sifreli_veri = giris_veri.get()
    cozme_anahtari = giris_anahtar.get()

    if sifreli_veri and cozme_anahtari:
        cozulmus_sonuc = ozel_coz(sifreli_veri, cozme_anahtari)
        sonuc_degiskeni.set("Şifre Çözülmüş Veri: " + cozulmus_sonuc)
    else:
        messagebox.showerror("Hata", "Lütfen veriyi ve anahtarı girin.")

pencere = tk.Tk()
pencere.title("Özel Şifreleme Aracı")


etiket_veri = tk.Label(pencere, text="Şifrelenecek Veri:", font=("Helvetica", 12))
giris_veri = tk.Entry(pencere, font=("Helvetica", 12), width=30)

etiket_anahtar = tk.Label(pencere, text="Kullanılacak Anahtar:", font=("Helvetica", 12))
giris_anahtar = tk.Entry(pencere, font=("Helvetica", 12), show='*', width=30)


sonuc_degiskeni = tk.StringVar()
etiket_sonuc = tk.Label(pencere, textvariable=sonuc_degiskeni, font=("Helvetica", 12), width=40, wraplength=300)


sifreleme_butonu = tk.Button(pencere, text="Şifrele", command=sifreleme_butonu_tikla, font=("Helvetica", 12), padx=10, pady=5)
cozme_butonu = tk.Button(pencere, text="Çöz", command=cozme_butonu_tikla, font=("Helvetica", 12), padx=10, pady=5)

etiket_veri.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
giris_veri.grid(row=0, column=1, padx=10, pady=5)

etiket_anahtar.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
giris_anahtar.grid(row=1, column=1, padx=10, pady=5)

sifreleme_butonu.grid(row=2, column=0, columnspan=2, pady=10)
cozme_butonu.grid(row=3, column=0, columnspan=2, pady=10)

etiket_sonuc.grid(row=4, column=0, columnspan=2, pady=5)

pencere.mainloop()
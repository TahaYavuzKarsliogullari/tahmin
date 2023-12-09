import random

def oyun():
    print("1 ile 100 arasında bir sayı seçtim. Şimdi sen tahmin et!")
    bilgisayar_sayisi = random.randint(1, 100)
    haklar = 5

    while haklar > 0:
        try:
            tahmin = int(input("Tahmininizi girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        if 1 <= tahmin <= 100:
            if tahmin == bilgisayar_sayisi:
                print("Tebrikler! Doğru tahmin ettin. Sayı:", bilgisayar_sayisi)
                break
            elif tahmin < bilgisayar_sayisi:
                print("Daha büyük bir sayı girin.")
            else:
                print("Daha küçük bir sayı girin.")

            haklar -= 1
            print("Kalan hakkınız:", haklar)
        else:
            print("Lütfen 1 ile 100 arasında bir sayı girin.")

    if haklar == 0:
        print("Hakkınız kalmadı. Doğru cevap:", bilgisayar_sayisi)

if __name__ == "__main__":
    oyun()

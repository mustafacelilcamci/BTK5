def cevre(uzun,kisa):
     return (uzun+kisa)*2
def alan(uzun,kisa):
    return (uzun*kisa)
sayi1=int(input("Kısa kenar"))
sayi2=int(input("Uzun kenar"))
print("Dikdörtgenin alanı",alan(sayi1,sayi2))
print("Dikdörtgenin çeversi",cevre(sayi1,sayi2))
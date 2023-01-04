import random
while True:
    Player=int(input("1.Taş 2.Kağıt 3.Makas: "))
    Computer=[1,2,3]
    Bilgisayar=random.choice(Computer)

    if Player==Bilgisayar:
        print("Berabere")


    elif (Bilgisayar  ==3) and (Player==1):

        print("Oyuncu kazandı bilgisayar makas yaptı ")


    elif (Bilgisayar==1) and (Player==3):

        print("Bilgisayar Kazandı bilgisayar taş yaptı")

    elif (Bilgisayar==2) and (Player==1):

        print("Bilgisayar Kazandı bilgisayar kağıt yaptı")


    elif (Bilgisayar==1) and (Player==2):

        print("Oyuncu Kazandı bilgisayar taş yaptı ")


    elif (Bilgisayar == 3) and (Player == 2):

        print("Bilgisayar Kazandı bilgisayar makas yaptı")


    elif (Bilgisayar == 2) and (Player == 3):

        print("Oyuncu Kazandı bilgisayar kağıt yaptı")

    else:
        print("Lütfen geçerli birşey giriniz")
    Retry=int(input("Tekrar oynamak ister misin 1.Evet 2.Hayır: "))

    if Retry==1:
        continue

    else:
        break
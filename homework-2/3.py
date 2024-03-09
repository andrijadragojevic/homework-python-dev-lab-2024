prisustvo = float(input("Unesite prisustvo u %: "))
seminarski_uradjeni = int(input("Da li je odradio seminarske (1 = DA, 0 = NE): "))


print("Moze da pristupi ispitu") \
if prisustvo > 75 and seminarski_uradjeni \
else print("Ne moze da pristupi ispitu")
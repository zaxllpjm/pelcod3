nama_saya = "Nama : Zendia Amelia"
print(nama_saya, "bertipe", type(nama_saya))

print()

NIM = "NIM : 230441100015 "
print(NIM, "bertipe", type(NIM))

print()

indeks = {
    "Celsius   " : "c",
    "Fahrenheit" : "f",
    "Kelvin    " : "k"
}
print("======Indeks Satuan Skala Suhu======")
for i in indeks:
    print("Satuan suhu :", i, "\t Indeks : ", indeks[i])
print()

suhu = float(input("Masukkan suhu : "))
satuan = input("Masukan indeks satuan skala suhu : ")

if (satuan == "c"):
    print (suhu, "derajat celsius : ")
    print ("Fahrenheit = ", (suhu*9/5)+32,"derajat")
elif (satuan == "f"):
    print (suhu, "derajat fahrenheit : ")
    print ("Celsius = ", (5/9)*(suhu-32),"derajat")
elif (satuan == "k"):
    print (suhu, "derajat kelvin : ")
    print ("Celsius = ", suhu-273,"derajat")
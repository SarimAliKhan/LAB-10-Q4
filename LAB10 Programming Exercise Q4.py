print("SARIM ALI KHAN")
print("18B-043-CS(A)")
print("LAB10")
fav_dishes = {"Fav1":"Biryani","Fav2":"Shashlik","Fav3":"Qorma","fav5":"Karahi","fav7":"Tikka"}
days = {"mon":"Shashlik","tue":"Qorma","wed":"Fajita","thu":"broast","fri":"Karahi"}
for i in fav_dishes:
    c = fav_dishes.get(i)
    for n in days:
        s = days.get(n)
        if c == s:
            print(c)




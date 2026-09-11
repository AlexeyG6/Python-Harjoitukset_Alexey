tunnus = ("python")
salasana = ("rules")

yritykset = 0

while yritykset != 5:
    yritykset += 1
    k = input("Anna tunnus: ")
    s = input("Anna salasana: ")
    if k == tunnus and s == salasana:
        print("Tervetuloa!")
        break   
    print("--------------")

if yritykset >= 5:
    print("Pääsy evätty.")
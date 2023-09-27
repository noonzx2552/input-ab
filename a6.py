money = int(input("พ่อให้เงินไปโรงเรียนกี่บาท:"))
school = str(input("เดินทางไปโรงเรียนด้วย[รถโดยสาร/วินมอเตอร์ไซค์/เเท็กซี่/เดิน]:"))

if school == "รถโดยสาร":
    print("เดินทางด้วย ", school ," เเละเหลือเงิน ", money - 10 ," บาท")
elif school == "วินมอเตอร์ไซค์":
    print("เดินทางด้วย ", school ," เเละเหลือเงิน ", money - 20 ," บาท")
elif school == "เเท็กซี่":
    print("เดินทางด้วย ", school ," เเละเหลือเงิน ", money - 40 ," บาท")
elif school == "เดิน":
    print("เดินทางด้วย ", school ," เเละเหลือเงิน ", money ," บาท")
else:
    print("error!")
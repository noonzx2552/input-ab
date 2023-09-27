score = int(input("score:"))

if score >= 90:
    print("ได้ค่าขนมเพิ่ม10บ./วัน")
elif score >= 80:
    print("ได้ค่าขนมเพิ่ม5บ./วัน")
elif score >= 70:
    print("ลดเล่นเกมลง1ชม./วัน")
else:
    print("ห้ามเล่นเกมส์เป็นเวลา 1 เดือน")
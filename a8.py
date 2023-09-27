a = int(input("AGE:"))
#if 20 < a:
#    print("ทานยาครั้งละ 2 เม็ด")
#elif 20 >= a:
#    print("ทานยาครั้งละ 1 เม็ด")
#elif 10 >= a:
#    print("ทานยาครั้งละ 1/2 เม็ด")
#elif 3 >= a:
#    print("ห้ามทานยานี้")
#else:
#    print("error!")

if a > 20:
    print("ทานยาครั้งละ 2 เม็ด")
elif 10 < a <= 20:
    print("ทานยาครั้งละ 1 เม็ด")
elif 3 < a <= 10:
    print("ทานยาครั้งละ 1/2 เม็ด")
else:
    print("ห้ามทานยานี้")
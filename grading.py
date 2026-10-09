name = (input("Enter your name:"))
y = int(input(f"{name},what's your score?"))
print(f"{y}")
if y >= 75:
    print(f"Excellent{name}!!! You scored A1🎉🎉")
elif y >= 70:
    print(f"Very Good{name}, you scored B2")
elif y >=65 :
    print(f"Good {name}, you scored B3 ")
elif y >= 60:
    print(f"Good {name}, you scored C4")
elif y>= 55:
    print(f"Good {name}, you scored C5")
elif y>= 50:
    print(f"Good {name}, you scored C6")
elif y>= 45:
    print(f"Oppps 😔{name}, you scored D7")
elif y>= 40:
     print(f"Opps 😔😔{name}, you scored E8")
elif y<=39:
    print(f"Ops 😭😭😭 {name}, you scored F9. You can do better next time")
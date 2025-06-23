import random
print("グー、チョキ、パーと入力")
A = input("入力してください：　")
b = random.randint(1,3)
if b == 1:
    print("相手はパーを出した")
elif b == 2:
    print("相手はチョキを出した")
else:
    print("相手はグーを出した")
if A == "パー":
    a = 1
elif A == "チョキ":
    a = 2
elif A == "グー":
    a = 3
if a == b:
    print("あいこ")
elif (a-b) % b == 1:
    print("あなたの勝ち")
else:
    print("あなたの負け")
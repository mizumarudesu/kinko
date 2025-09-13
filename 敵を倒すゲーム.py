import random
print("ルール説明　攻撃は５０から１００のダメージを与えられる、魔法は１０から２００のダメージを与えられる、カウンターは相手の攻撃が１３０以上なら成功して、１５０ダメージを与えることが出来る。カウンターに失敗すると、ダメージをくらうだけである。")
def battle():
    myhp = 1000
    print("あなたのhpは1000")
    b = input("enterを押してね")
    a = random.randint(1,3)
    if a == 1:
        print("スライムが現れた")
        hp = 300
        attack = random.randint(50,80)
    elif a == 2:
        print("ゴブリンが現れた")
        hp = 500
        attack = random.randint(80,150)
    else:
        print("魔王が現れた")
        hp = 1000
        attack = random.randint(60,200)
    while hp > 0 and myhp > 0:
        print()
        myattack = input()
        if myattack == "攻撃":
            myattack = random.randint(50,100)
            hp = hp - myattack
            print(f"あなたは{myattack}与えた")
        elif myattack == "魔法":
            myattack = random.randint(10,200)
            hp = hp - myattack
            print(f"あなたは{myattack}与えた")
        elif myattack == "カウンター":
            if attack >= 130:
                myattack = 150
                hp = hp - myattack
                print(f"あなたは{myattack}与えた")
                myattack = "カウンター"
                print("成功した")
            else:
                print("失敗した")
        if myattack == "カウンター" and attack >= 130:
            print(end = "")
        elif a == 1:
            myhp = myhp - attack
            print(f"あなたは{attack}くらった")
            attack = random.randint(50,80)
    
        elif a == 2:
            myhp = myhp - attack
            print(f"あなたは{attack}くらった")
            attack = random.randint(80,150)
    
        elif a == 3:
            myhp = myhp - attack
            print(f"あなたは{attack}くらった")
            attack = random.randint(60,200)
    
    
    
    
        print(f"あなたのhpは{myhp}")
    if myhp > 0:
        print("あなたの勝ち")
    else:
        print("あなたの負け")
    
if __name__ == "__main__":
        battle()

        
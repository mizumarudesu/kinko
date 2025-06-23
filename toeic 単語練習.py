import random
words = {"abandon" : "放棄する" , "absorb" : "吸収する" , "abstract" : "抽象的な" , "acquire" : "獲得する" , "adapt" : "適応する" , "defective" : "欠陥のある" , 
         "fraction" : "ほんの一部" , "shoreline" : "海岸線"}

def quiz():
    score = 0
    total = len(words)
    word_list = list(words.keys())
    random.shuffle(word_list)
    a = 1
    for word in word_list:
         
         print(f"単語 {word}")
         answer = input("意味は？: ")
         
         if answer.strip() == words[word]:
            print("正解！")
            score += 1
            a = a + 1
            print(f"結果： {score}/5 正解!\n")
            if a == 6:
                break
         else:
            print(f"不正解。正しい意味は{words[word]}です。")
            a = a + 1
            print(f"結果： {score}/5 正解!\n")
            if a == 6:
            
                break
         
             

        
    

              

if __name__ == "__main__":
    quiz()


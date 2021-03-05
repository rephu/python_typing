import random
import time

questions = ["北海道","青森","岩手","宮城","秋田","山形","福島","茨城","栃木","群馬","埼玉","千葉","東京","神奈川","新潟","富山","石川","福井","山梨","長野","岐阜","静岡","愛知","三重","滋賀","京都","大阪","兵庫","奈良","和歌山","鳥取","島根","岡山","広島","山口","徳島","香川","愛媛","高知","福岡","佐賀","長崎","熊本","大分","宮崎","鹿児島","沖縄"]




def serve():
    i = 0
    start = time.time()

    while i < 10:
        chosen = random.choice(questions)
        string = input(chosen + "をタイピング！>>>>")
        if string == chosen:
            print("クリア！")
            i += 1
            if i == 10:
                end = time.time() - start
                print("かかった時間は" + str(end) + "秒だよ")
            else:
                print("次の問題へ")
        else:
            print("ゲームオーバー！")
            break
    print("また遊んでね")

    
    
print("ルール説明\r\n〇〇(都道府県名)をタイピング！\r\nと表示されたら該当の都道府県名を入力します\r\n \r\n正解したら次の問題に進めるよ！\r\n問題は全部で10問！")
print("都道府県タイピングゲームを開始しますか？")      
answer = input("Y/N")
if answer == "y" or "Y":
    print("始めるよー！")
    print("開始まで...")
    time.sleep(2)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    serve()
else:
    print("いつかプレイしてね！")



    





     


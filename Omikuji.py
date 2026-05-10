import random
import tkinter as tk
import time

def main():
    root = tk.Tk()
    root.title("くじ")
    root.geometry("400x400")
    
    # 結果表示用テキストボックス
    result_text = tk.Text(root, height=12, width=40, font=("Arial", 14))
    result_text.pack(pady=10)
    
    def fortune():
        """運勢を判定"""
        a = random.randint(0, 100)   
        if a == 1: #1％
            return "大吉！！"
        elif 1 < a < 10: #9％
            return "吉"
        elif 10 <= a < 25: #15％
            return "中吉"
        elif 25 <= a < 50: #25％
            return "小吉"
        elif 50 <= a < 75: #25％
            return "末吉"
        elif 75 <= a < 90: #15％　
            return "凶"
        else: #10％
            return "大凶"
    
    def single_draw():
        """単発くじ"""
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "今日の運勢は・・・\n\n")
        result_text.insert(tk.END, fortune())

    
    def ten_draw():
        """10連くじ"""
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "10連運勢は・・・\n\n")
        hide_buttons()  # ボタンを隠す
        for i in range(10):
            result_text.insert(tk.END, f"{i+1}回目：{fortune()}\n")
            root.update()
            time.sleep(0.2)
        time.sleep(0.5)
        show_buttons()  # ボタンを再表示
    
    def end_program():
        """終了"""
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "終了します")
        root.after(500, root.quit)

    def hide_buttons():
        """ボタンを隠す"""
        one.pack_forget()
        ten.pack_forget()
        end.pack_forget()
    
    def show_buttons():
        """ボタンを再表示"""
        one.pack(side=tk.LEFT, padx=5)
        ten.pack(side=tk.LEFT, padx=5)
        end.pack(side=tk.LEFT, padx=5)

    def show_manual():  # 最初はボタンを表示
        root = tk.Tk()
        root.title("説明書")
        root.geometry("600x400")
        manual_text = tk.Text(root, height=30, width=80, font=("Arial", 12))
        manual_text.pack(pady=10)
        manual_text.insert(tk.END, "使用説明書\nこのプログラムは、運勢を占うくじ引きゲームです。以下の手順で遊ぶことができます。\n1. プログラムを実行すると、ウィンドウが表示されます。\n2. 「単発」ボタンをクリックすると、今日の運勢が表示されます。\n3. 「10連」ボタンをクリックすると、10回分の運勢が順番に表示されます。表示中はボタンが隠れます。\n4. 「終了」ボタンをクリックすると、プログラムが終了します。\n\n運勢の種類と確率\n- 大吉: 1%\n- 吉: 9%    \n- 中吉: 15%\n- 小吉: 25%\n- 末吉: 25%\n- 凶: 15%\n- 大凶: 10%\n\n注意\nこのプログラムは、PythonのTkinterライブラリを使用してGUIを作成しています。Pythonがインストールされている環境で実行してください。\n運勢の結果は完全にランダムであり、実際の運勢を反映するものではありません。楽しんで遊んでください！\n\n創作主より\nGUI化にはAIを使いましたが、運勢の判定や確率設定は自分で考えました。単発と10連の両方を実装することで、より楽しめるように工夫しました。今後も面白いプログラムを作っていきたいと思います。\n大吉が出るまで終われない、とか遊んでみると意外と沼ります。時間を溶かす可能性があるので、ほどほどに楽しんでくださいね。")

    # ボタンフレーム
    button_frame = tk.Frame(root)
    button_frame.pack()
    
    one = tk.Button(button_frame, text="単発", width=10, command=single_draw)
    one.pack(side=tk.LEFT, padx=5)
    ten = tk.Button(button_frame, text="10連", width=10, command=ten_draw)
    ten.pack(side=tk.LEFT, padx=5)
    end = tk.Button(button_frame, text="終了", width=10, command=end_program)
    end.pack(side=tk.LEFT, padx=5)
    manual = tk.Button(button_frame, text="使い方", width=10, command=show_manual)
    manual.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()

# 数値入力を受け取る
user_input = input("数値を入力してください: ")

# 入力された文字列を数値に変換する
try:
    number = int(user_input)  # 整数に変換
    # number = float(user_input)  # 小数に変換する場合はこちらを使用

    # 数値を使った処理
    print("入力された数値:", number)
    print("入力された数値を2倍:", number * 2)

except ValueError:
    print("無効な入力です。数値を入力してください。")
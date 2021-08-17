# floor()を使うためにインポート
import math

# 与えられたデータ
heavy_rain_number = [
    203, 146, 333, 171, 206, 123,
    230, 430, 357, 318, 268, 225,
    236, 463, 252, 309, 252, 330,
    220, 272, 358, 367, 308, 309,
    269, 334, 327, 350, 377, 345
]

# データのすべての要素について処理する
# for x in range(n): for以下のブロックの処理をn回回す、iは何回目のループか（i>=0)
# len()関数: 引数に与えられた配列やリストの長さを取得する
for i in range(len(heavy_rain_number)):

    # グラフの***の部分を表す変数
    graph = ""

    # ***...を描画する
    # heavy_rain_number[i] / 10回forを回して、その回数graphに*を追加
    # math.floor()関数: 引数に与えられた小数の小数第一位を切り捨てて整数にする
    for j in range(math.floor(heavy_rain_number[i] / 10)):
        graph += "*"  # graphにぶち込む

    # 最後に表示する
    # format()関数: 文字列中の第n(>=0)番目の{}をn番目の引数で置換する
    print("{}: ( {} ) {}".format(1991 + i, heavy_rain_number[i], graph))


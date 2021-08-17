import numpy as np  # NumPyをインポート
import statistics as stat  # 標準偏差をとるためにstatisticsをインポート
from math import floor  # floor()を使うためにmath.floor()をインポート

# 平均0、標準偏差1の正規分布に従う乱数のリストを生成（要素数: 1000000）
n = 1000000
x = np.random.randn(n)
print("リストxの先頭10個の要素値", x[0:10])

print("[1]乱数の出現分布")

# -2.75より小さい値の集合を表示
# range(): 範囲を指定する関数
# floor(x): 小数xを切り捨てて整数にする関数
# len(x): 配列xの大きさを取得する関数
# filter(x, y): 配列yのうち、条件式xに適合する要素だけをフィルタして返す関数
print("[ -inf : -2.75 ]: ", end='')  # ラベルをまず表示（print()の第２引数にend=''とすることで改行を回避）
for _ in range(
        floor(
            len(
                list(
                    filter(lambda m: m < -2.75, x))
            ) / 5000  # ***...の数は当該要素数の1/5000
        )
):
    print("*", end='')  # ***...を表示

# 一旦改行する
print("\n", end='')

# -2.75~+2.75の値を11分割して表示
for i in range(11):
    a = -2.75 + 0.5 * i  # 範囲の左端
    b = -2.75 + 0.5 * (i + 1)  # 範囲の右端
    print(
        "[ {}{} : {}{} ]: ".format(
            "+" if a > 0 else "",  # ラベルの左端に"+"を付けるかどうか
            a,  # 範囲の左端
            "+" if b > 0 else "",  # ラベルの右端に"+"を付けるかどうか
            b  # 範囲の右端
        ), end=''  # end=''で改行を回避
    )

    for _ in range(
            floor(
                len(
                    list(
                        filter(lambda m: a <= m < b, x)  # aからbの範囲にある要素をxから抽出
                    )
                ) / 5000
            )
    ):
        print("*", end='')

    # 改行する
    print("\n", end='')

# -inf~-2.75の時と同様、+2.75~+infの表示処理
print("[ +2.75 : +inf ]: ", end='')
for _ in range(
        floor(
            len(
                list(
                    filter(lambda m: 2.75 <= m, x)  # 2.75より大きい要素だけをxから抽出
                )
            ) / 5000
        )
):
    print("*", end='')

# 改行
print("\n", end='')

print("[2]平均uと標準偏差s（理論値）:実測値")
u = sum(x) / n  # 平均値（総和/xの全総素数）
s = stat.pstdev(x)  # 標準偏差（statisticsライブラリのpstdev(x)関数より算出）
print("平均 u(0): {}".format(u))
print("標準偏差 s(1): {}".format(s))

# [-ks:ks]の範囲にある要素の確率（範囲にある要素数/全要素数）を表示する
labels = [0.68, 0.95, 0.99]  # 確率（理論値）のラベル
for i in range(3):
    print(
        "[-{}s:{}s]の範囲内の確率({}): {}".format(
            i,
            i,
            labels[i],
            len(
                list(
                    filter(lambda m: -(i + 1) * s <= m < (i + 1) * s, x)  # -(i + 1)~(i + 1)の範囲にある要素のみを抽出（iが0からなのに対し、kは1からなのでi+1としている）
                )
            ) / len(x)
        )
    )


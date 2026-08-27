# ## 12. while ループ
# `while` を使って，1 から順に整数を足していき，合計がはじめて 10 を超えたときの合計を出力してください．
#
# 期待する出力：15

total = 0
_ = 1

while total <= 10:
    total += _
    _ += 1

print(total)

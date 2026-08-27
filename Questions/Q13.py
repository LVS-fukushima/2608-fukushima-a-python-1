# ## 13. break, continue
# 1 から 10 までの整数を for 文で順に処理してください．
# 値が奇数のときは `continue` でスキップし，値が 8 になったら `break` でループを終了してください．
# ループ内では値を出力してください．
#
# 期待する出力：
# ```
# 2
# 4
# 6
# ```

for _ in range(1, 11):
    if _ % 2 != 0:
        continue

    if _ == 8:
        break
    
    print(_)

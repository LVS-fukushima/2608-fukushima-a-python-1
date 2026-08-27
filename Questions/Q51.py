# ## 51. 型の確認
# 3つの変数に以下のように代入したコードがあります．各変数の型を出力してください．出力形式は問いません．
# ```
# data1 = {'A':1, 'B':2}
# data2 = "hoge"
# data3 = {1,2,3,4,5}
# ```
# 期待する出力：<class 'dict'> <class 'str'> <class 'set'>

data1 = {'A':1, 'B':2}
data2 = "hoge"
data3 = {1,2,3,4,5}

print(type(data1),type(data2),type(data3))
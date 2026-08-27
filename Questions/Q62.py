# ## 62. 内包表記１
# 文字列のリスト `['The', 'quick', 'brown']` を代入し、
# それぞれの文字列の長さからなるリストを返す内包表記を記述してください。
#
# 期待する出力：[3, 5, 5]

li = ['The', 'quick', 'brown']

range = [len(text) for text in li]

print(range)
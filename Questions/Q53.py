# ## 53. split
# 変数に文字列 `'C C++ // python java'` を代入し，この文字列を空白で区切った後のリストを出力してください，また，同じことを `'/'` でも行い，出力してください．
#
# 期待する出力：['C', 'C++', '//', 'python', 'java'], ['C C++ ', '', ' python java']

text = 'C C++ // python java'

print(text.split(' '))
print(text.split('/'))
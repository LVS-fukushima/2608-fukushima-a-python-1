# ## 64. 内包表記（条件付き）
# 文字列のリスト `['cat', 'dog', 'elephant', None, 'giraffe']` を代入し、
# None を除いたリストを新たに作成してください。
#
# 期待する出力：['cat', 'dog', 'elephant', 'giraffe']

li = ['cat', 'dog', 'elephant', None, 'giraffe']

result = [animal for animal in li if animal is not None]

print(result)
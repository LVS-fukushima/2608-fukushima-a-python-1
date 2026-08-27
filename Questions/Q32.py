# ## 32. zip
# 2 つのリスト `names = ['Alice', 'Bob', 'Charlie']` と `scores = [90, 75, 85]` が与えられています．
# `zip` を使って，「名前: 点数」の形式で各人を 1 行ずつ出力してください．
#
# 期待する出力：
# ```
# Alice: 90
# Bob: 75
# Charlie: 85
# ```

names = ['Alice', 'Bob', 'Charlie']
scores = [90, 75, 85]

for name,score in zip(names, scores):
    print(f'{name}: {score}')

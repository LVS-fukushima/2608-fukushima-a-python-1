# ## 43. 辞書（キーの存在確認）
# 今，以下のように辞書が作成済みです．
# ```
# d = {'apple':10, 'grape':20, 'orange':30}
# ```
# この辞書に対して，'apple'というキーが存在するかを確認し，存在しなければ，'apple'というキーに対して-1という値を追加してください．また，同様のことを'pineapple'でも行なってください．
#
# その後，最終的な辞書を出力してください．
#
# 期待する出力：{'apple': 10, 'grape': 20, 'orange': 30, 'pineapple': -1}

d = {
    'apple':10,
    'grape':20, 
    'orange':30
}

if 'apple' not in d:
    d['apple'] = -1
if 'pineapple' not in d:
    d['pineapple'] = -1

print(d)
# ## 89. 関数（デコレータ）
# 74.標準ライブラリ（time）を書き換え、3秒待機してからメッセージを表示する関数 `wait_three_secounds` を定義してください。
# デコレータ `measure_time` を作成して関数の実行時間を計測し、実行時間を出力してください。
#
# 期待する出力：
# ```
# Hello World
# 3.0028164386749268
# ```

from functools import wraps
import time



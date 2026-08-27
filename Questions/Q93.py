# ## 93. クラス４（ABC）
# 以下の要件に従って、複数の抽象メソッドを持つABCを定義し、実装クラスを作成してください。
#
# * `Vehicle` という名前の抽象基底クラスを定義し、`start` と `stop` という2つの抽象メソッドを持たせる。
# * `Car` クラスを定義し、`Vehicle` を継承する。`start` メソッドでは「Car started」、`stop` メソッドでは「Car stopped」と出力する。
# * `Bike` クラスを定義し、`Vehicle` を継承する。`start` メソッドでは「Bike started」、`stop` メソッドでは「Bike stopped」と出力する。

from abc import ABC, abstractmethod



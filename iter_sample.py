# coding: utf-8

# モジュール itertools をインポート
import itertools

# 整数 0, 1, 2 が合計 2 個並んだ、すべてのタプルについてのループ
for tsui in itertools.product(range(3), repeat=2):

    print(tsui)

print('#' * 30)

######################################################################

# 'a' と 'b' が合計 3 個並んだ、すべてのタプルについてのループ
for choku in itertools.product('ab', repeat=3):

    # 'a' の数を数える
    a_count = 0

    # タプル choku の各要素についてのループ
    for moji in choku:
        if moji == 'a':
            a_count = a_count + 1

    # 'a' の数と、タプルを表示する
    print(a_count, choku)

print('#' * 30)

######################################################################

# 'A', 'B', 'C', 'D' から 2 個を選んで作られる、
# すべての順列を表すタプルについてのループ
for jun in itertools.permutations('ABCD', r=2):

    print(jun)

print('#' * 30)

######################################################################

# 'A', 'B', 'C', 'D' から 2 個を選んで作られる、
# すべての組合せを表すタプルについてのループ
for kumi in itertools.combinations('ABCD', r=2):

    print(kumi)

print('#' * 30)


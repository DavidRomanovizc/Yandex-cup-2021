"""
Нам нужно достать с сервера 4 переменных в три запроса, при это в одном запросе имена не должны повторяться,
всего переменных 4 и возвращаются они в качестве value.

a -> A "произвольное значение"
b -> B
c -> C
d -> D
Нам нужно определить соответсвие

Если мы делаем один запрос, то
a -> A

Если мы делаем запрос на две переменных, то мы получаем значения переменных, которые мы не сможем сопоставить
"""
# Я не знаю, почему в некоторых тестах этот алгоритм не сработал
import requests
import sys
from collections import Counter


def ReqVar(vars):
    headers_map = {"X-Cat-Variable": ",".join(vars)}
    resp = requests.request("MEW", r"http://127.0.0.1:7777/", headers=headers_map)
    values = []
    for header in resp.headers:
        if header.lower() == 'x-cat-value':
            values = resp.headers[header].strip().split(', ')
    if not values:
        return None
    # values = list(map(lambda x: x.strip(), values))
    return values


def Unions(c1, c2):
    res = Counter()
    for k1 in c1:
        if k1 not in c2:
            res[k1] = c1[k1]
        else:
            res[k1] = max(c1[k1], c2[k1])
    for k2 in c2:
        if k2 not in res:
            res[k2] = c2[k2]
    return res


def Diff(c1, c2):
    res = Counter()
    for k1 in c1:
        if k1 not in c2:
            res[k1] = c1[k1]
        else:
            d = c1[k1] - c2[k1]
            if d:
                res[k1] = d
            if d < 0:
                a = []
                a[100] = 0
    return res


A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()
D = sys.stdin.readline().strip()

req1 = Counter(ReqVar([A, B, C]))  # a b c
req2 = Counter(ReqVar([A, C, D]))  # a c d
req3 = Counter(ReqVar([B, C, D]))  # b c d

R12 = Unions(req1, req2)
R23 = Unions(req2, req3)
R13 = Unions(req1, req3)

req1R12 = Diff(R12, req1)
req2R12 = Diff(R12, req2)

req2R23 = Diff(R23, req2)
req3R23 = Diff(R23, req3)

req1R13 = Diff(R13, req1)
req3R13 = Diff(R13, req3)

a = b = c = d = None

if req1R12:
    d = list(req1R12.keys())[0]
    b = list(req2R12.keys())[0]
if req2R23:
    b = list(req2R23.keys())[0]
    a = list(req3R23.keys())[0]
if req1R13:
    d = list(req1R13.keys())[0]
    a = list(req3R13.keys())[0]


if a is None and b is None and c is None and d is None:
    a = b = c = d = list(R13.keys())[0]

while a is None or b is None or c is None or d is None:
    if a is None and b and c:
        a = list(Diff(req1, Counter([b, c])).keys())[0]
    if b is None and d and c:
        b = list(Diff(req1, Counter([a, c])).keys())[0]
    if c is None and a and b:
        c = list(Diff(req1, Counter([a, b])).keys())[0]
    if d is None and a and c:
        d = list(Diff(req2, Counter([a, c])).keys())[0]

print(a)
print(b)
print(c)
print(d)

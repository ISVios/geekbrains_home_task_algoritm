#!/bin/env python3

from collections import namedtuple

count = int(input())

Enterprise_struct = namedtuple("Enterprise", ["name", "quart1", "quart2", "quart3", "quart4", "res"])

enters = []

for i in range(count):
    ent = Enterprise_struct(
        input("input name: "),
        float(input("first quart: ")),
        float(input("second quart: ")),
        float(input("third quart: ")),
        float(input("fourth quart: ")),
        0,
    )
    ent  = ent._replace(res = sum(ent[1:]))
    enters.append(ent)
    print()

avg = sum(map(lambda x: x.res, enters)) / count
print(f"\navg is {avg}\n")

bad = []
print("Company with > avg")
for ent in enters:
    if ent.res >= avg:
        print(ent.name, ent.res)
    else:
        bad.append(ent)

if bad:
    print()
    print("Company with < avg")
    for ent in bad:
        print(ent.name, ent.res)

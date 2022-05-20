#!/bin/env python
# 1. Определение количества различных подстрок с использованием хэш-функции. 
#  Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
#  Требуется найти количество различных подстрок в этой строке.



import hashlib


def num_subs(s: str) -> int:
   

    if s == "":
        return 0

    full_hash = hashlib.sha1(s.encode('utf-8')).hexdigest()
    empty_hash = hashlib.sha1(''.encode('utf-8')).hexdigest()
    count = 0

    for i_ind in range(len(s) + 1):
        for j_ind in range(len(s) + 1):
            try_hash = hashlib.sha1(s[i_ind:j_ind].encode('utf-8')).hexdigest()
            if try_hash != full_hash and try_hash != empty_hash: # ignore empty and full # to not duplicate
                count += 1
 
    return count


s = input('input text: ')
print("count of substring is", num_subs(s))


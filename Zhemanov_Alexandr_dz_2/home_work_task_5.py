#!/bin/env python3
# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# ASCII таблица питона(chr)

BEGIN = 32
END = 127
COUNT_IN_LINE = 10
i = 1

for ch_i in range(BEGIN, END + 1):

    print(f"{ch_i:3d}-{chr(ch_i)} ", end="")
    
    if i == COUNT_IN_LINE: # без %
        i = 0
        print()
    
    i += 1

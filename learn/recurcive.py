"""
N Taille de l'escalier
Monte 1 / 2 / 3 marche
"""

10
    3  = 3 * 1 + 2 * 1 + 1 * 1
    3 =  1 + 1  + 1

10 / 3
    3 = 1 / 2

4
 1 1 1 1
 1 1 2
 1 2 1
 1 3

 2 1 1
 2 2

 3 1

4
 1 1 1 1 1
 1 1 1 2
 1 1 2 1
 1 1 3
 1 2 1 1
 1 2 2
 1 3 1

 2 1 1 1
 2 1 2
 2 2 1
 2 3

 3 1 1
 3 2

p = nombre de possibilité

5 = p(4) + p(3) + p(2)
4 = p(3) + p(2) + p(1)
3 = p(2) + p(1) + p(0)

p(n) = p(n - 1) + p(n - 2) + p(n - 3)

p(0) = 1
p(1) = 1
p(2) = 2
p(3) = 4

def p(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return p(n - 1) + p(n - 2) + p(n - 3)

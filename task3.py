# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.
#
# блоксхемы я не рисую из принципа. курс называется алгоритмы на языке питон  а не уроки рисования.


n = int(input('n = '))
reverted = 0
while n > 0:
    reverted = reverted * 10 + n%10
    n //= 10

print (reverted)
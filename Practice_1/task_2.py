'''
2.Длина Московской кольцевой автомобильной дороги —109 километров.
Стартуем с нулевого километра МКАД и едем со скоростью V километров в час.
На какой отметке остановимся через T часов? Программа получает на вход значение V и T.
Если V>0, то движемся в положительном направлении по МКАД, если же значение V<0, то в отрицательном.
Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановимся.
'''


print("Ввод V")
V = int(input())
print("Ввод T")
T = int(input())
km = (V*T) % 109
print(km)

# -*- coding: utf-8 -*-
# Домашнее задание. Лучше если каждая задачка будет оформлена в виде одного файла .py
# 2) Пользователь вводит число от 1 до 12. Вернуть название сезона, которому принадлежит месяц с этим номером (весна, лето, зима, весна).

a = int(input())
if 3 <= a <=5:
    print("Spring")
elif 6 <= a <= 8:
    print("Summer")
elif 9 <= a <= 11:
    print("Autumn")
else: print("Winter")

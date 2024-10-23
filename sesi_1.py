#Penggunaan Module 1
# import math
# print(math.sqrt(16))

#Penggunaan Module 2
# import math as m
# print(m.sqrt(25))

#Penggunaan Module 3
# from math import sqrt
# print(sqrt(36))

#Penggunaan Module 4
# from math import sqrt as s
# print(s(36))

#Contoh
import math
#import pygame

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

print(hitung_luas_lingkaran(10))
# Made By MNRCH
# https://github.com/MNRCHY

import random

print ("")
print ("===========================")
print ("====== Ayo Main Suit ======")
print ("===========================")
print ("")
user_act = input ("Apa yang akan kamu pasang? (batu, gunting, kertas = ")
choice = ["batu", "gunting", "kertas"]
com_act = random.choice(choice)

print ("Kamu pasang ", {user_act}, "Lawan pasang", {com_act})

if user_act == com_act:
    print ("hasilnya SERI, kedua pemain memilih ", {user_act})

elif user_act == "batu":
    if com_act == "gunting":
        print ("Wah kamu menang, lawan memilih ", {com_act})
    else: print ("Yah kamu kalah, lawan memilih ", {com_act})

elif user_act == "kertas":
    if com_act == "batu":
        print ("Wah kamu menang, lawan memilih ", {com_act})
    else: print ("Yah kamu kalah, lawan memilih ", {com_act})

elif user_act == "gunting":
    if com_act == "kertas":
        print ("Wah kamu menang, lawan memilih ", {com_act})
    else: print ("Yah kamu kalah, lawan memilih ", {com_act})

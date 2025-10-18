#!/bin/env python3


import sys
import random
import numpy as np
import os

# PERMAINAN TRIPLE DICE


def main():
    # cek argument input user
    if len(sys.argv) < 2:
        print("Masukkan player. Contoh:")
        print("   python3 triple_dice.py dhurin faisal bestari")
        sys.exit(1)

    print("\n====SELAMAT DATANG PLAYER TRIPLE DICE=====")
    print_player()

    print("\n==otomatis generate dadu==")
    print_dadu()

    print("\n==otomatis generate dadu tersembunyi==")
    print("\n== Dadu Tersembunyi Pemain ==")
    print_dadu_tersembunyi()
    tebak_skor()

    print("== Dadu Tersembunyi Semua Pemain dan Skor Tebak ==")
    reveal()


# generate dadu
player = len(sys.argv)
jumlah_player = player - 1
dadu = np.random.randint(1, 7, size=(jumlah_player, 12))
dadu_tersembunyi = np.random.randint(1, 7, size=(jumlah_player, 2))

# isi tebakan player
tebakan_skor = []


# memunculkan player dan menghitung jumlah player
def print_player():
    a = 1
    while a < player:
        print(f"haloo player {a}: {sys.argv[a]} ")
        a += 1

    print(f"jumlah player: {jumlah_player}")


# print dadu masing2 player
def print_dadu():
    b = 1
    while b < player:
        print(f"dadu {sys.argv[b]} \t=> {dadu[b-1]} ")
        b += 1


# fungsi buat clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# tampilkan dadu tersembunyi
def print_dadu_tersembunyi():
    for i in range(jumlah_player):
        input(f"\n[ENTER] untuk membuka dadu tersembunyi pemain {sys.argv[i+1]}...")
        print(f"Dadu tersembunyi pemain {sys.argv[i+1]}: {dadu_tersembunyi[i]}")

        input("[ENTER] untuk menyembunyikan...")
        clear_screen()
        print_player()
        print_dadu()


# tebak skor
def tebak_skor():
    for i in range(jumlah_player):
        while True:
            try:
                print(
                    f"""\n{sys.argv[i+1]} tebak skor akhir kamu:
                        1. low
                        2. midlow
                        3. midhigh
                        4. high
                      """
                )
                tebakan = int(input("Masukkan angka antara 1 sampai 4: "))

                if 1 <= tebakan <= 4:
                    tebakan_skor.append(tebakan)
                    break  # keluar dari while jika input valid
                else:
                    print("   Angka harus antara 1 hingga 4! Coba lagi.")
            except ValueError:
                print("   Input harus berupa angka! Coba lagi.")

        clear_screen()
        print_player()
        print_dadu()


def reveal():
    input(f"\n[ENTER] untuk membuka dadu tersembunyi...")

    for i in range(jumlah_player):
        print(f"Pemain {sys.argv[i+1]}: {dadu_tersembunyi[i]}")

    input(f"\n[ENTER] untuk membuka Tebakan...")
    kategori = {1: "low", 2: "midlow", 3: "midhigh", 4: "high"}

    print("\n== Tebakan Pemain ==")
    for i in range(jumlah_player):
        angka = tebakan_skor[i]
        teks = kategori.get(angka, "tidak valid")
        print(f"Pemain {sys.argv[i+1]} menebak: {angka} → {teks}")


# ==========Main============================
main()

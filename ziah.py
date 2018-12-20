#!/usr/bin/python
import sys
def utama():
    print "Mau gk jadi istri gua ?"
    print "1 = Mau"
    print "2 = Tidak Mau"
    dipilih = raw_input("Pilih Nomor ( 1 / 2 ) : ")
    if dipilih == "1":
        print '"Makasih ya...Hbd ya sayang maaf cuman bisa ngasih ginian...moga panjang umur and trus ama gua..love u :* "'
    elif dipilih == "2":
        print 'yaudah dah klo masih blm mau..gua tunggu ampe mau yank"'
    else :
        print "Pilihannya Cuma 1 Sama 2 Doang yank -_- "
    ulangi()
    
def ulangi():
    dicobalagi = raw_input("Coba lagi ? [Y/T] : ")
    if dicobalagi.lower() == "y":
        utama()
    elif dicobalagi.lower() == "t":
        sys.exit("Dadah :)")
    else :
        print "Pilihannya Cuma Y dan T Doang yank -_- "
        ulangi()

utama()

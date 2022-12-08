## chiffrement rsa
import base64


def chiffrement_rsa(m, e, n):
    return (m**e)%n

## calcul de la clef publique

def clef_publique(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    for e in range(2, phi):
        if pgcd(e, phi) == 1:
            break
    return (e, n)

## calcul de la clef privee

def clef_privee(p, q, e):
    phi = (p-1)*(q-1)
    for d in range(2, phi):
        if (d*e)%phi == 1:
            break
    return (d)

## pgcd

def pgcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

## main

def getPos(lettre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if lettre == alphabet[i]:
            return i


def RSA():
    p = int(input("p: "))
    q = int(input("q: "))
    m = input("message: ")
    e, n = clef_publique(p, q)
    print("clef publique: ", e, n)
    d = clef_privee(p, q, e)
    print("clef privee: ", d)
    for lettre in m:
        lettrechiffre = chiffrement_rsa(getPos(lettre) +1, e, n)
        print(lettrechiffre)




import hashlib

def hash(mot):
    return hashlib.sha256(mot.encode('utf-8')).hexdigest()

print(hash("testhash"))

import hamming_codec
def encode(message):
    # convert message to binary

    print(message)
    return hamming_codec.encode(message)

def decode(message):
    return hamming_codec.decode(message)

print(encode("testHamming"))

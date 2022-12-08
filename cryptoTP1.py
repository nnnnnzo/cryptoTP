from Crypto.Random import get_random_bytes

from prompt_toolkit.shortcuts import button_dialog, message_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import progress_dialog
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import yes_no_dialog

def cesar(phrase, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase_cryptee = ""
    phrase = phrase.lower()
    for lettre in phrase:
        if lettre in alphabet:
            position = alphabet.find(lettre)
            nouvelle_position = (position + n) % 26
            nouvelle_lettre = alphabet[nouvelle_position]
            phrase_cryptee = phrase_cryptee + nouvelle_lettre
        else:
            phrase_cryptee = phrase_cryptee + lettre
    return phrase_cryptee


print(cesar("abc", 4))


def breakcesar(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lettreatest = "eaisnrtolu"
    maxoc = 0
    phrase = phrase.lower()

    for lettre in phrase:
        newmaxoc = phrase.count(lettre)
        if newmaxoc > maxoc:
            maxoc = newmaxoc
            maxlettre = lettre

    for test in lettreatest:
        positiondecalage = alphabet.find(maxlettre) - alphabet.find(test)
        print(cesar(phrase, -positiondecalage))


print(breakcesar(cesar("les petits chats ces avions grand", 65)))

from aes_cipher import (FileEncrypter, FileDecrypter)

makey = "testaes"


def encrypt_file_aes(file_in, key):
    file_encrypter = FileEncrypter()
    file_encrypter.Encrypt(file_in, key)
    file_encrypter.SaveTo(file_in)


def decrypt_file_aes(file_in, key):
    file_decrypter = FileDecrypter()
    file_decrypter.Decrypt(file_in, key)
    file_decrypter.SaveTo(file_in)


# encrypt_file_aes("/Users/enzolagadec/Desktop/TP1.pdf", makey)
# decrypt_file_aes("/Users/enzolagadec/Desktop/TP1.pdf", makey)

file = input_dialog(
    title='Chemin du fichier',
    text='Entrez le chemin du fichier: ').run()

choiceMode = radiolist_dialog(
    title="Mode d'utilisation",
    text="Quel mode utiliser ?",
    values=[
        ("e", "Encrypter"),
        ("d", "Decrypter")
    ]
).run()
key = input_dialog(
    title='Clé',
    text='Entrez la clé: ').run()

if choiceMode == "e":
    encrypt_file_aes(file, key)
    message_dialog(
        title='Resultat',
        text='Fichier encrypté !').run()
elif choiceMode == "d":
    decrypt_file_aes(file, key)
    message_dialog(
        title='Resultat',
        text='Fichier decrypté !').run()

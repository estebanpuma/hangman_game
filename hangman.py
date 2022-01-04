import os, time

def start():
    welcome = '''                  **            ** ****** **     ****** ******* **     ** ******
                   **    **    **  **     **     **     **   ** ***   *** **
                    **  ****  **   ****   **     **     **   ** ** * * ** ****
                     ****  ****    **     **     **     **   ** **  *  ** **
                      **    **     ****** ****** ****** ******* **     ** ****** 

                   **  **     **     **    ** ****** **     **     **     **   **
                   **  **    ****    ***   ** **     ***   ***    ****    ***  **
                   ******   **  **   **  * ** **  ** ** * * **   **  **   ** * **
                   **  **  ********  **   *** **   * **  *  **  ********  **  ***
                   **  ** **      ** **    ** ****** **     ** **      ** **   **

                    ******     **     **     ** ******
                    **        ****    ***   *** **
                    **  **   **  **   ** * * ** ****
                    **   *  ********  **  *  ** **
                    ****** **      ** **     ** ******
             '''
    start_w = "A jugar"
    print(welcome)
    time.sleep(3)
    os.system ("cls")
    print(start_w)

def timeout():
    timer = 120
    for s in range (120):
        print(timer)
        time.sleep(1)
        timer -= 1
        os.system ("cls")
        if timer == 0:
            print("game over")


def player():
    player = input('Ingresa tu nombre: ')
    

def get_data():
    words = []
    with open('./files/data.txt','r', encoding= 'utf-8') as f:
        for word in f:
            words.append(word.strip('\n'))
    return words


def interface(words):
    word = words[0]
    guessed=[]
    cont = 0
    for letter in word:
        guessed.append('_')
        print(guessed[cont], end=' ')
        cont += 1
    letterin = ''
    while True:
        
        letter_guess = input('Ingresa una letra: ')
        letterin += letter_guess
        for letter in word:
            if letter_guess == letter:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        if word == letter_guess:
            break


def run():
    start()
    player()
    interface(get_data())
    
    


if __name__ == '__main__':
    run()
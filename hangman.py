import os, time

#Welcome to the game
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
    time.sleep(1)
    os.system ("cls")
    print(start_w)
    time.sleep(1)
    os.system ("cls")
#Max time for each game
def timeout():
    timer = 120
    for s in range (120):
        print(timer)
        time.sleep(1)
        timer -= 1
        os.system ("cls")
        if timer == 0:
            print("game over")

#player info
def player():
    player = input('Ingresa tu nombre: ')
    
# get data
def get_data():
    words = []
    with open('./files/data.txt','r', encoding= 'utf-8') as f:
        for word in f:
            words.append(word.strip('\n'))
    return words


def interface(words):
# char control (only lower letters)   
    word = list(words[3])
    special = ['á', 'é', 'í', 'ó', 'ú']
    standar = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        cont = 0
        for char in special:
            
            if word[i] == char:
                word[i] = standar[cont]
            cont += 1    
    print(word)

#show total spaces for the word
    guess_status = ['_' for letter in word ]
    for space in guess_status:
        print(space, end=' ')
    print("")
    #create a list with the acepted chars
    acepted_chars = [chr(i) for i in range(97,122) ] + list('ñ')
    #game cycle
    input_letters = ''
    while True:
        #input control
        while True:
            try:
                
                guessed_letter = (input('Ingresa una letra: ')).lower()
                os.system ("cls") 
                if guessed_letter not in acepted_chars:
                    raise TypeError
            except TypeError:
                print('Recuerda que solo debes ingresar letras')
            if len(guessed_letter) > 1:
                print('Solo ingresa una letra')
                
            else:
                break  
        
            
        input_letters += ' ' + guessed_letter
        
        
        print('Letras ingresadas', input_letters)
        for i in range(len(word)):
            if guessed_letter == word[i]:
                guess_status[i] = guessed_letter  
        for space in guess_status:
            print(space, end=' ')
        print("")

        if guess_status == list(word):
            break

    print('Felicidades')



def run():
    start()
    player()
    interface(get_data())
    
    


if __name__ == '__main__':
    run()
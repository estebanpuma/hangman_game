import os, time

firsterror = '''
                *
                *
                *
                *
               * *
              *****
            
            '''
secerror = '''
                ********
                *
                *
                *
               * *
              *****
            
            '''
thirderror = '''
                ********
                *      O
                *
                *
               * *
              *****
            
            '''
fourtherror = '''
                ********
                *      O
                *      |
                *
               * *
              *****
            
            '''
fiftherror = '''
                ********
                *      O
                *    --|--
                *
               * *
              *****
            
            '''
sixerror = '''
                ********
                *      O
                *    --|--
                *     / \ 
               * *
              *****
            GAME OVER....!!!!
            '''

#Welcome to the game
def start():
    os.system ("cls")
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
    players=[]
    players.append(player)
    
# get data
def get_data():
    words = []
    with open('./files/data.txt','r', encoding= 'utf-8') as f:
        for word in f:
            words.append(word.strip('\n'))
    return words


def interface(words):
# char control (only lower letters)   
    points = 100
    rounds = 0
    while rounds<=len(words):
        
        word = list(words[rounds])
        rounds += 1
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
        jugadas = 0
        errors = 0
        
        while True:
            #input control
            while True:
                try:
                    
                    guessed_letter = (input('Ingresa una letra: ')).lower()
                    os.system ("cls") 
                    if len(guessed_letter) > 1:
                        print('Solo ingresa una letra')
                        break
                    elif guessed_letter not in acepted_chars:
                        raise TypeError
                except TypeError:
                    print('Recuerda que solo debes ingresar letras')
                    break   
                else:
                    break  
            
            
            if guessed_letter in acepted_chars:       
                input_letters += ' ' + guessed_letter
                jugadas += 1
                
            print('Letras ingresadas:', input_letters)
            
            
            for i in range(len(word)):
                if guessed_letter == word[i]:
                    guess_status[i] = guessed_letter
                

            for space in guess_status:
                print(space, end=' ')
            print("")

            if guessed_letter not in word:
                errors += 1
            if errors == 0:
                points += 0    
                
            if errors == 1:
                points -=10
                print(firsterror)
            elif errors == 2:
                points -=20
                print(secerror)
            elif errors == 3:
                points -=30
                print(thirderror)
            elif errors == 4:
                points -=40
                print(fourtherror)
            elif errors == 5:
                points -=50
                print(fiftherror)
            elif errors == 6:
                points -=100
                print(sixerror)
                print('Puntos: ', points)
                time.sleep(2)
                break

            if guess_status == list(word):
                print('Felicidades. Ganaste!!!')
                print('Puntos: ', points)
                points += 100
                time.sleep(2)
                break

        

    



def run():
    start()
    player()
    interface(get_data())
    
    


if __name__ == '__main__':
    run()
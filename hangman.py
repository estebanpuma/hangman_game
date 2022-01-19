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
    points = 0
    rounds = 0
    while rounds<=len(words):
        rounds += 1
        word = list(words[rounds])
        points += 100
        special = ['á', 'é', 'í', 'ó', 'ú']
        standar = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(word)):
            cont = 0
            for char in special:
                
                if word[i] == char:
                    word[i] = standar[cont]
                cont += 1    
        

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
                points -= 16  
                
            if errors == 1:
                print(firsterror)

            elif errors == 2:
                print(secerror)

            elif errors == 3:
                print(thirderror)

            elif errors == 4: 
                print(fourtherror)

            elif errors == 5:               
                print(fiftherror)

            elif errors == 6:      
                points -= 4         
                print(sixerror)
                print('Puntos: ', points)
                time.sleep(2)
                exit()
                break

            if guess_status == list(word):
                print('Felicidades. Ganaste!!!')
                print('Puntos: ', points)
                time.sleep(2)
                os.system ("cls")
                break

        

    



def run():
    start()
    player()
    interface(get_data())
    
    


if __name__ == '__main__':
    run()
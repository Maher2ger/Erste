import sys
import os
def game():    
         #head

    print('     ╔═══════════════════════════════════════════════════╗')
    print('     ║                                                   ║')
    print('     ║     ██     ██    █    ████     ████               ║')
    print('     ║      █     █     █    █        █   █              ║')
    print('     ║      ██   ██     █    ████     ████    gewinnt!!  ║')
    print('     ║       ██ ██      █    █        █  ██              ║')
    print('     ║        ███       █    ████     █   █              ║')
    print('     ║                                                   ║')
    print('     ║          Maher & Marco                            ║')
    print('     ║                                                   ║')
    print('     ║                                                   ║')
    print('     ╚═══════════════════════════════════════════════════╝')
    print()
    print('        ****Der erste Spieler hat diese Figur "X" .****')
    print('        ****Der zweite Spieler hat diese Figur "O" .***')
    print()

    first_player = input("what is the name of the first Player?: ")
    print("welcome "+first_player+', your symbol is"X".')
    second_player = input("what is the name of the second Player?: ")
    print("welcome ",second_player+', your is symbol"O".')
    
    
    SA = ["_","_","_","_","_","_","_","_"]          #Zeile : A
    SB = ["_","_","_","_","_","_","_","_"]          #Zeile : B
    SC = ["_","_","_","_","_","_","_","_"]
    SD = ["_","_","_","_","_","_","_","_"]
    SE = ["_","_","_","_","_","_","_","_"]
    SF = ["_","_","_","_","_","_","_","_"]

    def spielfeld():
            print('      ',"  1  "," 2 ","  3 ","  4 ","  5 ","  6 ","  7 ","  8 ")

            print('      ',"  ▼  "," ▼ ","  ▼ ","  ▼ ","  ▼ ","  ▼ ","  ▼ ","  ▼ ")
            print('      ',SA,"        press ’I’ for more informations.")
            print('      ',SB,"        press ’X’ to exit the game.")
            print('      ',SC,"        press ’R’ to restart the game. ")
            print('      ',SD)
            print('      ',SE)
            print('      ',SF)
            print()
    spielfeld()
                                #gueltige Eingaben
    gueltige_Eingaben = ["1","2","3","4","5","6","7","8",]
    gueltige_Eingaben2 = ["X" , "I" ,"H","R"]

    def infos():
        print("valid inputs are the numbers from 1 to 8")
        print("also 'I' for more information, 'R' to restart the game")
        print("'X' to exit the game. Attention:The scores will be nullified ")
        print("when you restart the game.")
        

    def gewonnen1():            #Der ERSTE Spieler hat gewonnen 
            print("******************************************************")
            print("*♥♥♥♥♥♥♥♥ツ "+first_player+" hat gewonnen ☑♥♥♥♥♥♥♥♥♥*")
            print("******************************************************")
            what_now = input("to play again press 'R' or press any key to exit the game: ")
            if what_now == "R":
                                print()
                                print("************a new game is started***************")
                                print()
                                game()
            else:
                                sys.exit()
    def gewonnen2():            #Der ZWEITE Spieler hat gewonnen
            print("*********************************************************")
            print("*♥♥♥♥♥♥♥♥ ツ "+second_player+" hat gewonnen ☑♥♥♥♥♥♥♥♥♥♥*")
            print("*********************************************************")
            what_now = input("to play again press 'R' or press any key to exit the game: ")
            if what_now == "R":
                                print()
                                print("************a new game is started***************")
                                print()
                                game()
            else:
                                sys.exit()
    def undecided():
        if "_" not in SA:
            print("*********** no one is a winner ************")
            what_now = input("to play again press 'R' or press any key to exit the game: ")
            if what_now == "R":
                                print()
                                print("************a new game is started***************")
                                print()
                                game()
            else:
                                sys.exit()
                                
    def gewinn_testen():                #gewinnfaelle
            def sa(x):                  #der erste Fall : erste  Zeile
                while x <5:             
                    if SA[x] == "X" and SA[x+1] == "X" and SA[x+2] == "X" and (SB[x] == "X" or SB[x+2] == "X"):
                        gewonnen1()
                    elif SA[x] == "O" and SA[x+1] == "O" and SA[x+2] == "O" and (SB[x] == "O" or SB[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return sa(x+1)
            sa(0)
            
            
            def sb(x):                  #der zweite Fall : zweite Zeile 
                while x <5:
                    if SB[x] == "X" and SB[x+1] == "X" and SB[x+2] == "X" and (SA[x] == "X" or SA[x+2] == "X"  or SC[x] == "X"    or SC[x+2] == "X"):
                        gewonnen1()
                                
                    elif SB[x] == "O" and SB[x+1] == "O" and SB[x+2] == "O" and (SA[x] == "O" or SA[x+2] == "O" or SC[x] == "O"    or SC[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return sb(x+1)
            sb(0)
            
            
            def sc(x):                  #der dritte Fall : dritte Zeile 
                while x <5:
                    if SC[x] == "X" and SC[x+1] == "X" and SC[x+2] == "X" and (SB[x] == "X" or SB[x+2] == "X"  or SD[x] == "X"    or SD[x+2] == "X"):
                        gewonnen1()
                    elif SC[x] == "O" and SC[x+1] == "O" and SC[x+2] == "O" and (SB[x] == "O" or SB[x+2] == "O" or SD[x] == "O"    or SD[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return sc(x+1)
            sc(0)
            
            def sd(x):
                while x <5:
                    if SD[x] == "X" and SD[x+1] == "X" and SD[x+2] == "X" and (SC[x] == "X" or SC[x+2] == "X"  or SE[x] == "X"    or SE[x+2] == "X"):
                        gewonnen1()
                    elif SD[x] == "O" and SD[x+1] == "O" and SD[x+2] == "O" and (SC[x] == "O" or SC[x+2] == "O" or SE[x] == "O"    or SE[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return sd(x+1)
            sd(0)
            
            def se(x):
                while x <5:
                    if SE[x] == "X" and SE[x+1] == "X" and SE[x+2] == "X" and (SD[x] == "X" or SD[x+2] == "X"  or SF[x] == "X"    or SF[x+2] == "X"):
                        gewonnen1()
                    elif SE[x] == "O" and SE[x+1] == "O" and SE[x+2] == "O" and (SD[x] == "O" or SD[x+2] == "O" or SF[x] == "O"    or SF[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return se(x+1)
            se(0)
            
            
            def sf(x):
                while x <5:
                    if SF[x] == "X" and SF[x+1] == "X" and SF[x+2] == "X" and (SE[x] == "X" or SE[x+2] == "X"):
                        gewonnen1()
                    elif SF[x] == "O" and SF[x+1] == "O" and SF[x+2] == "O" and (SE[x] == "O" or SE[x+2] == "O"):   
                        gewonnen2()
                    else:
                        return sf(x+1)
            sf(0)
            
            
            def sp1(x):                     #erste 3 Zeile
                    while x < 8:
                        if SA[x] == "X" and SB[x] == "X" and SC[x] == "X" and (SA[x+1] == "X" or SC[x+1] == "X" or SA[x-1] == "X" or SC[x-1] == "X"):
                            gewonnen1()
                        elif SA[x] == "O" and SB[x] == "O" and SC[x] == "O" and (SA[x+1] == "O" or SC[x+1] == "O" or SA[x-1] == "O" or SC[x-1] == "O"):
                            gewonnen2()
                        else:
                            return sp1(x+1)
            sp1(0)

            def sp2(x):                     #zeile 2 , 3 , 4
                    while x < 8:
                        if SB[x] == "X" and SC[x] == "X" and SD[x] == "X" and (SB[x+1] == "X" or SD[x+1] == "X" or SB[x-1] == "X" or SD[x-1] == "X" ):
                            gewonnen1()
                        elif SB[x] == "O" and SC[x] == "O" and SD[x] == "O" and (SB[x+1] == "O" or SD[x+1] == "O" or SB[x-1] == "O" or SD[x-1] == "O" ):
                            gewonnen2()
                        else:
                            return sp2(x+1)

            sp2(0)

            def sp3(x):                 #Zeile 3,4,5
                    while x < 8:
                        if SC[x] == "X" and SD[x] == "X" and SE[x] == "X" and (SC[x+1] == "X" or SE[x+1] == "X" or SC[x-1] == "X" or SE[x-1] == "X" ):
                            gewonnen1()
                        elif SC[x] == "O" and SD[x] == "O" and SE[x] == "O" and (SC[x+1] == "O" or SE[x+1] == "O" or SC[x-1] == "O" or SE[x-1] == "O" ):
                            gewonnen2()
                        else:
                            return sp3(x+1)

            sp3(0)  

            def sp4(x):                 #Zeile 4,5,6
                    while x < 8:
                        if SD[x] == "X" and SE[x] == "X" and SF[x] == "X" and (SD[x+1] == "X" or SF[x+1] == "X" or SD[x-1] == "X" or SF[x-1] == "X" ):
                            gewonnen1()
                        elif SD[x] == "O" and SE[x] == "O" and SF[x] == "O" and (SD[x+1] == "O" or SF[x+1] == "O" or SD[x-1] == "O" or SF[x-1] == "O" ):
                            gewonnen2()
                        else:
                            return sp4(x+1)

            sp4(0)


            
            
                
    the_next_player = True
    
            
            

    def S1():                   #Der erste Spieler
            w = input(first_player +" Wählen Sie eine Spalte : ")   #eine Spalte wählen
            
            
                           
            if w in gueltige_Eingaben2:
                            if w == "X":
                                 Exit = input("to exit the game press Y or \
press any key to return to the game:")
                                 if Exit == "Y":
                                    print("****************GAME OVER********************")
                                    sys.exit()
                                 else:
                                    return S1()
                            elif w == "R":
                                Restart = input("to restart the game press Y \
or press any key to return to the game :")
                                if Restart == "Y":
                                    print()
                                    print("************a new game is started***************")
                                    print()
                                    game()
                                else:
                                    return S1()
                            elif w == "I":
                                infos()
                                return S1()
                                
            
                            else:
                                return S1()
            elif w in gueltige_Eingaben:
                           w = int(w) -1
                
                           
            else:
                        print('Falsche Eingabe')
                        return S1()
            def wahl(w): 
                        if SF[w]  == "_":
                            SF[w] = "X"
                        elif SE[w] == "_":
                            SE[w] = "X"
                        elif SD[w]  == "_":
                            SD[w] = "X"
                        elif SC[w]  == "_":
                            SC[w] = "X"
                        elif SB[w]  == "_":
                            SB[w] = "X"
                        elif SA[w]  == "_":
                            SA[w] = "X"
                        
                        else:
                            print('Sie können hier keine Steine mehr drauf legen')
                            return S1()
            
            wahl(w)
        
            print(spielfeld())
            gewinn_testen()
            undecided()
            
            
    def S2():               #Der zweite Spieler
            w2 = input(second_player+" Wählen Sie eine Spalte : ")   
            if w2 in gueltige_Eingaben2:
                            if w2 == "X":
                                 Exit = input("to exit the game press Y or \
press any key to return to the game :")
                                 if Exit == "Y":
                                    print("****************GAME OVER********************")
                                    sys.exit()
                                 else:
                                    return S2()
                            elif w2 == "R":
                                    Restart = input("to restart the game press Y \
or press any key to return to the game :")
                                    if Restart == "Y":
                                        print()
                                        print("************a new game is started***************")
                                        print()
                                        game()
                                    else:
                                        return S2()
                            elif w2 == "I":
                                infos()
                                return S2()
                            else:
                                return S2()
            elif w2 in gueltige_Eingaben:
                w2 = int(w2) - 1
                            
            else:
                        print('Falsche Eingabe')
                        return S2()
              
            
            def wahl1(w2):
                
                        
                        if SF[w2]  == "_":
                            SF[w2] = "O"
                        elif SE[w2] == "_":
                            SE[w2] = "O"
                        elif SD[w2]  == "_":
                            SD[w2] = "O"
                        elif SC[w2]  == "_":
                            SC[w2] = "O"
                        elif SB[w2]  == "_":
                            SB[w2] = "O"
                        elif SA[w2]  == "_":
                            SA[w2] = "O"
                        
                        else:
                            print('Sie können hier keine Steine mehr drauf legen')
                            return S2()
            
            wahl1(w2)
            print(spielfeld())
            gewinn_testen()
            undecided() 
                    
                    
                    
            
            
        
        

    while the_next_player == True: # this will loop until invalid_input is set to be True
        S1()
        S2()
game()    #restart the game

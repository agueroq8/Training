print('Welcome to Baloot Calculator')
TeamA=0
TeamB=0

while (TeamA or TeamB) <=152:
    TeamA +=int(input('Team A Score : '))
    TeamB +=int(input('Team B Score : '))
    print(f'''Team A     || Team B
{ TeamA}         || {TeamB}''')
    if (TeamA >= 152 and TeamA>TeamB):
        print(f'The Winner is Team A {TeamA}')
    elif (TeamB >= 152 and TeamB>TeamA):
        print(f'The Winner is Team B {TeamB}')
    elif (TeamA and TeamB >= 152):
        if TeamA > TeamB:
            print(f'The Winner is Team A {TeamA}')
        elif TeamB >TeamA:
            print(f'The Winner is Team B {TeamB}')
        elif TeamA == TeamB:
            print('The Winner Who Buys The Last Round')
            
        

    
    

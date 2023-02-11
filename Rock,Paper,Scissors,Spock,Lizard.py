import random

while True:
 def game(choise,result):
     print('===Start Game===')
     comp_choise = random.choice('rpsspl')
     print('----------------')
     print('Your Select - ', str.capitalize(choise))
     print('Comp Select -', str.capitalize(comp_choise))
     if str.lower(choise) == comp_choise:
        print('Result: friendly End:)')
     elif str.lower(choise) == 'r' and comp_choise =='p':
        result['comp'] += 1
        print('----Comp Win----')
     elif str.lower(choise) == 'r' and comp_choise =='s':
        result['player'] += 1
        print('----Player Win----')      
     elif str.lower(choise) == 'p' and comp_choise =='r':
        result['player'] += 1
        print('----Player Win----')    
     elif str.lower(choise) == 'p' and comp_choise =='s':
        result['comp'] += 1
        print('----Comp Win----')    
     elif str.lower(choise) == 's' and comp_choise =='r':
        result['comp'] += 1
        print('----Comp Win----')    
     elif str.lower(choise) == 'l' and comp_choise =='p':
        result['player'] += 1
        print('----Player Win----')    
     elif str.lower(choise) == 'l' and comp_choise =='r':
        result['comp'] += 1
        print('----Comp Win----')    
     elif str.lower(choise) == 'l' and comp_choise =='sp':
        result['player'] += 1
        print('----Player Win----')    
     elif str.lower(choise) == 'sp' and comp_choise =='r':
        result['player'] += 1
        print('----Player Win----')  
     elif str.lower(choise) == 'sp' and comp_choise =='s':
        result['player'] += 1
        print('----Player Win----')  
     elif str.lower(choise) == 'sp' and comp_choise =='p':
        result['comp'] += 1
        print('----Comp Win----')  
     elif str.lower(choise) == 'l' and comp_choise =='s':
        result['comp'] += 1
        print('----Comp Win----')  
 
 result = {'comp': 0, 'player': 0}
 choise = input('Select R /P / S/ Sp/ L/:')
 game(choise, result)
 print(result)
from random import choice

'''Salt Analysis via a code typed into the IDLE
            
Hard-coding everything
Heavy usage of dictionaries'''

#a help message
helpMsg = '''Use the given code words to do a certain task for finding out the given salt.
All chemicals should be referred to by their chemical formula.
Intensity of heating code words are listed below.

Intensity Code:-
Intensity          : Codename
Heat Very Strongly : strong
Heat Very Slightly : slight

The code is case sensitive. There should a space between every single key word. It removes any unnecessary spaces/symbols from yout input.
Note: wherever you want to add the given salt as the chemical, use the keyword salt.

All functions:
'new' :- Picks a new salt. If used while an old salt is still being analysed, it deducts a massive amount of points and gives you the answer.

'list *' :- Prints a list of all the chemicals. If u put a specific category instead of *, then it lists out all chemicals in that category
            a. 'acids' :- Lists out all acids
            b. 'reag' :- Lists out all special reagents and indicators
            c. 'misc' :- Miscellanoeus stuff like water, paper pellets, etc

'add <chemical name> [to <tube>]' :- adds the chemical in the specified test tube. Test tube not specified, then adds to last used test tube. Can add contents of one test tube into the other, specify test tube number rather than chemical name.

'heat [<intensity> [<tube>]] :- heats the mentioned test tube (default test tube is the last used one) with a given intensity (slight heating by default)

'flame test' :- Carries out flame test on your given salt

'guess <ion> is <name>' :- Give your guess for the specified ion ('cation' or 'anion'). If right, gain points. If wrong lose points.

'pass in <tube>' :- Pass the evolved gas in the previous reaction (if any) into a specified test tube

'introduce <chemical> [to <tube>]' :- Introduce the chemical to the test tube (default test tube is last one used) by a glass rod

'create SE' :- Create the Sodium Carbonate Extract

'create WE' :- Create the Water Extract

'create OS' :- Create the Original Salt Solution

'quit' :- Quit out of Salt Analysis Emulator. Gives you the answer to the old salt, if a salt is stil being analysed.

'new tube' :- Take a new test tube

'discard <tube>' :- Remove the specified test tube

Here, test tubes also refer to boiling tubes, so don't worry about that.
Also there is no limit to the number of test tubes you can take.
If you want information as to a certain test, please refer to your lab manual :)''' 

def codeError():
    print 'ERROR! Please recheck what you have typed'

def Quit():
    if salt != [None, None]:
        ch = raw_input('Are you sure? Press y to proceed, anything else to return>>> ').lower()
        if ch == 'y':
            formula, name = saltFormula()
            print 'The salt was %s, with formula %s'%(name, formula)
        else: return
    print 'THANK YOU FOR USING THE SALT ANALYSIS EMULATOR.'
    quit()

def printtubes():
    print
    for i in range(len(tubes)):
        if not (tubes[i]['contents'] == []):
            output = 'Test Tube %d has'%(i+1)
            for chemical in tubes[i]['contents']:
                output += (' ' + str(chemical) + ',')
            output = output[:-1] + '.'
            if tubes[i]['heated']:
                output += 'It has been heated %s.'%('slightly' if tubes[i]['heated'] == 1 else 'strongly')
            if tubes[i]['colour']:
                output += 'Its colour is %s.'%(tubes[i]['colour'])
            print output
        else:
            print 'Test tube %d is empty'%(i+1)
    print 'Current Test Tube:' , currenttubeindex + 1
    
#ALL CHEMICALS LISTS
acids_list = [{'dil_HCl':'Diluted Hydrochloric acid'}, {'conc_HCl':'Concentrated Hydrochloric acid'},
              {'dil_H2SO4':'Diluted Sulphuric acid'}, {'conc_H2SO4':'Concentrated Sulphuric acid'},
              {'dil_HNO3':'Diluted Nitric acid'}, {'conc_HNO3':'Concentrated Nitric acid'}, {'CH3COOH':'Acetic Acid'}]
misc_list = [{'water':'water'}, {'paper':'Paper Pellets'}, {'LApaper':'Lead Acetate paper'}, {'ADpaper':'Acidified Dichromate Paper'},
             {'Moist Starch Paper':'MSpaper'}, {'Moist Starch Iodide Paper':'MSIpaper'}, {'Moist Blue Litmus Paper':'MBLpaper'}]
# Add more reagents specific to certain tests for new cations/anions
reag_list = [{'NH4OH':'Ammonium hydroxide'}]

acids = [acid.keys()[0] for acid in acids_list]
misc = [misc.keys()[0] for misc in misc_list]
reagents = [reag.keys()[0] for reag in reag_list]

def List(category):
    if category == '*':
        print 'ACIDS:'
        for chemical in acids:
            print chemical , ' - ', acids_list[chemical]
        print'\nREAGENTS'
        for chemical in reagents:
            print chemical , ' - ', reag_list[chemical]
        print '\nMISCELLANEOUS'
        for chemical in misc:
            print chemical , ' - ', misc_list[chemical]
    elif category == 'acids':
        for chemical in acids:
            print chemical , ' - ', acids_list[chemical]
    elif category == 'misc':
        for chemical in misc:
            print chemical , ' - ', misc_list[chemical]
    elif category == 'reag': 
        for chemical in reagents:
            print chemical , ' - ', reag_list[chemical]

def saltFormula():  #write code to return the formula as string
    name = salt[0]['name'] + ' ' + salt[1]['name']
    if salt[0]['valency'] == salt[1]['valency']:
        formula = salt[0]['formula'] + salt[1]['formula']
    elif salt[0]['formula'] == 'NH4':
        formula = '(NH4)%d%s'%(salt[1]['valency'], salt[1]['formula'])
    elif salt[0]['valency'] == 1:
        formula = '%s%d%s'%(salt[0]['formula'], salt[1]['valency'], salt[1]['formula'])
    elif len(salt[1]['formula']) > 2:
        formula = '%s%d(%s)%d'%(salt[0]['formula'], salt[1]['valency'], salt[1]['formula'], salt[0]['valency'])
    else: #len(salt 1 formula) <= 2
        formula = '%s%d%s%d'%(salt[0]['formula'], salt[1]['valency'], salt[1]['formula'], salt[0]['valency'])
    return formula, name 

def newSalt():
    global salt, saltflag, tubes
    if salt != [None, None]:
        ch = raw_input('Are you sure? Press y to proceed, anything else to exit>>> ').lower()
        if ch == 'y':
            formula, name = saltFormula()
            print 'The salt was %s, with formula %s'%(name, formula) 
        else: return
    salt[0] = choice(cations)
    salt[1] = choice(anions)
    print
    print 'A salt has been chosen'
    if salt[0]['colour'] != None: print 'Colour -' , salt[0]['colour']
    else: print 'No recognizable colour'
    if salt[0]['odour'] != None and salt[1]['odour'] != None: print 'Mix of smells detected'
    elif salt[0]['odour'] != None: print 'Odour -' , salt[0]['odour'], 'Smell'
    elif salt[1]['odour'] != None: print 'Odour -' , salt[1]['odour'], 'Smell'
    else: print 'No recognizable odour'
    tubes = list()
    tubes.append(new_tube())
    saltflag = [False, False]

def guess(ion, name):
    dictionary = {'cation':0, 'anion':1}
    index = dictionary[ion]
    if saltflag[index] == True:
        print 'You have already guessed the %s, try to guess the other ion.'%(ion)
        return
    if name == salt[index]['formula']:
        print 'CORRECT! The %s was %s, with formula %s' % (ion, salt[index]['name'], salt[index]['formula'])
        saltflag[index] = True
    else:
        print 'Wrong guess :/'
    if saltflag == [True, True]:
        print 'GREAT! YOU HAVE GUESSED THE SALT.'
        formula, name = saltFormula()
        print 'The salt was indeed %s, with formula %s.' % (name, formula)
        reset()

def reset():
    global salt, saltflag, tubes, currenttubeindex
    salt = [None, None]  #Use this as a flag to check whether new salt has been picked
    saltflag = [False, False]  #use this as a flag to check whether a salt has been guessed correctly
    tubes = list()
    tubes.append(new_tube()) 

def new_tube(chemical = None):
    global currenttubeindex
    tube = {'contents':list(), 'heated':0, 'colour':None, 'gas':None}
    #0 - not heated, 1 - slightly heated, 2 - strongly heated
    #'gas' value is to keep track of what gas is being emitted
    if chemical != None: tube['contents'].append(chemical)
    currenttubeindex = len(tubes)
    return tube

def discard(index):
    global tubes, currenttubeindex
    if tubes[index]['contents'] == []:
        del tubes[index]
        currenttubeindex = 0
    else:
        ch = raw_input('This test tube is not empty. Are you sure you want to discard this tube? Press y to continue: ').lower()
        if ch == 'y':
            del tubes[index]
            currenttubeindex = 0
    if len(tubes) == 0:
        tubes.append(new_tube())

def heat(code):
    global tubes, currenttubeindex
    if len(code) == 1:
        index = currenttubeindex
        heat = 1
    elif len(code) == 2:
        index = currenttubeindex
        heat = 2 if code[-1] == 'strongly' else 1
    elif len(code) == 3 and code[2][0] == 't' and code[1] in ('slightly', 'strongly'):
        index = int(code[1][1]) - 1
        heat = 2 if code[-1] == 'strongly' else 1
    else:
        codeError()
        return
    if tubes[index]['contents'] != [None]:
        tubes[index]['heated'] = heat
        currenttubeindex = index
    else:
        print 'Test Tube %d is empty. It can\'t be heated'%(index+1)
    prelim_tests()
    

def add(chemical, index = None):
    global currenttubeindex, tubes
    if index == None: index = currenttubeindex
    
    if chemical[0] == 't': #if adding one test tube into another
        emptiedindex = int(chemical[-1]) - 1
        tubes[index]['contents'].extend(tubes[emptiedindex]['contents'])
        currenttubeindex = index
        tubes[emptiedindex] = new_tube()
    else:
        if not (chemical in reagents or chemical in acids or chemical in misc or chemical == 'salt'): return 'error'
        tubes[index]['contents'].append(chemical)
        currenttubeindex = index
    solubility_test()
    prelim_tests()

#FUNCTIONS FOR TESTS
#These functions should be placed in the add() function (except for flame test, there's a keyword for that)
#If heating is required for some of the tests, put it under the heating function

def flame_test():
    if salt[0]['flame'] != None:
        print 'The flame is %s in colour' % (salt[0]['flame'])
    else:
        print 'No characteristic flame colour'

def solubility_test():
    i = currenttubeindex
    if sorted(tubes[i]['contents']) == sorted(['salt', 'water']): #test for solubility in water
        print
        if salt[1]['formula'] == 'CO3': print 'Salt insoluble in water'
        else: print 'Salt soluble in water'
    elif sorted(tubes[i]['contents']) == sorted(['salt', 'dil_HCl']): #test for solubility in dil HCl
        print
        if salt[0]['formula'] == 'Pb':
            print 'White precipitate is formed'
            tubes[i]['colour'] = 'white'
        else: print 'Soluble in dil_HCl'

def prelim_tests():
    global tubes
    i = currenttubeindex
    
    if sorted(tubes[i]['contents']) == ['dil_HCl', 'salt']: #dilute acid test
        if salt[1]['formula'] == 'CO3':
            print '\nColourless, odourless gas evolved.'
            tubes[i]['gas'] = 'CO2'
        elif tubes[i]['heated']: #only CO3 reaction takes place without heat
            if salt[1]['formula'] == 'S':
                print '\nGas with rotten egg smell evolved'
                tubes[i]['gas'] = 'H2S'
            elif salt[1]['formula'] == 'NO2':
                print '\nSlight brown fumes evolved'
                tubes[i]['gas'] = 'NO'
            elif salt[1]['formula'] == 'SO3':
                print '\nGas with burning sulphur smell evolved'
                tubes[i]['gas'] = 'SO2'
        
    if sorted(tubes[i]['contents']) == ['conc_H2SO4', 'salt']:
        if salt[1]['formula'] == 'Cl':
            print '\nColourless gas with irritating smell'
            tubes[i]['gas'] = 'HCl'
        elif tubes[i]['heated']: #only Cl reaction takes place without heat
            if salt[1]['formula'] == 'Br':
                print '\nReddish brown gas evolved'
                tubes[i]['gas'] = 'Br2'
            elif salt[1]['formula'] == 'I':
                print '\nViolet vapours evolved'
                tubes[i]['gas'] = 'I2'
            elif salt[1]['formula'] == 'CH3COO':
                print '\nGas with vinegar smell evolved'
                tubes[i]['gas'] = 'CH3COOH'
            elif salt[1]['formula'] == 'NO3':
                print '\nSlight brown fumes evolved'
                tubes[i]['gas'] = 'NO'
    
            
#Actual loop for taking inputs-
print '''WELCOME TO SALT ANALYSIS EMULATOR!

A randomly generated salt is analyzed via a simple code

To find out about the syntax for the code, type help.
If you want to start analysing a salt, type new'''

#Dictionary for each cation/anion
#anions:
carbonate = {'name':'carbonate', 'type':'anion', 'formula':'CO3', 'valency':2, 'odour':None}
sulphide = {'name':'sulphide', 'type':'anion', 'formula':'S', 'valency':2, 'odour':'Rotten egg'}
nitrite = {'name':'nitrite', 'type':'anion', 'formula':'NO2', 'valency':1, 'odour':None}
sulphite = {'name':'sulphite', 'type':'anion', 'formula':'SO3', 'valency':2, 'odour':None}
chloride = {'name':'chloride', 'type':'anion', 'formula':'Cl', 'valency':1, 'odour':None}
bromide = {'name':'bromide', 'type':'anion', 'formula':'Br', 'valency':1, 'odour':None}
iodide = {'name':'iodide', 'type':'anion', 'formula':'I', 'valency':1, 'odour':None}
acetate = {'name':'acetate', 'type':'anion', 'formula':'CH3COO', 'valency':1, 'odour':'Vinegar'}
nitrate = {'name':'nitrate', 'type':'anion', 'formula':'NO3', 'valency':1, 'odour':None}
sulphate = {'name':'sulphate', 'type':'anion', 'formula':'SO4', 'valency':2, 'odour':None}
phosphate = {'name':'phosphate', 'type':'anion', 'formula':'PO4', 'valency':3, 'odour':None}
anions = [sulphide, carbonate, nitrite, chloride, bromide, iodide, sulphate, phosphate]
#cations
ammonium = {'name':'Ammonium', 'type':'cation', 'formula':'NH4', 'valency':1, 'odour':'Ammoniacal', 'flame':None, 'colour':None} 
lead = {'name':'Lead', 'type':'cation', 'formula':'Pb', 'valency':2, 'odour':None, 'flame':None, 'colour':None} 
cations = [ammonium, lead]

reset()

while True:
    print
    codestring = raw_input('Enter code line >>> ').rstrip().lstrip()
    code = codestring.split()  #retreive individual keyword
    code = [word for word in code if word.isalnum() or word == '*' or \
            (word in reagents or word in acids or word in misc or word == 'salt')]  #remove any junk, spaces etc
    if code[0] == 'help':
        if len(code) == 1:
            print helpMsg
        else:
            codeError()
    elif code[0] == 'quit':
        if len(code) == 1: Quit()
        else: codeError()
    elif code[0] == 'list':
        if len(code) != 2: codeError()
        else: List(code[1])
    elif code[0] == 'new':
        if len(code) == 1:newSalt()
        elif code[1] == 'tube':
            if len(code) != 2: codeError()
            else:
                tubes.append(new_tube())
        else: codeError()
        
    if salt == [None, None]: continue
    
    if code[0] == 'add':
        if len(code) == 4 and code[2] == 'to':
            errorstring = add(code[1], int(code[-1][-1]) - 1)
        elif len(code) == 2:
            errorstring = add(code[-1])
        else:
            errorstring = 'error'
        if errorstring == 'error': codeError()
    elif code[0] == 'create':
        if len(code) != 2: codeError()
        elif code[1] in ('OS', 'SE', 'WE'):
            tubes.append(new_tube(code[1]))
    elif code[0] == 'heat':
        heat(code)
    elif code == ['flame', 'test']: flame_test()
    elif code[0] == 'guess' and code[1] in ('cation', 'anion') and code[2] == 'is' and \
         (code[3] in [ion['formula'] for ion in (cations+anions)]):
        guess(code[1], code[3])
    elif code[0] == 'discard' and code[1][0] == 't':
        discard(int(code[1][1]) - 1)
        
    if salt != [None, None]: printtubes()







    


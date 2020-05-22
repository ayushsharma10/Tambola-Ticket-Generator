# Loading Libraries
import numpy as np
import pandas as pd
import itertools
import random


def generate_ticket():
    
    #Design
    design = [1,1,1,2,2,2,2,2,2]
    design_combination = list(set(itertools.permutations(design, 9)))
    selected_design = list(design_combination[np.random.randint(low= 0, high = len(design_combination))])
    
    #Alignment
    alignment = [4,3,2,2,2,2]
    alignment_combination = list(set(itertools.permutations(alignment, 6)))
    selected_alignment = list(alignment_combination[np.random.randint(low= 0, high = len(alignment_combination))])
    
    insert_one_index = []
    for i in range(9):
        if selected_design[i] == 1:
            insert_one_index.append(i)
            
    for i in insert_one_index:
        selected_alignment.insert(i,1)
        
    #Adding values
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []
    r6 = []
    r7 = []
    r8 = []
    r9 = []
    matrix = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

    for i,j in enumerate(selected_design):
        while len(matrix[i]) < j:
            if i == 0:
                num = np.random.randint(low= i*10 + 1, high = (i+1)*10)
            
            else:
                num = np.random.randint(low= i*10, high = (i+1)*10)
                
            if num not in matrix[i]:
                matrix[i].append(num)
                matrix[i] = sorted(matrix[i])
                
    
    #Formatting
    for i,j in enumerate(selected_alignment):
        if j == 1:
            matrix[i].insert(0,'  ')
            matrix[i].insert(2,'  ')
        elif j == 2:
            matrix[i].insert(1,'  ')
        elif j == 3:
            matrix[i].insert(2,'  ')
        else:
            matrix[i].insert(0,'  ')
            
    ticket = pd.DataFrame(np.array(matrix).T)
    ticket.rename(columns = {i:j for i,j in zip(range(0,9), ['']*9)}, inplace = True)
    ticket.rename(index = {i:j for i,j in zip(range(0,3), ['']*3)}, inplace = True )
    
    #Getting ticket
    return(ticket)

    
    
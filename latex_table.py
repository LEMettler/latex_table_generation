#!/usr/bin/env python
# coding: utf-8

import numpy as np
def generateLatexTable(*args_values, column_names=None, round_values=None, seperate_values=False,
                       table_caption='', table_label='', booktabs=True, file_name=None):
    '''
    Convert argument arrays to code for a LaTeX-Table in form of a String/File.

    :args_values: arrays containing the column values (lists, numpy arrays)
    :column_names: names of columns, (list, numpy array; default=None)
    :round_values: decimal place to round to (int, list, numpy array; default=None)
    :seperate_values: split args_values into seperate arrays, if args_values are arrays for each row set to True,
                    if args_values are arrays for each column set to False (Boolean, default=False)
    :table_caption: LaTeX caption of table (String; default='')
    :table_label: LaTeX label of table (String; default='')
    :booktabs: If LaTeX booktabs package is used. If not, hline is used to seperate (Boolean; default=True)
    :file_name: file name under which to save the table in the current folder. If file_name = None
                no file will be created (Boolean, default=None)
                
    '''
    
    args_values = list(args_values)
    #rounding values
    if type(round_values) is int:
        for i in range(len(args_values)):
            try:
                args_values[i] = np.round(args_values[i], round_values)
            except:
                pass
    if type(round_values) is list or np.ndarray:
        for i in range(len(args_values)):
            try:
                args_values[i] = np.round(args_values[i], round_values[i])
            except:
                pass
            
    #seperate args into seperate arrays
    args_values = np.array(args_values)
    if seperate_values:
        args_values = args_values.T
    
    #write actual values
    rows = np.full(len(args_values[0]), '\t \t', dtype=str)
    for column in args_values[:-1]:
        #to string + replacement  
        column = np.char.replace(column.astype(str), '.', ',')
        rows = np.char.add(rows, column)
        rows = np.char.add(rows, ' & ')
    rows = np.char.add(rows, np.char.replace(args_values[-1].astype(str), '.', ','))
    rows = np.char.add(rows, ' \\\ \n')
    rows = ''.join(rows)
    
    #insert column names
    if column_names is not None:
        rows = '' + ' & '.join(column_names) + ' \\\ \n\t\midrule\n' + rows
        
    
    #latex code before and after data
    style = args_values.shape[0]*'c'
    text = f'\\begin{{table}}[]\n\t\centering\n\t\caption{{{table_caption}}}\n\t\\begin{{tabular}}{{{style}}}\n\t\\toprule\n\t'
    text = text + rows + f'\t\\bottomrule \n\t\\end{{tabular}}\n\t\\label{{{table_label}}}\n\\end{{table}}'
    if not booktabs:
        text = text.replace('toprule', 'hline').replace('midrule', 'hline').replace('bottomrule', 'hline')
        
    # save file if needed
    if file_name is not None:
        with open(file_name, 'w') as file:
            file.write(text)
            print(f'Table saved in: {file_name} \n')
    return text
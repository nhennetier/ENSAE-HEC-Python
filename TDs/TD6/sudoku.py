#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 9 19:24:24 2019

@author: alex
"""
import numpy as np

class Sudoku:
    """
    We will create a sudoku. We will modelise it with a matrice (numpy array).
    We will give a number to each square as follow
    
         0  |  1  |  2  
       -----------------
         3  |  4  |  5
       -----------------
         6  |  7  |  8
         
    A case not filled will contains -1
    """ 
    
    def __init__(self, values=None):
        if values is None:
            self.values = (np.ones((9, 9)) * -1).astype(int)
        else:
            self.values = np.array(values).astype(int)
            if not self.check():
                raise ValueError('Wrong value passed as input.')
                
    def check(self):
        """
        Check if the sudoku is correct, i.e. there is no doublons on rows, columns, or squares
        """
        for i in range(9):
            current_check = self.check_row(i) and self.check_column(i) and self.check_square(i)
            if not current_check:
                return False
        return True
    
    def check_row(self, i):
        """
        Check if there is no doublon on the i-th row
        """
        appeared = set()
        for n in self.values[i, :]:
            if n != -1 and n in appeared:
                return False
            appeared.add(n)
        return True
            
    def check_column(self, i):
        """
        Check if there is no doublon on the i-th column
        """
        appeared = set()
        for n in self.values[:, i]:
            if n != -1 and n in appeared:
                return False
            appeared.add(n)
        return True
            
    def check_square(self, i):
        """
        Check if there is no doublon on the i-th square
        """
        appeared = set()
        row = i // 3
        column = i % 3
        for n in self.values[3 * row: 3 * (row + 1), 3 * column: 3 * (column + 1)].flatten():
            if n != -1 and n in appeared:
                return False
            appeared.add(n)
        return True
            
    def mark(self, i, j, n):
        """
        Put a n in the i-th row, j-th column.
        If it breaks the logic of the sudoku, will do nothing and return False.
        Return True otherwise
        """
        if (n != -1) and (n < 1 or n > 9):
            raise ValueError('Wrong value for n')
        old = self.values[i, j]
        self.values[i, j] = n
        current_square = (i // 3) * 3 + j // 3
        if not(self.check_row(i) and self.check_column(j) and self.check_square(current_square)):
            self.values[i, j] = old
            return False
        return True
    
    def show(self):
        print(self.values)

    def complete(self):
        return self.check() and np.all(self.values != -1)

    def __getitem__(self, key):
        return self.values[key]

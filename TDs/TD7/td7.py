from tests import *
from solutions import Sudoku

"""
Exercice 1: Coder ce sudoku

5 3  |  7  |
     |1 9 5|
  9 8|     |  6
------------------
8    |  6  |    3
     |8   3|    1
7    |  2  |    6
------------------
  6  |     |2 8
     |  1 9|    5
     |  8  |  7 9

Le sudoku sera sous forme de classe, la grille sera stockée sous un numpy array, dans un attribut
grid et les cases vides seront des 0.
"""

test_exo_1(sudoku)

"""
Exercice 2: Coder une méthode pour checker si une ligne est valide, c'est à dire que chaque chiffre
est présent au plus une fois.

Cette méthode sera nommée is_valid_row, prendra en argument l'index de la ligne à vérifier et
retournera True ou False
"""

test_exo_2(Sudoku)

"""
Exercice 3: Coder une méthode pour checker si une colonne est valide, c'est à dire que chaque
chiffre est présent au plus une fois.

Cette méthode sera nommée is_valid_column, prendra en argument l'index de la colonne à vérifier et
retournera True ou False
"""

test_exo_3(Sudoku)

"""
Exercice 4: Coder une méthode pour checker si un carré est valide, c'est à dire que chaque
chiffre est présent au plus une fois.

Cette méthode sera nommée is_valid_square, prendra en argument l'index de la ligne et de la colonne
de la case à tester, testera le carré associé à cette case, et retournera True ou False
"""

test_exo_4(Sudoku)


"""
Exercice 5: Coder une méthode pour checker si la ligne, la colonne et le carré associé à une case
sont valides.

Cette méthode sera nommée is_valid, prendra en argument l'index de la ligne et de la colonne
de la case à tester, et retournera True ou False
"""

test_exo_5(Sudoku)


"""
Exercice 6: Coder une méthode pour résoudre un sudoku. Demander des indices au prof si vous êtes
bloqués.

Cette méthode sera nommé solve, ne prendra aucun argument et modifiera la grille sans en créer
d'autres.
"""

test_exo_6(Sudoku)

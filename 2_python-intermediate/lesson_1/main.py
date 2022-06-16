import phrase # import package (__init__.py)
from phrase import phrase_star_wars # import function from package
from phrase.spanish import phrase_isabel_allende # directly import the function from the file.
from phrase.english import phrase_john_lennon # directly import the function from the file.


print(phrase.phrase_mario_vargas_llosa())
print(phrase_star_wars())

print(phrase_isabel_allende())
print(phrase_john_lennon())

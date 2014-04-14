superheroBattle
===============

Super Hero Battle is a python game where the user can battle with the computer in an arcade-style action game. 

Utilizes sqlite3 to store and load characters to/from a database file. Current database (main.db) only has 2 characters.

Gameplay:

=>Characters have 4 attacks, each with a name and damage value. 
=>User gets to choose a character, computer chooses a random character not in use. 
=>Player can choose which attack to use each turn.
=>"Speed" stat value (out of 100) for the character will determine the percentage chance that an attack will miss.
===> Ex: 30-Speed means that there is a 30% chance an attack will miss.

Files:

shb_v2.py => Main game file. Contains the superHero() class which has functions for battling and keeping track of user health and attacks.

amrDB.py => File used to Add/Modify/Remove characters to/from the database.

printdb.py => Used to print the contents of the database. Doesn't necessarily have to be it's own file.

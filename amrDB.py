import sqlite3
import sys
import os

# INITIALIZATION FOR SQLITE - Creates db with this name if it doesn't exist
con = sqlite3.connect('main.db')
cur = con.cursor()

#Makes a tuple out of the inputted data
def makeTuple(a, b, c, d, e, f, g, h, i, j, k):
    t = ()  #temp tuple
    t = t + (a, b, c, d, e, f, g, h, i, j, k)
    return t

#Print Database
with con:
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    for row in rows:
        print row

# This will keep the user in the db edit loop, ADD/MOD/RM
while True:
    amrDB = raw_input("1: Add character ; 2: Rm character ; 3: Mod Stat ; 4: Print DB ; 5: Exit ")
    if int(amrDB) is 1:     # Add to Database
        data = ()           # Initialize tuple
        while True:
            nm = raw_input("Enter Char Name (STR): ")
            hlth = raw_input("Enter HLTH value (1-100): ")
            spd = raw_input("Enter SPD value (1-100): ")
            a1nm = raw_input("Enter ATK 1 Name: ")
            a1pw = raw_input("Enter ATK 1 Power: ")
            a2nm = raw_input("Enter ATK 2 Name: ")
            a2pw = raw_input("Enter ATK 2 Power: ")
            a3nm = raw_input("Enter ATK 3 Name: ")
            a3pw = raw_input("Enter ATK 3 Power: ")
            a4nm = raw_input("Enter ATK 4 Name: ")
            a4pw = raw_input("Enter ATK 4 Power: ")
            data = data + (makeTuple(nm, hlth, spd, a1nm, a1pw, a2nm, a2pw, a3nm, a3pw, a4nm, a4pw),)

            with con:
                cur.executemany('INSERT INTO characters values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
                con.commit()
                break

    elif int(amrDB) is 2:    # Remove charcter from database
        rmChar = raw_input("Remove which character? ")
        with con:
            cur.execute("DELETE FROM characters WHERE name = '%s'" % rmChar)
            con.commit()
            break

    elif int(amrDB) is 3:    # Modify 1 stat of a character
        while True:
            charMod = raw_input("Modify which character? >> ")
            
            # Use appropriate naming for the stat in the DB
            # ex: Attack 1 name = a1Name, Attack 1 value = a1Val, etc...
            statMod = raw_input("Which stat? >> ")
            val = raw_input("Value? >> ")
            
            # Needed for cur.execute since we can't pass variables into it
            stmt = "UPDATE characters SET '" + statMod + "' = '" + str(val) + "' WHERE name = '" + charMod + "'"
            
            with con:
                cur.execute(stmt)
                con.commit()
                break

    elif int(amrDB) is 4:   # print DB
        os.system("python printdb.py")
        
    elif int(amrDB) is 5:   # Exit
        break

    else:   # Exit if not adding/modding/removing/printing 
        break
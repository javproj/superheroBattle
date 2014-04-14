import random
import sqlite3
import sys
import os
import time

### CLASSES
class superHero():
    """
        The superHero class will be used to create superhero instances for battling.  The initialization function takes the superhero's name, health, attack strength, and speed. The Speed value will determine the chance that an attack on the hero will miss. 
    """
    
    def __init__(self, name, health, speed, a1n, a1v, a2n, a2v, a3n, a3v, a4n, a4v):
        self.name = name
        self.maxHealth = health     # maxHealth used to keep their maximum health value
        self.bHealth = health       # bHealth used for battling
        self.alive = True           # Boolean value for knowing if hero is alive
        self.speed = speed          # Determines chance hero will be hit, value 1-100
        # names and values of each of the 4 attacks 
        # a1n = attack 1 name, a1v = attack 1 value, etc...
        self.a1n = a1n
        self.a1v = a1v
        self.a2n = a2n
        self.a2v = a2v
        self.a3n = a3n
        self.a3v = a3v
        self.a4n = a4n
        self.a4v = a4v
    
    def isAttackedBy(self, attacker, move):
        """
            This class takes an instance of the superHero class and use's it's stats to determine how much damage to deal. We grab a random number between 1 and 100, if that number is greater than or equal to the hero's speed, then the attack can go through. 
        """
        move = int(move)    # Turn this into an int since it comes in as a NoneType
        
        if (random.randint(1, 100) > self.speed):    
            if self.bHealth >= attacker.getMoveVal(move):
                self.bHealth = self.bHealth - attacker.getMoveVal(move)
                print self.name, "takes", attacker.getMoveVal(move), "damage!"
                
                if self.bHealth == 0:
                    self.alive = False
                    print self.name + " has died!!!"
            else:
                self.bHealth = 0
                self.alive = False
                print self.name + " has died!!!"
        else:
            print self.name, "is too Fast"

    def statReset(self):
        """Resets the adjustable stats for self instance back to default """
        self.bHealth = self.maxHealth
        self.alive = True
    
    def displayMoves(self):
        """ Displays the Attack names and values for the user to choose from"""
        print "*****************"
        print "1- " + self.a1n + ": " + str(self.a1v) + " damage"
        print "2- " + self.a2n + ": " + str(self.a2v) + " damage"
        print "3- " + self.a3n + ": " + str(self.a3v) + " damage"
        print "4- " + self.a4n + ": " + str(self.a4v) + " damage"
        print "*****************"
        
    def getMoveVal(self, val):
        if val == 1:
            return self.a1v
        elif val == 2:
            return self.a2v
        elif val == 3:
            return self.a3v
        elif val == 4:
            return self.a4v
### END CLASSES

### FUNCTIONS
def makeTuple(a, b, c, d):
    """Makes a tuple out of the inputted data, for use in adding to database"""
    t = ()  #temp tuple
    t = t + (a, b, c, d)
    return t
### END FUNCTIONS

### GAME STATE
while True:
    begin = raw_input("Enter 1 to play, 2 to update the DB, 'quit' to exit: ")
    if begin == 'quit':
        break
    ##ACTUAL GAME STATE CASE ONE
    if int(begin) == 1:
        # These temporary arrays will store all of the data from my main.db
        t_name = []
        t_hlth = []
        t_spd = []
        t_a1n = []
        t_a1v = []
        t_a2n = []
        t_a2v = []
        t_a3n = []
        t_a3v = []
        t_a4n = []
        t_a4v = []
        
        #SQLITE3 Constants
        db = raw_input("Enter the name of the database to use: ")
        con = sqlite3.connect(db, timeout = 10)
        cur1 = con1.cursor()
        
        #Gets the names of all in my db
        cur1.execute("select name from Characters")
        for record in cur1.fetchall():
            t_name.append(str(record[0]))

        #Gets the hp of all in my db
        cur1.execute("select health from Characters")
        for record in cur1.fetchall():
            t_hlth.append(int(record[0]))

        #Gets the spd of all in my db
        cur1.execute("select speed from Characters")
        for record in cur1.fetchall():
            t_spd.append(int(record[0]))

        #Gets the atk names and vals of all in my db
        cur1.execute("select a1Name from Characters")
        for record in cur1.fetchall():
            t_a1n.append(str(record[0]))

        cur1.execute("select a1Val from Characters")
        for record in cur1.fetchall():
            t_a1v.append(int(record[0]))

        cur1.execute("select a2Name from Characters")
        for record in cur1.fetchall():
            t_a2n.append(str(record[0]))

        cur1.execute("select a2Val from Characters")
        for record in cur1.fetchall():
            t_a2v.append(int(record[0]))

        cur1.execute("select a3Name from Characters")
        for record in cur1.fetchall():
            t_a3n.append(str(record[0]))

        cur1.execute("select a3Val from Characters")
        for record in cur1.fetchall():
            t_a3v.append(int(record[0]))

        cur1.execute("select a4Name from Characters")
        for record in cur1.fetchall():
            t_a4n.append(str(record[0]))

        cur1.execute("select a4Val from Characters")
        for record in cur1.fetchall():
            t_a4v.append(int(record[0]))
        
        # Close the db, don't need it here any longer
        con1.close()
        
        #Display Character names and their index
        cntr = 0
        for x in t_name:
            print (cntr + 1), ": ", x
            cntr += 1

        # Asks the user for his character choice
        u1 = raw_input("Which character do you want? (Number): ")
        u1 = int(u1) - 1

        print "You Chose", t_name[u1], "!!!"
        
        # Randomly choose player for the computer
        # Set to random number, then put it in while loop to randomize until it's a diffeent character from the player if they were the same
        u2 = random.randint(0, (len(t_name)-1))
        while u2 == u1:
            u2 = random.randint(0, (len(t_name) - 1))
        print "The Computer has chosen", t_name[u2], "!!!"

        # Create instances of the characters
        player1 = superHero(t_name[u1], t_hlth[u1], t_spd[u1], t_a1n[u1], t_a1v[u1], t_a2n[u1], t_a2v[u1], t_a3n[u1], t_a3v[u1], t_a4n[u1], t_a4v[u1])
        
        player2 = superHero(t_name[u2], t_hlth[u2], t_spd[u2], t_a1n[u2], t_a1v[u2], t_a2n[u2], t_a2v[u2], t_a3n[u2], t_a3v[u2], t_a4n[u2], t_a4v[u2])
        
        #NOW WE CAN START PLAYING THE GAME
        print "Lets PLAY!!!", player1.name, "versus", player2.name, "\n"
        
        #Heads or Tails, who goes first
        first = random.randint(0, 1)
        last = 0    # 0 is player1, 1 is player 2
        if first == 0:
            print player1.name, "Attacks!"
            
            player1.displayMoves()
            
            p1Move = raw_input("Player 1, which move? ")
            
            time.sleep(0.5)
            player2.isAttackedBy(player1, p1Move)
        else:
            print player2.name, "Attacks!"
            
            player2.displayMoves()
            
            p2Move = raw_input("Player 2, which move? ")
            
            time.sleep(0.5)
            player1.isAttackedBy(player2, p2Move)
            last = 1
        time.sleep(0.5)
        
        #After initial attack, we throw game into a loop until one dies
        while (player1.alive == True) and (player2.alive == True):
            if last == 0:
                print player2.name, "Attacks!"
                
                player2.displayMoves()
                
                p2Move = raw_input("Player 2, which move? ")
                
                time.sleep(0.5)
                
                player1.isAttackedBy(player2, p2Move)
                
                last = 1
            else:
                print player1.name, "Attacks!"
                
                player1.displayMoves()
                
                p1Move = raw_input("Player 1, which move? ")
                
                time.sleep(0.5)
                
                player2.isAttackedBy(player1, p1Move)
                
                last = 0
            
            time.sleep(0.5)
        break  
    elif int(begin) == 2: #ADD/MOD/RM from DB
        os.system("python amrDB.py")
    else:
        break

### END GAME STATE
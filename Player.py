from Meeple import Meeple
class Player(object):

    #initialises the player object, only name can be set via this method
    #all other attributes will have default values across all players.
    def __init__(self, name):
        self._name = name
        self._colour = None
        self._avatar = None
        self._score = 0
        self._activeMeeples = []
        self._inactiveMeeples = []

    #Player sets the colour their meeples will be
    def setColour(self,colour):
        self._colour = colour
    #Returns the players colour
    def getColour(self):
        return self._colour

    #returns the players name
    def getName(self):
        return self._name

    #This method will calculate the score of a finished set of tiles and
    #increment the players score accordingly
    def increaseScore(self):
        pass

    #returns the players current score
    def getScore(self):
        return self._score

    #Prompts user to enter colour of their meeples and spawns 9 meeples
    #of that colour and places them in the inactive meeple list
    def createMeeples(self):
        for _ in range(0,8):
            m = Meeple(self)
            self._inactiveMeeples.append(m)

    #returns the amount of meeples available
    def meeplesAvailable(self):
        meeples=len(self._inactiveMeeples)
        return meeples

    #returns a meeple for placement if one is available
    def getMeeple(self):
        if len(self._inactiveMeeples) > 0:
            m = self._inactiveMeeples.pop()
            m.place()
            self._activeMeeples.append(m)
            return m

        else:
            print("No meeples available for placement; all on board.")

    def takeBack(self,meeple):
        m = self._activeMeeples.pop(meeple)
        self._inactiveMeeples.append(m)

if __name__=="__main__":
    p=Player("Brian")
    p.setColour("Red")
    p.createMeeples()
    meeple=p.getMeeple()
    print(meeple)

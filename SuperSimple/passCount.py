class Marks:

    def __init__( self  ):
        self.scoreList = []
        self.passLimit = None
        self.count = 0

    def addScore( self, score ):
        self.scoreList.append( score  )
    
    def getScores( self ):
        print( self.scoreList )

    def setPassLimit(self, limit):
        self.passLimit = limit
    
    def countPass( self  ):
        for score in self.scoreList:
            if score >=self.passLimit:
                self.count+=1

        print( "Total Pass Count ", self.count )
    
markObject = Marks()
markObject.setPassLimit(50)
markObject.addScore( 20 )
markObject.addScore( 90 )
markObject.addScore( 50 )

markObject.getScores()
markObject.countPass()
    
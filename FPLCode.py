print "FANTASY PREMIER LEAGUE"
myfile=open("gk.txt","r") #opening data files
myfile1=open("def.txt","r") #opening data files
myfile2=open("mid.txt","r") #opening data files
myfile3=open("strike.txt","r") #opening data files 
defender=myfile1.readlines()
goalkeeper=myfile.readlines()
midfielder=myfile2.readlines() 
strike=myfile3.readlines()
def occurences(ob,list1): #checks no. of occurences of ob in list1
    ctr=0
    for i in list1:
        if i==ob:
            ctr+=1
    return ctr 
def editor(list1,val): #editor function for
    ctr=0
    for i in list1:
        if val==i:
            ctr+=1
    for i in range(ctr):
        list1.remove(val)
def CSeditor(list1,val): #editor function for list cleansheets
    ctr=0
    for i in list1:
        if val==i:
            ctr+=1
    if ctr>=2:
        for i in range(ctr-1):
            list1.remove(val)
    else:
        pass
def checkifin(list1,ob): #checks if ob is in list1
    if ob in list1:
        return True 
    else:
        return False 
def Erroreditor(list1,ob): #if user enters a non-existent player
    try:
        if ob in list1:
            return True
        else:
            print (10/0) #raises an error as zerodivison is not possible
    except:
        print "ERROR!!PLAYER DOESN'T EXIST"
import random
class FPL: #class for all the players who are converted to objects
    def __init__(self,name,team,price,points=0):
        self.name=name
        self.price=price
        self.team=team
        self.points=points
    def __str__(self):
        return self.name+"   "+self.team+"   "+str(self.price)+"   "+str(self.points)
class PROJECT: #class for showing the players to user,picking a team and choosing a formation
    players=[]
    def __init__(self):
        self.goalkeepers=[]
        self.defenders=[]
        self.midfielders=[]
        self.strikers=[]
        self.players=[]
        self.teamvalue=0.0
        self.captain=""
    def showoptions(self):#function shows the options to user
        self.list=[]
        print "GOALKEEPERS"
        for i in goalkeeper:
            s=i.split()
            ob=FPL(s[0],s[1],float(s[2]))
            self.goalkeepers+=[ob]
            print ob
        print "DEFENDERS"
        for i in defender:
            s=i.split()
            ob=FPL(s[0],s[1],float(s[2]))
            self.defenders+=[ob]
            print ob
        print "MIDFIELDERS"
        for i in midfielder:
            s=i.split()
            ob=FPL(s[0],s[1],float(s[2]))
            self.midfielders+=[ob]
            print ob
        print "STRIKERS"
        for i in strike:
            s=i.split()
            ob=FPL(s[0],s[1],float(s[2]))
            self.strikers+=[ob]
            print ob
        PROJECT.players=self.goalkeepers+self.defenders+self.midfielders+self.strikers
    def pickteam(self): #function allows user to pick team
        self.names=[]
        self.teams=[]
        for i in PROJECT.players:
            self.names+=[i.name]
        self.list=[]
        self.playersnames=[]
        print "PICK A TEAM OF ELEVEN PLAYERS"
        print "MAX DEFENDERS = 5 \n MAX KEEPERS = 1 \n MAX MIDFIELDERS = 5 \n MAX STRIKERS= 3 "
        print "YOU CAN PICK MAXIMUM OF 3 PLAYERS FROM EACH TEAM"
        print "CAPTAIN-THIS PLAYER OF YOUR TEAM GETS DOUBLE POINTS FOR THE GAMEWEEK.YOU CAN CHOOSE ONLY ONE CAPTAIN.CAPTAIN SHOULD BE IN THE TEAM"
        print "YOUR BUDGET IS",75.0
        ctr=0 #counter for no. of defenders
        ctr1=0 #counter for no. of goalkeepers
        ctr2=0 #counter for no. of midfielders
        ctr3=0 #counter for no. of strikers
        while True:
            player=raw_input("enter choice")
            try:
                if Erroreditor(self.names,player):
                    for j in PROJECT.players:
                        if j.name==player: #in case user tries to pick same player twice
                            if j in self.list:
                                print "PLAYER ALREADY PICKED"
                                pass
                            else:
                                if j in self.defenders:
                                    ctr+=1
                                if j in self.goalkeepers:
                                    ctr1+=1
                                if j in self.midfielders:
                                    ctr2+=1
                                if j in self.strikers:
                                    ctr3+=1
                                if ctr>5: #if no. of defenders exceeds given value
                                    print "DEFENDERS EXCEEDED"
                                    ctr-=1
                                    print (10/0) #raises an error as zerodivison is not possible
                                if ctr1>1: #if no. of defenders exceeds given value
                                    print "GOALKEEPERS EXCEEDED"
                                    ctr1-=1
                                    print (10/0) #raises an error as zerodivison is not possible
                                if ctr2>5: #if no. of defenders exceeds given value
                                    print "MIDFIELDERS EXCEEDED"
                                    ctr2-=1
                                    print (10/0) #raises an error as zerodivison is not possible
                                if ctr3>3: #if no. of defenders exceeds given value
                                    print "STRIKERS EXCEEDED"
                                    ctr3-=1
                                    print (10/0) #raises an error as zerodivison is not possible
                                if occurences(j.team,self.teams)>2: #calling function occurences to make sure that user does not more than 3 players from same team
                                    print "TOO MANY PLAYERS SELECTED FROM",j.team
                                    print (10/0) #raises an error as zerodivison is not possible
                                self.teamvalue+=j.price
                                if self.teamvalue>75.0:
                                    print "BUDGET EXCEEDED"
                                    self.teamvalue-=j.price
                                    print (10/0) #raises an error as zerodivison is not possible
                                self.list+=[j]
                                self.playersnames+=[j.name]
                                print "AMOUNT LEFT IS", 75.0-self.teamvalue
                                self.teams+=[j.team]
                                if len(self.list)==11:
                                    captain=raw_input("enter captain")
                                    self.captain+=captain
                                    if captain not in self.playersnames: #if captain is not in team
                                        print "CAPTAIN SHOULD BE IN THE TEAM"
                                        print (10/0) #raises an error as zerodivison is not possible
                                    else:
                                        break
                if len(self.list)==11: #cannot have more than 11 players
                   break
            except: 
                print "ENTER AGAIN, INVALID INPUT"
        print "TEAM VALUE IS",self.teamvalue
    def showformation(self): #function shows user formation based on players he has picked
        defenders=0
        midfielders=0
        strikers=0
        dict1={}
        for i in self.list:
            if i in self.defenders:
                defenders+=1
            elif i in self.midfielders:
                midfielders+=1
            elif i in self.strikers:
                strikers+=1
        print "YOUR FORMATION IS",defenders,"-",midfielders,"-",strikers
class GAMEWEEK(PROJECT): #class for showing what all happened in gameweek.All the scorers and many more are shown here
    gs=[]
    cs=[]
    yc=[]
    assists=[]
    def __init__(self):
        PROJECT.__init__(self)
    @staticmethod
    def random(players,gs,cs,yc,assists): #FUNCTIONS ASSIGNS RANDOM PLAYERS AS GOALSCORERS,CLEANSHEETS,YELLOW CARDS,ASSISTS
        for i in range(100):
            x=random.choice(players)
            k=[gs,cs,yc,assists]
            m=random.choice(k)
            m+=[x]
    def edit(self): #edit function
        for i in GAMEWEEK.gs:
            if i in self.goalkeepers:
                editor(GAMEWEEK.gs,i)
        for i in GAMEWEEK.assists:
            if i in self.goalkeepers:
                editor(GAMEWEEK.assists,i)
        for i in GAMEWEEK.cs:
            if i in self.strikers:
                editor(GAMEWEEK.cs,i) #strikers can't keep cleansheet
        for i in GAMEWEEK.cs:
            CSeditor(GAMEWEEK.cs,i)
    @staticmethod
    def show(gs,cs,yc,assists):
        for i in GAMEWEEK.gs:
            print i.name,"SCORED"
        for i in GAMEWEEK.cs:
            print i.name,"kept a cleansheet"
        for i in GAMEWEEK.yc:
            print i.name,"got a yellow card"
        for i in GAMEWEEK.assists:
            print i.name,"assisted"
class POINTS(GAMEWEEK): #assign points to user's team based on performance in GAMEWEEK
    def __init__(self):
        PROJECT.__init__(self)
        GAMEWEEK.__init__(self)
        self.playerpoints=0
    def ASSIGNPOINTS(self):
        for i in self.list:
            if i.name==self.captain:
                self.playerpoints+=4
            else:
                self.playerpoints+=2
        for i in self.list:
            if i in GAMEWEEK.gs:
                if i in self.defenders:
                    if i.name==self.captain:
                        self.playerpoints+=12
                    else:
                        self.playerpoints+=6
                elif i in self.strikers or self.midfielders:
                    if i.name==self.captain:
                        self.playerpoints+=8
                    else:
                        self.playerpoints+=4
                else:
                    pass
            if i in GAMEWEEK.cs:
                if i in self.defenders or self.goalkeepers:
                    if i.name==self.captain:
                        self.playerpoints+=8
                    else:
                        self.playerpoints+=4
                elif i in self.midfielders:
                    if i.name==self.captain:
                        self.playerpoints+=2
                    else:
                        self.playerpoints+=1
                else:
                    pass
            if i in GAMEWEEK.yc:
                if i.name==self.captain:
                    self.playerpoints-=4
                else:
                    self.playerpoints-=2
            if i in GAMEWEEK.assists:
                if i.name==self.captain:
                    self.playerpoints+=8
                else:
                    self.playerpoints+=4
        return self.playerpoints
class stats(GAMEWEEK):#shows the user all the important stats of the gameweeek
    def __init__(self):
        PROJECT.__init__(self)
        GAMEWEEK.__init__(self)
        self.totalpoints=0.0
        self.dctg={}
        self.dctd={}
        self.dctm={}
        self.dcts={}
    def highestprice(self):
        dct={}
        for i in PROJECT.players:
            dct[i.price]=i.name
        lst=dct.keys()
        lst.sort(reverse=True)
        return dct[lst[0]]
    def costliestteam(self):
        dctcostly={}
        for i in PROJECT.players:
            dctcostly[i.price]=i
        lst=dct.keys()
        lst.sort(reverse=True)
        k=lst[0]+lst[1]+lst[2]+lst[3]+lst[4]
        sample+=[k]
while True:
    try:
        print "WELCOME TO FANTASY PREMIER LEAGUE"
        print "YOUR CHOICES ARE"
        print "1.PICK A TEAM"
        print "2.SHOW POINTS"
        print "3.SHOW STATS"
        print "4.QUIT"
        choice=input("enter a choice 1,2,3 or 4")
        if choice==1:
            n=input("enter no. of users for gameweek1")
            BIGLIST=[]
            for i in range(n):
                ob=POINTS()
                BIGLIST+=[ob]
                ob.showoptions()
                ob.pickteam()
                ob.showformation()
        elif choice==2:
            GAMEWEEK.random(PROJECT.players,GAMEWEEK.gs,GAMEWEEK.cs,GAMEWEEK.yc,GAMEWEEK.assists)
            for i in BIGLIST:
                i.edit()
            GAMEWEEK.show(GAMEWEEK.gs,GAMEWEEK.cs,GAMEWEEK.yc,GAMEWEEK.assists)
            ctr=0
            for i in BIGLIST:
                ctr+=1
                print "POINTS FOR PLAYER",ctr,"ARE",i.ASSIGNPOINTS()
        elif choice==3:
            ob=stats()
            print "PLAYER WITH HIGHEST PRICE IS",ob.highestprice()
        elif choice==4:
            break
        else:
            print (10/0) #raises an error as zerodivison is not possible
    except:
        print "INVALID CHOICE"



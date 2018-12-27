#Project 2 - CS 177
#Danilo de Amo Arantes Filho
#This is a graphical simulator for a Clay Target Game.
#Using the Angle and Power of launch as well as an artificial gravity, the game simulates
#two inanimate targets flying across the game window. By clicking on the targets with the
#mouse, the Player gets points based on said parameters. Scores are stored and shown by
#clicking on ''High Scores'' button. 

#Import necessary libraries 
from graphics import*
from time import*
from random import*
from math import*

#GameWindow function that creates the game simulation window. 
def GameWindow():
        #Game Window 
	GWin = GraphWin('Game Window', 600,600)
	GWin.setBackground('Light Sky Blue')
	
	Ground = Rectangle(Point(-1,450),Point(600,600))
	Ground.setFill('Light Green')
	Ground.draw(GWin)
	return GWin #Returns Game Window

#Function that animates clay targets across the Game Window and updates Score if a Clay is hit.

def Ani(a,p,g,game,Score_Display,R_Display):
        Round = R_Display.getText()
        R_Display.setText(Round + 1)
        y1 = randint(350,450)
        y2 = randint(350,450)
        i = 210

        #Clay 1 
        clay1 = Circle(Point(-8,y1),8)
        clay1.setFill('Dark grey')
        clay1.draw(game)

        #Clay 2 
        clay2 = Circle(Point(608,y2),8)
        clay2.setFill('Dark grey')
        clay2.draw(game)

        targets = [clay1,clay2]

        #Initial Dx,Dy of clays
        dx1 = p*(cos(a))
        dy1 = p*(sin(a))
        dx2 = p*(cos(a))
        dy2 = p*(sin(a))

        #Score increment function. 
        score = (g+p)/10
        

        while len(targets) > 0:
                i -= 1
                click = game.checkMouse()
                center1 = clay1.getCenter()
                center2 = clay2.getCenter()
                if center1.getX() <= 592 and center1.getY() <= 450:
                        clay1.move(dx1,-dy1)
                        sleep(0.05)
                        if click != None:
                                if checkCir(click,clay1) == True: #Clay 1 Hit detector
                                        clay1.undraw()
                                        targets.pop(0)
                                        score_counter = Score_Display.getText()
                                        Score_Display.setText(score_counter + round(score,2))                                        
                                                                       
                elif center1.getX() > 592 or center1.getY() > 450:#If clay reaches wall
                        clay1.undraw()
                        targets.pop(0)
                        
                if center2.getX() >= 8 and center2.getY() <= 442:
                        clay2.move(-dx2,-dy2)
                        sleep(0.01)
                        if click != None:
                                if checkCir(click,clay2) == True: #Clay 2 Hit detector
                                        if len(targets) > 1:
                                                clay2.undraw()
                                                targets.pop(1)
                                                score_counter = Score_Display.getText()
                                                Score_Display.setText(score_counter + round(score,2))
                                                
                                        elif len(targets) == 1:
                                                clay2.undraw()
                                                targets.pop(0)
                                                score_counter = Score_Display.getText()
                                                Score_Display.setText(score_counter + round(score,2))
                                              
                elif center2.getX() < 8 or center2.getY() > 442: #If clay reaches wall
                        clay2.undraw()
                        if len(targets) > 0:
                                targets.pop(0)
                                
                dy1 -= (g**2)/i
                dy2 -= (g**2)/i

        clay1.undraw()
        clay2.undraw()

        
#Function that defines buttons inside Control Panel. 
def Buttons(): 
        #Control Panel 
	CP = GraphWin('Clay Target Control Panel', 400,400)
	
	Text(Point(CP.getWidth()/2,20), 'Game Panel').draw(CP)
	Rec1 =  Rectangle(Point(10,30), Point(390,180)).draw(CP)
	
	Text(Point(CP.getWidth()/2,210), 'Target Panel').draw(CP)
	Rec2 =  Rectangle(Point(10,220), Point(390,370)).draw(CP)
	
	#Buttons - Rec1 	
	NG = Rectangle(Point(20,40), Point(135,90))
	NG.setFill('Green')
	NG.draw(CP)	
	Text(Point(77.5,65), 'New Game').draw(CP)
	
	HS = Rectangle(Point(145,40), Point(265,90))
	HS.setFill('Blue')
	HS.draw(CP)	
	Text(Point((CP.getWidth()/2)+5,65), 'High Scores').draw(CP)
	
	Q = Rectangle(Point(275,40), Point(380,90))
	Q.setFill('Red')
	Q.draw(CP)	
	Text(Point(327.5,65), 'Quit').draw(CP)
	
	#Player Name Entry
	PN = 'Player Name'
	Text(Point(77.5,120), 'Player').draw(CP)
	Player = Rectangle(Point(20,130), Point(135,170)).draw(CP)
	P_Name = Text(Point(77.5,150),'').draw(CP)

	#Round Display
	round_counter = 0
	Text(Point((CP.getWidth()/2),120), 'Round').draw(CP)
	R = Rectangle(Point(180,130), Point(220,170)).draw(CP)
	
	R_Display = Text(Point((CP.getWidth()/2),150), round_counter)
	R_Display.draw(CP)	
	
	#Score Display
	Text(Point(327.5,120), 'Score').draw(CP)
	S = Rectangle(Point(305,130), Point(350,170)).draw(CP)
	
	Score_Display = Text(Point(327.5,150), 0)
	Score_Display.draw(CP)
	
	#Angle
	Text(Point(80,230), 'Angle').draw(CP)
	A = Rectangle(Point(50,250), Point(110,290)).draw(CP)
	
	UpA = Circle(Point(125,255), 12).draw(CP)
	UpA.setFill('Light Grey')
	DownA = Circle(Point(125,285), 12).draw(CP)
	DownA.setFill('Light Grey')
	
	UpArrow = Line(Point(125,265), Point(125, 245))
	UpArrow.setArrow('last')
	UpArrow.draw(CP)
	
	DownArrow = Line(Point(125,275),Point(125,295))
	DownArrow.setArrow('last')
	DownArrow.draw(CP)
	
	Angle_Display = Text(Point(80,270), 45)
	Angle_Display.draw(CP)	
	
	#Power
	Text(Point(200,230), 'Power').draw(CP)
	P = Rectangle(Point(170,250), Point(230,290)).draw(CP)
	
	UpP = Circle(Point(245,255), 12).draw(CP)
	UpP.setFill('Light Grey')
	DownP = Circle(Point(245,285), 12).draw(CP)
	DownP.setFill('Light Grey')
	
	UpArrow = Line(Point(245,265), Point(245, 245))
	UpArrow.setArrow('last')
	UpArrow.draw(CP)
	
	DownArrow = Line(Point(245,275),Point(245,295))
	DownArrow.setArrow('last')
	DownArrow.draw(CP)
	
	Power_Display = Text(Point(200,270), 10)
	Power_Display.draw(CP)	
	
	#Gravity
	Text(Point(320,230), 'Gravity').draw(CP)
	G = Rectangle(Point(290,250), Point(350,290)).draw(CP)
	
	UpG = Circle(Point(365,255), 12).draw(CP)
	UpG.setFill('Light Grey')
	DownG = Circle(Point(365,285), 12).draw(CP)
	DownG.setFill('Light Grey')
	
	UpArrow = Line(Point(365,265), Point(365, 245))
	UpArrow.setArrow('last')
	UpArrow.draw(CP)
	
	DownArrow = Line(Point(365,275),Point(365,295))
	DownArrow.setArrow('last')
	DownArrow.draw(CP)
	
	Gravity_Display = Text(Point(320,270), 5)
	Gravity_Display.draw(CP)
	
	#Pull Button
	Pull = Rectangle(Point(120,310), Point(280,360))
	Pull.setFill('Light Coral')
	Pull.draw(CP)
	
	Pull_txt = Text(Point(200,335), 'Pull')
	Pull_txt.setSize(30)
	Pull_txt.draw(CP)

        #Returns all graphic objects 
	return CP,NG,HS,Q,P_Name,R_Display,Score_Display,UpA,DownA,Angle_Display,UpP,DownP,Power_Display,UpG,DownG,Gravity_Display,Pull,A,P,G,Player,round_counter
        
def checkSqr(Mouse,button): #Checks for clicks inside Squared shapes.
        P1 = button.getP1()
        P2 = button.getP2()

        if P1.getX() < Mouse.getX() < P2.getX() and P1.getY() < Mouse.getY() < P2.getY():
                return True
        else:
                return False
def checkCir(Mouse,button): #Checks for clicks inside circles. 
        Center = button.getCenter()
        x1, y1 = Mouse.getX(), Mouse.getY()
        x2, y2 = Center.getX(), Center.getY()
        distance = ((x1-x2)**2+(y1-y2)**2)**.5
        if distance < 12:
                return True

#Function that creates HighScores window, opens high scores file or creates one if none exists. 
def HighScores(Player,Score): 
        HighScores = GraphWin('High Scores', 200,400)
        HS_list = []
        try:

                HS = open('top_scores.txt','r')
                HS_list = HS.readlines()        
                HS.close()
                print(HS_list)

                HS = open('top_scores.txt','w+')
                for line in HS_list:
                        HS.write(line)
                if Player != '':
                        HS.write(str(Player)+'\t'+str(Score)+'\n')
                HS.close()
        except IOError:
                HS = open('top_scores.txt','w+')
                HS.write('Top 10 Scores\n=============\n'+ str(Player)+'\t'+str(Score)+'\n') 
                HS.close()

        HS = open('top_scores.txt','r')
        HS_list = HS.readlines()
        HS.close()

                            
        return HighScores, HS_list

        
	
def ControlPanel(Functions,click,GameWin): #Adds functionality to Buttons()
        CP,NG,HS,Q,P_Name,R_Display,Score_Display,UpA,DownA,Angle_Display,UpP,DownP,Power_Display,UpG,DownG,Gravity_Display,Pull,A,P,G,Player,round_counter = Functions
        while True:
                click = CP.getMouse()
                
                if checkSqr(click,NG) == True: #New game Button

                        if P_Name.getText() != '':
                                NG.setFill('Green')
                                R_Display.setText(0)
                                Score_Display.setText(0)
                                Angle_Display.setText(45)
                                Power_Display.setText(10)
                                Gravity_Display.setText(5)
                                
                elif R_Display.getText() == 5:
                        R_Display.setText(0)
                        Score_Display.setText(0)

                        

                elif checkSqr(click,HS) == True: #High Score Button
                        y = 0
                        pl = P_Name.getText()
                        sc = Score_Display.getText()
                        HSWin, HS_list = HighScores(pl,sc)
                        HS_Win = Rectangle(Point(-1,-1), Point(200,400)).draw(HSWin)
                        for line in HS_list:
                                y+=30
                                Text(Point(HSWin.getWidth()/2,y),str(line)).draw(HSWin)

                        HS_click = HSWin.getMouse()
                        if checkSqr(HS_click,HS_Win) == True:
                                HSWin.close()

                elif checkSqr(click,Q) == True: #Quit Button
                        GameWin.close()
                        CP.close()

                elif checkCir(click,UpA) == True:#UpAngle Button
                        
                        if 30 <= Angle_Display.getText() < 60:
                                increase = (Angle_Display.getText() + 1)
                                Angle_Display.setText(increase)

                elif checkCir(click,DownA) == True: #Down Angle Button
                        if 30 < Angle_Display.getText() < 60:
                                increase = (Angle_Display.getText() - 1)
                                Angle_Display.setText(increase)

                elif checkCir(click,UpP) == True: #Up Power Button
                        if 5 <= Power_Display.getText() < 50:
                                increase = (Power_Display.getText() + 1)
                                Power_Display.setText(increase)

                elif checkCir(click,DownP) == True: #Down Power Button
                        if 5 < Power_Display.getText() < 50:
                                increase = (Power_Display.getText() - 1)
                                Power_Display.setText(increase)

                elif checkCir(click,UpG) == True: #Up Gravity Button
                        if 3 <= Gravity_Display.getText() < 25:
                                increase = (Gravity_Display.getText() + 1)
                                Gravity_Display.setText(increase)
                                
                elif checkCir(click,DownG) == True: #Down Gravity Button
                        if 3 < Gravity_Display.getText() < 25:
                                increase = (Gravity_Display.getText() -1)
                                Gravity_Display.setText(increase)

                elif checkSqr(click,Pull) == True: #Pull Button
                        a = Angle_Display.getText()
                        p = Power_Display.getText()
                        g = Gravity_Display.getText()
                        if P_Name.getText() != '':
                                Pull.setFill('Yellow')
                                UpA.setFill('Red')
                                DownA.setFill('Red')
                                UpP.setFill('Red')
                                DownP.setFill('Red')
                                UpG.setFill('Red')
                                DownG.setFill('Red')
                                NG.setFill('Grey')
                                sleep(2)
                                Ani(a,p,g,GameWin,Score_Display,R_Display)
                                NG.setFill('Green')

                elif checkSqr(click,Player) == True:#Player Name Entry 
                        P_Name.setText('')
                        Name = Entry(Point(77.5,150),15)
                        Name.setFill('White')
                        Name.draw(CP)
                        CP.getMouse()
                        Player_Name = Name.getText()
                        Name.undraw()
                        P_Name.setText(Player_Name)

                elif checkSqr(click,A) == True: #Angle Entry 
                        Angle_Display.setText('')
                        Angle = Entry(Point(80,270),2)
                        Angle.setFill('White')
                        Angle.draw(CP)
                        CP.getMouse()
                        Ang = Angle.getText()
                        try:
                                Ang = int(Ang)
                        except ValueError:
                                Angle.undraw()
                                Angle_Display.setText(45)
                                
                        if type(Ang) != int or Ang < 30 or Ang > 60:
                                Angle.undraw()
                                Angle_Display.setText(45)
                        else:
                                Angle.undraw()
                                Angle_Display.setText(Ang)

                elif checkSqr(click,P) == True: #Power Entry 
                        Power_Display.setText('')
                        Power = Entry(Point(200,270),2)
                        Power.setFill('White')
                        Power.draw(CP)
                        CP.getMouse()
                        Pow = Power.getText()
                        try:
                                Pow = int(Pow)
                        except ValueError:
                                Power.undraw()
                                Power_Display.setText(10)
                        if type(Pow) != int or Pow < 5 or Pow > 50:
                                Power.undraw()
                                Power_Display.setText(10)
                        else:
                                Power.undraw()
                                Power_Display.setText(Pow)

                elif checkSqr(click,G) == True: #Gravity Entry 
                        Gravity_Display.setText('')
                        Gravity = Entry(Point(320,270),2)
                        Gravity.setFill('White')
                        Gravity.draw(CP)
                        CP.getMouse()
                        Grav = Gravity.getText()
                        try:
                                Grav = int(Grav)
                        except ValueError:
                                Gravity.undraw()
                                Gravity_Display.setText(5)
                        if type(Grav) != int or Grav < 3 or Grav > 25:
                                Gravity.undraw()
                                Gravity_Display.setText(5)
                        else:
                                Gravity.undraw()
                                Gravity_Display.setText(Grav)

                        
                        
#Main Function that calls other functions. 
def main():
        GWin = GameWindow()
        Functions = list(Buttons())
        CP = Functions[0]
        click = CP.getMouse()
        while True:
                ControlPanel(Functions,click,GWin)

#Initialize the Game(Main function)
main()


        
        

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:04:05 2016

@author: admin
"""

import turtle


def main():

    image = "pacman.gif"
    imageleft = "pacmanleft.gif" 
    imageup = "pacmanup.gif" 
    imagedown = "pacmandown.gif" 
    image = "pacman.gif"
    ##setup screen
    window = turtle.Screen()
    
    window.setup(800,800)
    window.bgcolor("black")
    window.addshape((image))
    window.addshape((imageleft))
    window.addshape((imageup))
    window.addshape((imagedown))
    window.addshape("pacman-grid1.gif")
    centerpen0 = turtle.Turtle()
    centerpen0.goto(0,-22)
    centerpen0.shape("pacman-grid1.gif")
    centerpen0.penup()
    pacman = turtle.Turtle()
    pacman.color("yellow")
    pacman.shape(image)
    pacman.penup()
    pacman.speed(0)
    pacman.setposition(20,190)
    
   ### if x in range (123,100,1) :
      ###  pacman.speed(1)
        
    ####else: pacman.speed(0)    
     



    
    
        ######### pac-man moving speed#####
    speed = 0  
#################define movement  functions
    def turnleft():
        pacman.shape(imageleft)
        pacman.setheading(0)
        pacman.left(180)
        pacman.fd(1)
        speed +1
        return speed
    def turnright(): 
        pacman.shape(image)
        pacman.setheading(0)
        pacman.right(0)
        pacman.fd(1)
        speed = +1
        return speed
    def turnup():
        speed =+ 1
        pacman.shape(imageup)
        pacman.setheading(0)
        pacman.left(90)
        pacman.fd(1)
        return speed
    def turndown():
        speed = + 1
        pacman.shape(imagedown)
        pacman.setheading(0)
        pacman.left(270)
        pacman.fd(1)
        return speed 

    turtle.listen()
    turtle.onkey(turnleft,"Left")
    turtle.onkey(turnright,"Right")
    turtle.onkey(turnup,"Up")
    turtle.onkey(turndown,"Down")


    while True:
        pacman.fd(speed)
        print (pacman.pos())
        if ((-193 <= pacman.xcor() <= 190) and (185 <= pacman.ycor()<= 205)):####ROW1 RIGHT
            speed = 1
    
        elif ((-193 <= pacman.xcor() <= 190) and (135 <= pacman.ycor()<= 164)):####ROW3 COMPLETE
            speed = 1
        elif ((-193 <= pacman.xcor() <= -170) and (163 <= pacman.ycor()<= 186)):#####ROW 2 RIGHT
            speed = 1
        elif ((-120 <= pacman.xcor() <= -140) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT1
            speed = 1
        elif ((-22 <= pacman.xcor() <= 5) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
            speed = 1
        elif ((15 <= pacman.xcor() <= 35) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
            speed = 1
        elif ((117 <= pacman.xcor() <= 130) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
            speed = 1
        elif ((180 <= pacman.xcor() <= 193) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
            speed = 1
        elif ((-193 <= pacman.xcor() <= -170) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((-120 <= pacman.xcor() <= -140) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((117 <= pacman.xcor() <= 130) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((180 <= pacman.xcor() <= 193) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((-85 <= pacman.xcor() <= -95) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((64 <= pacman.xcor() <= 85) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
            speed = 1
        elif ((-193 <= pacman.xcor() <= -121) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
            speed = 1
        elif ((-85 <= pacman.xcor() <= -22) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
            speed = 1
        elif ((15 <= pacman.xcor() <= 85) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
            speed = 1

        elif ((-73 <= pacman.xcor() <= -1) and (96 <= pacman.ycor()<= 103)):
            speed = 1
        elif ((20 <= pacman.xcor() <= 80) and (90 <= pacman.ycor()<= 103)):
            speed = 1
        elif ((120 <= pacman.xcor() <= 188) and (90 <= pacman.ycor()<= 115)):
            speed = 1

            #9th row
        elif ((-193 <= pacman.xcor() <= -69) and (-3 <= pacman.ycor()<= 10)):
            speed = 1
        elif ((69 <= pacman.xcor() <= 193) and (-3 <= pacman.ycor()<= 10)):
            speed = 1

            #11 th row
        elif ((-123 <= pacman.xcor() <= -117) and (-55 <= pacman.ycor()<= -38)):
            speed = 1
        elif ((-74 <= pacman.xcor() <= 73) and (-55 <= pacman.ycor()<= -38)):
            speed = 1
        elif ((120 <= pacman.xcor() <= 116) and (-55 <= pacman.ycor()<= -38)):
            speed = 1

            #12th row
            
        elif ((-120 <= pacman.xcor() <= -140) and ( -54<= pacman.ycor()<=-79 )):
            speed = 1
        elif ((117 <= pacman.xcor() <= 130) and ( -54<= pacman.ycor()<=-79 )):
            speed = 1
        elif ((180 <= pacman.xcor() <= 193) and (-54 <= pacman.ycor()<=-79)):
            speed = 1
        elif ((-85 <= pacman.xcor() <= -95) and (-54 <= pacman.ycor()<=-79 )):
            speed = 1


            #13th row
        elif ((-194 <= pacman.xcor() <= -21) and (-108 <= pacman.ycor()<= -80)):
            speed = 1
        elif ((21 <= pacman.xcor() <= 194) and (-108 <= pacman.ycor()<= -80)):
            speed = 1            
            
            
        ###row 14th
        elif ((-193 <= pacman.xcor() <= -170) and (-131 <= pacman.ycor()<= -106)):
            speed = 1
        elif ((-120 <= pacman.xcor() <= -140) and (-131 <= pacman.ycor()<= -106)):
            speed = 1
        elif ((-22 <= pacman.xcor() <= 5) and (-131 <= pacman.ycor()<= -106)):
            speed = 1
        elif ((15 <= pacman.xcor() <= 35) and (-131<= pacman.ycor()<= -106)):
            speed = 1
        elif ((117 <= pacman.xcor() <= 130) and (-131 <= pacman.ycor()<= -106)):
            speed = 1
        elif ((180 <= pacman.xcor() <= 193) and (-131 <= pacman.ycor()<= -106)):           
            speed = 1

              #15th row
        elif ((-194 <= pacman.xcor() <= -166) and (-152 <= pacman.ycor()<= -130)):
            speed = 1
        elif ((-122 <= pacman.xcor() <= 122) and (-152 <= pacman.ycor()<= -130)):
            speed = 1
        elif ((164 <= pacman.xcor() <= 194) and (-152 <= pacman.ycor()<= -130)):
            speed = 1
                 #16th row
        elif ((-194 <= pacman.xcor() <= -166) and (-170 <= pacman.ycor()<= -159)):
            speed = 1
        elif ((-122 <= pacman.xcor() <= -118) and (-170 <= pacman.ycor()<= -159)):
            speed = 1
        elif ((-75 <= pacman.xcor() <= -70) and (-170<= pacman.ycor()<= -159)):
            speed = 1
        elif ((69 <= pacman.xcor() <= 74) and (-170 <= pacman.ycor()<= -159)):
            speed = 1
        elif ((116 <= pacman.xcor() <= 121) and (-170 <= pacman.ycor()<= -159)):
            speed = 1
        elif ((165 <= pacman.xcor() <= 194) and (-190 <= pacman.ycor()<= -130)):
            speed = 1

        ######row 18th    
        elif ((-200 <= pacman.xcor() <= -170) and (-220<= pacman.ycor()<= -210)):
            speed = 1
        elif ((-120 <= pacman.xcor() <= -140) and (-220 <= pacman.ycor()<= -210)):
            speed = 1
        elif ((117 <= pacman.xcor() <= 130) and (-220 <= pacman.ycor()<= -210)):
            speed = 1     
        elif ((180 <= pacman.xcor() <= 193) and (-220 <= pacman.ycor()<= -210)):
            speed = 1
        elif ((-85 <= pacman.xcor() <= -95) and (-220 <= pacman.ycor()<= -210)):
            speed = 1
        elif ((64 <= pacman.xcor() <= 85) and (-220 <= pacman.ycor()<= -210)):
            speed = 1

    
        #19th ROW
        elif ((-195 <= pacman.xcor() <= 199) and (-242 <= pacman.ycor()<= -225)):
            speed = 1
    
            
            #17th Row
        elif ((-193 <= pacman.xcor() <= -121) and (-200 <= pacman.ycor()<= -188)):#####ROW 17 LEFT
            speed = 1
        elif ((-85 <= pacman.xcor() <= -22) and (-235 <= pacman.ycor()<= -188)):#####ROW 17 LEFT
            speed = 1
        elif ((15 <= pacman.xcor() <= 85) and (-235 <= pacman.ycor()<= -188)):#####ROW 17 right
            speed = 1
        elif ((130 <= pacman.xcor() <= 195) and (-200 <= pacman.ycor()<= -188)):#####ROW 17 right
            speed = 1 


            #7 th row
        elif ((-123 <= pacman.xcor() <= -117) and (45 <= pacman.ycor()<= 60)):
            speed = 1
        elif ((-74 <= pacman.xcor() <= 73) and (45 <= pacman.ycor()<= 60)):
            speed = 1
        elif ((120 <= pacman.xcor() <= 116) and (45 <= pacman.ycor()<= 60)):
            speed = 1








            
            ###col 1st
        elif ((-195<= pacman.xcor() <= 190) and (198 <= pacman.ycor()<= 93)):
            speed = 1            
        elif ((-195 <= pacman.xcor() <= 190) and (3 <= pacman.ycor()<= -2)):
            speed = 1
        elif ((-195 <= pacman.xcor() <= 190) and (-92 <= pacman.ycor()<= -242)):
            speed = 1

            #2nd col
        elif ((-169 <= pacman.xcor() <= -164) and (198 <= pacman.ycor()<= 185)):
            speed = 1
        elif ((-169 <= pacman.xcor() <= -164) and (150 <= pacman.ycor()<= 139)):
            speed = 1
        elif ((-169 <= pacman.xcor() <= -164) and (95 <= pacman.ycor()<= 102)):
            speed = 1
        elif ((-169 <= pacman.xcor() <= -164) and (-5 <= pacman.ycor()<= 5)):
            speed = 1
        elif ((-169 <= pacman.xcor() <= -164) and (-96 <= pacman.ycor()<= -91)):
            speed = 1
        elif ((-169 <= pacman.xcor() <= -164) and (-220 <= pacman.ycor()<= -92)):
            speed = 1

            #3rd col
        elif ((-139 <= pacman.xcor() <= -144) and (197 <= pacman.ycor()<= 180)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -144) and (136 <= pacman.ycor()<= 152)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -144) and (95 <= pacman.ycor()<=103)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -144) and (5 <= pacman.ycor()<= -4)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -144) and (-99 <= pacman.ycor()<= -89)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -144) and (-193 <= pacman.ycor()<= 188)):
            speed = 1
        elif ((-139 <= pacman.xcor() <= -21) and (-241 <= pacman.ycor()<= -235)):
            speed = 1
            
            

        elif ((-193 <= pacman.xcor() <= -160) and ( 205<= pacman.ycor()<= -270)):#colom1
            speed = 1
        elif ((-133 <= pacman.xcor() <= -118) ):#colom4
            speed = 1
        elif ((118 <= pacman.xcor() <= 133) ):#colom14
            speed = 1 
    ##col17
        elif ((173 <= pacman.xcor() <= 215) and ( 189<= pacman.ycor()<= 102)):
            speed = 1
        elif ((173 <= pacman.xcor() <= 215) and ( 12<= pacman.ycor()<= -15)):
            speed = 1
        elif ((173 <= pacman.xcor() <= 215) and ( -70<= pacman.ycor()<= -249)):
            speed = 1
            
    ###col16
        elif ((165 <= pacman.xcor() <=179 ) and ( -128<= pacman.ycor()<= -199)):
            speed = 1
    ###col15
        elif ((140 <= pacman.xcor() <=152 ) and ( 180<= pacman.ycor()<= 210)):
            speed = 1  
        elif ((140 <= pacman.xcor() <=152 ) and ( 158<= pacman.ycor()<= 128)):
            speed = 1  
        elif ((140 <= pacman.xcor() <=152 ) and ( 80<= pacman.ycor()<= 122)):
            speed = 1 
        elif ((140 <= pacman.xcor() <=152 ) and ( -10<= pacman.ycor()<= 15)):
            speed = 1 
        elif ((140 <= pacman.xcor() <=152 ) and ( -116<= pacman.ycor()<= -69)):
            speed = 1 
        elif ((140 <= pacman.xcor() <=152 ) and ( -252<= pacman.ycor()<= -183)):
            speed = 1 
        
    ###col12
        elif ((60 <= pacman.xcor() <=80 ) and ( 184<= pacman.ycor()<= 206)):
            speed = 1            
        elif ((60 <= pacman.xcor() <=80 ) and ( 80<= pacman.ycor()<= -156)):
            speed = 1
        elif ((60 <= pacman.xcor() <=80 ) and ( -90<= pacman.ycor()<= 50)):
            speed = 1
        elif ((60 <= pacman.xcor() <=80 ) and ( -198<= pacman.ycor()<= -150)):
            speed = 1            

    ###col6
        elif ((-80 <= pacman.xcor() <=-65 ) and ( 184<= pacman.ycor()<= 206)):
            speed = 1            
        elif ((-80 <= pacman.xcor() <=-65 ) and ( 80<= pacman.ycor()<= -156)):
            speed = 1
        elif ((-80 <= pacman.xcor() <=-65 ) and ( -90<= pacman.ycor()<= 50)):
            speed = 1
        elif ((-80 <= pacman.xcor() <=-65 ) and ( -198<= pacman.ycor()<= -150)):
            speed = 1
        elif ((-80 <= pacman.xcor() <=-65 ) and ( 96<= pacman.ycor()<= 165)):
            speed = 1        




            #colom10
        elif ((12 <= pacman.xcor() <= 32) and (150 <= pacman.ycor()<= 200)):
            speed = 1
        elif ((12 <= pacman.xcor() <= 32) and (40 <= pacman.ycor()<= 115)):
            speed = 1
        elif ((12 <= pacman.xcor() <= 32) and (-220 <= pacman.ycor()<= -210)):
            speed = 1
            #colom8
        elif ((-33 <= pacman.xcor() <= -13) and (150 <= pacman.ycor()<= 200)):
            speed = 1
        elif ((-33 <= pacman.xcor() <= -13) and (40 <= pacman.ycor()<= 115)):
            speed = 1 
        elif ((-33 <= pacman.xcor() <= -13) and (-153 <= pacman.ycor()<=-75)):
            speed = 1
        elif ((-33 <= pacman.xcor() <= -13) and (-220 <= pacman.ycor()<= -210)):
            speed = 1
            #colom1
        elif ((-205 <= pacman.xcor() <= -170)and (-250 <= pacman.ycor()<=-85)):
            speed = 1
            #colom17
        elif ((189 <= pacman.xcor() <= 210)and (-250 <= pacman.ycor()<=-85)):
            speed = 1
        else:
            speed = 0
            pacman.back(2)




















        
main()       
delay=input("press enter")        
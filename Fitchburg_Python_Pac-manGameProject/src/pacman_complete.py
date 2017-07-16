
# -*- coding: utf-8 -*-
"""
File:       pacman-i3.py    
Date:       11/29/2016
Instructor: Nguyen Thai
Course:     CSC 7014 - The Practice of Computer Programming
Author:     Prashanti sudha Kosgi
id :        01374492
Description: PCP project increment3.

"""


def main():
    import turtle
    import time
    import math
    import winsound
    food = "coin1.gif"    
    image = "pacman.gif"
    imageleft = "pacmanleft.gif" 
    imageup = "pacmanup.gif" 
    imagedown = "pacmandown.gif" 
    ##setup screen
    window = turtle.Screen()
    window.clear()
    
    window.setup(800,800)
    window.bgcolor("black")
    window.addshape((image))
    window.addshape((imageleft))
    window.addshape((imageup))
    window.addshape((imagedown))
    window.addshape(food)
    window.addshape("pacman-grid1.gif")
    window.addshape("pink-ghost.gif")
    window.addshape("red-ghost.gif")
    window.addshape("orange-ghost.gif")
    window.addshape("blue-ghost.gif")
    window.addshape("youwin.gif")
    window.addshape("youlost.gif")
    window.addshape("booster.gif")
    window.addshape("ghost.gif")
    window.addshape("over.gif")
    window.addshape("cherry.gif")
    window.addshape("straberry.gif")
    window.addshape("apple.gif")
    window.addshape("time.gif")
#########################front page###################### 
    mazepen = turtle.Turtle()
    mazepen.pencolor("yellow")
    mazepen.penup()
    mazepen.goto(-180,120) 
    mazepen.write("ENHACED PACMAN",font=("Impact",35, "bold"))
    mazepen.penup()
    mazepen.goto(-150,-30)
    mazepen.pencolor("red")
    mazepen.write("              Welcome !! \n Hit Space to Start Playing !!",font=("Arial",15, "bold"))
    mazepen.goto(-120,-150)
    mazepen.pencolor("red")
    mazepen.write("         Prof-Nguyen Thai \n               CSC-7014   \n               Fall 2016 \n Fitchburg State University",font=("Arial",12, "bold"))
    mazepen.goto(-80,-220)
    mazepen.pencolor("red")
    mazepen.write("By- Reshma \n       Prashanthi \n       Pooja",font=("Arial",12, "bold"))
    winsound.PlaySound('pacman_start.wav', winsound.SND_ASYNC)
###########################^^^^^^^END OF FRONT PAGE^^^^^^^^^^#################    

    def nextpage():
        window.clear()
        window.bgcolor("black")
        centerpen0 = turtle.Turtle()
        centerpen0.goto(0,-22)
        centerpen0.shape("pacman-grid1.gif")
        centerpen0.stamp()
        centerpen0.penup()
        centerpen = turtle.Turtle()
        centerpen.pu()
        centerpen.ht()
########################creating coins###################

        window.tracer(0,60)

        coinlist=[]
        def make_turtle(name):
            name = turtle.Turtle()
            name.shape(food)
            name.penup()
            return name

        co5= make_turtle("co5")
        co5.setpos(46,-95)
        coinlist.append(co5)
        co6= make_turtle("co6")
        co6.setpos(71,-95)
        coinlist.append(co6)
        co7= make_turtle("co7")
        co7.setpos(96,-95)
        coinlist.append(co7)
        co8= make_turtle("co8")
        co8.setpos(23,-95)
        coinlist.append(co8)
        co9= make_turtle("co9")
        co9.setpos(23,-123)
        coinlist.append(co9)
        co10= make_turtle("co10")
        co10.setpos(121,-95)
        coinlist.append(co10)
        co11= make_turtle("co11")
        co11.setpos(146,-95)
        coinlist.append(co11)
        co12= make_turtle("co12")
        co12.setpos(171,-95)
        coinlist.append(co12)
        co13= make_turtle("co13")
        co13.setpos(191,-118)
        coinlist.append(co13)
        co14= make_turtle("co14")
        co14.setpos(191,-141)
        coinlist.append(co14)
        co15= make_turtle("co15")
        co15.setpos(191,-95)
        coinlist.append(co15)
        co16= make_turtle("co16")
        co16.setpos(191,-187)
        coinlist.append(co16)
        co17= make_turtle("co17")
        co17.setpos(191,-210)
        coinlist.append(co17)
        co18= make_turtle("co18")
        co18.setpos(191,-233)
        coinlist.append(co18)
        co19= make_turtle("co19")
        co19.setpos(166,-235)
        coinlist.append(co19)
        co20= make_turtle("co20")
        co20.setpos(141,-235)
        coinlist.append(co20)
        
        co21= make_turtle("co21")
        co21.setpos(116,-235)
        coinlist.append(co21)
        co22= make_turtle("co22")
        co22.setpos(91,-235)
        coinlist.append(co22)
        co23= make_turtle("co23")
        co23.setpos(66,-235)
        coinlist.append(co23)
        co24= make_turtle("co24")
        co24.setpos(41,-235)
        coinlist.append(co24)
        co25= make_turtle("co25")
        co25.setpos(16,-235)
        coinlist.append(co25)
        co26= make_turtle("co26")
        co26.setpos(-9,-235)
        coinlist.append(co26)
        co27= make_turtle("co27")
        co27.setpos(-34,-235)
        coinlist.append(co27)
        co28= make_turtle("co28")
        co28.setpos(-59,-235)
        coinlist.append(co28)
        co29= make_turtle("c029")
        co29.setpos(-90,-235)
        coinlist.append(co29)
        co30= make_turtle("co30")
        co30.setpos(-109,-235)
        coinlist.append(co30)
        
        co31= make_turtle("co31")
        co31.setpos(-144,-235)
        coinlist.append(co31)
        co32= make_turtle("co32")
        co32.setpos(-169,-235)
        coinlist.append(co32)
        co33= make_turtle("co33")
        co33.setpos(-193,-235)
        coinlist.append(co33)
        co34= make_turtle("co34")
        co34.setpos(-193,-211)
        coinlist.append(co34)
        co35= make_turtle("co35")
        co35.setpos(-193,-191)
        coinlist.append(co35)
        co36= make_turtle("co36")
        co36.setpos(-193,-141)
        coinlist.append(co36)
        co37= make_turtle("co37")
        co37.setpos(-193,-116)
        coinlist.append(co37)
        co38= make_turtle("co38")
        co38.setpos(-193,-91)
        coinlist.append(co38)
        co39= make_turtle("co39")
        co39.setpos(-193,5)
        coinlist.append(co39)
        co40= make_turtle("co40")
        co40.setpos(-193,95)
        coinlist.append(co40)
        co41= make_turtle("co41")
        co41.setpos(-193,116)
        coinlist.append(co41)
        co42= make_turtle("co42")
        co42.setpos(-193,141)
        coinlist.append(co42)
        co43= make_turtle("co43")
        co43.setpos(-193,166)
        coinlist.append(co43)
        #####1ST ROW####
        
        co44= make_turtle("co44")
        co44.setpos(-193,191)
        coinlist.append(co44)
        co45= make_turtle("co45")
        co45.setpos(-168,193)
        coinlist.append(co45)
        co46= make_turtle("co46")
        co46.setpos(-144,193)
        coinlist.append(co46)
        co47= make_turtle("co47")
        co47.setpos(-123,193)
        coinlist.append(co47)
        co48= make_turtle("co48")
        co48.setpos(-100,193)
        coinlist.append(co48)
        co49= make_turtle("co49")
        co49.setpos(-75,193)
        coinlist.append(co49)
        co50= make_turtle("co50")
        co50.setpos(-50,193)
        coinlist.append(co50)
        
        co51= make_turtle("co51")
        co51.setpos(-28,193)
        coinlist.append(co51)
        co52= make_turtle("co52")
        co52.setpos(35,193)
        coinlist.append(co52)
        co53= make_turtle("co53")
        co53.setpos(63,193)
        coinlist.append(co53)
        co54= make_turtle("co54")
        co54.setpos(88,193)
        coinlist.append(co54)
        co55= make_turtle("co55")
        co55.setpos(113,193)
        coinlist.append(co55)
        co56= make_turtle("co56")
        co56.setpos(138,193)
        coinlist.append(co56)
        co57= make_turtle("co57")
        co57.setpos(163,193)
        coinlist.append(co57)
        co58= make_turtle("co58")
        co58.setpos(188,191)
        coinlist.append(co58)
        co59= make_turtle("co59")
        
        #####3rd row####
        co59.setpos(-168,148)
        coinlist.append(co59)
        co60= make_turtle("co60")
        co60.setpos(-144,148)
        coinlist.append(co60)
        co61= make_turtle("co61")
        co61.setpos(-123,148)
        coinlist.append(co61)
        co62= make_turtle("co62")
        co62.setpos(-100,148)
        coinlist.append(co62)
        co63= make_turtle("co63")
        co63.setpos(-75,148)
        coinlist.append(co63)
        co64= make_turtle("co64")
        co64.setpos(-50,148)
        coinlist.append(co64)
        co65= make_turtle("co65")
        co65.setpos(-28,148)
        coinlist.append(co65)
        co66= make_turtle("co66")
        co66.setpos(35,148)
        coinlist.append(co66)
        co67= make_turtle("co67")
        co67.setpos(57,148)
        coinlist.append(co67)
        co68= make_turtle("co68")
        co68.setpos(79,148)
        coinlist.append(co68)
        co69= make_turtle("co69")
        co69.setpos(101,148)
        coinlist.append(co69)
        co70= make_turtle("co70")
        co70.setpos(123,148)
        coinlist.append(co70)
        co71= make_turtle("co71")
        co71.setpos(145,148)
        coinlist.append(co71)
        co72= make_turtle("co672")
        co72.setpos(167,148)
        coinlist.append(co72)
        co73= make_turtle("co73")
        co73.setpos(189,148)
        coinlist.append(co73)
        co74= make_turtle("co74")
        co74.setpos(-3,148)
        coinlist.append(co74)
        co75= make_turtle("co75")
        co75.setpos(19,148)
        coinlist.append(co75)
        
        #####2ND ROW##########
        co76= make_turtle("co76")
        co76.setpos(-24,171)
        coinlist.append(co76)
        co77= make_turtle("co77")
        co77.setpos(190,171)
        coinlist.append(co77)
        co78= make_turtle("co78")
        co78.setpos(-121,171)
        coinlist.append(co78)
        co79= make_turtle("co79")
        co79.setpos(24,171)
        coinlist.append(co79)
        co80= make_turtle("co80")
        co80.setpos(121,171)
        coinlist.append(co80)
        
        ######5TH ROW#######
        co81= make_turtle("co81")
        co81.setpos(-168,100)
        coinlist.append(co81)
        co82= make_turtle("co82")
        co82.setpos(-144,100)
        coinlist.append(co82)
        co83= make_turtle("co83")
        co83.setpos(-123,100)
        coinlist.append(co83)
        co84= make_turtle("co84")
        co84.setpos(-75,100)
        coinlist.append(co84)
        co85= make_turtle("co85")
        co85.setpos(-50,100)
        coinlist.append(co85)
        co86= make_turtle("co86")
        co86.setpos(-28,100)
        coinlist.append(co86)

        co88= make_turtle("co88")
        co88.setpos(19,102)
        coinlist.append(co88)
        co89= make_turtle("co89")
        co89.setpos(48,102)
        coinlist.append(co89)
        co90= make_turtle("co90")
        co90.setpos(75,102)
        coinlist.append(co90)
        co91= make_turtle("co91")
        co91.setpos(123,102)
        coinlist.append(co91)
        co92= make_turtle("co92")
        co92.setpos(145,102)
        coinlist.append(co92)
        co93= make_turtle("co93")
        co93.setpos(169,102)
        coinlist.append(co93)
        co94= make_turtle("co94")
        co94.setpos(189,102)
        coinlist.append(co94)
        ###4th row#####
        co95= make_turtle("co95")
        co95.setpos(-123,125)
        coinlist.append(co95)
        co96= make_turtle("co96")
        co96.setpos(-75,125)
        coinlist.append(co96)
        co97= make_turtle("co97")
        co97.setpos(75,125)
        coinlist.append(co97)
        co98= make_turtle("co98")
        co98.setpos(123,125)
        coinlist.append(co98)
        co99= make_turtle("co99")
        co99.setpos(189,125)
        coinlist.append(co99)
        
        #### 6th row#####
        co100= make_turtle("co100")
        co100.setpos(-123,75)
        coinlist.append(co100)
        co101= make_turtle("co101")
        co101.setpos(-26,75)
        coinlist.append(co101)
        co102= make_turtle("co102")
        co102.setpos(21,75)
        coinlist.append(co102)
        co103= make_turtle("co103")
        co103.setpos(121,75)
        coinlist.append(co103)
        
        ######7th row######
        co104= make_turtle("co104")
        co104.setpos(-123,50)
        coinlist.append(co104)
        co105= make_turtle("co105")
        co105.setpos(-75,50)
        coinlist.append(co105)
        co106= make_turtle("co106")
        co106.setpos(-50,50)
        coinlist.append(co106)
        co107= make_turtle("co107")
        co107.setpos(-28,50)
        coinlist.append(co107)
        co108= make_turtle("co108")
        co108.setpos(-3,50)
        coinlist.append(co108)
        co109= make_turtle("co109")
        co109.setpos(19,50)
        coinlist.append(co109)
        co110= make_turtle("co110")
        co110.setpos(48,50)
        coinlist.append(co110)
        co111= make_turtle("co111")
        co111.setpos(75,50)
        coinlist.append(co111)
        co112= make_turtle("co112")
        co112.setpos(123,50 )
        coinlist.append(co112)
        
        ####8th row######
        
        co113= make_turtle("co113")
        co113.setpos(-123,29 )
        coinlist.append(co113)
        co114= make_turtle("co114")
        co114.setpos(-75,29 )
        coinlist.append(co114)
        co115= make_turtle("co115")
        co115.setpos(75,29 )
        coinlist.append(co115)
        co116= make_turtle("co116")
        co116.setpos(123,29 )
        coinlist.append(co116)
        
        #####9th row#######
        co117= make_turtle("co117")
        co117.setpos(-168,5 )
        coinlist.append(co117)
        co118= make_turtle("co118")
        co118.setpos(-144,5 )
        coinlist.append(co118)
        co119= make_turtle("co119")
        co119.setpos(-123,5 )
        coinlist.append(co119)
        co120= make_turtle("co120")
        co120.setpos(-100,5 )
        coinlist.append(co120)
        co121= make_turtle("co121")
        co121.setpos(-75,5 )
        coinlist.append(co121)
        co123= make_turtle("co123")
        co123.setpos(75,5 )
        coinlist.append(co123)
        co124= make_turtle("co124")
        co124.setpos(98,5 )
        coinlist.append(co124)
        co125= make_turtle("co125")
        co125.setpos(123,5 )
        coinlist.append(co125)
        co126= make_turtle("co126")
        co126.setpos(145,5 )
        coinlist.append(co126)
        co127= make_turtle("co127")
        co127.setpos(169,5 )
        coinlist.append(co127)
        co128= make_turtle("co128")
        co128.setpos(189,5 )
        coinlist.append(co128)
        
        ######10TH ROW#########
        co129= make_turtle("co129")
        co129.setpos(-123,-19 )
        coinlist.append(co129)
        co130= make_turtle("co130")
        co130.setpos(-75,-19 )
        coinlist.append(co130)
        co131= make_turtle("co131")
        co131.setpos(75,-19 )
        coinlist.append(co131)
        co132= make_turtle("co132")
        co132.setpos(123,-19)
        coinlist.append(co132)
        
        ########11th row########
        co133= make_turtle("co133")
        co133.setpos(-123,-46 )
        coinlist.append(co133)
        co134= make_turtle("co134")
        co134.setpos(-75,-46 )
        coinlist.append(co134)
        co135= make_turtle("co135")
        co135.setpos(-50,-46)
        coinlist.append(co135)
        co136= make_turtle("co136")
        co136.setpos(-28,-46)
        coinlist.append(co136)
        co137= make_turtle("co137")
        co137.setpos(-3,-46)
        coinlist.append(co137)
        co138= make_turtle("co138")
        co138.setpos(19,-46 )
        coinlist.append(co138)
        co139= make_turtle("co139")
        co139.setpos(48,-46 )
        coinlist.append(co139)
        co140= make_turtle("co140")
        co140.setpos(75,-46 )
        coinlist.append(co140)
        co141= make_turtle("co141")
        co141.setpos(123,-46 )
        coinlist.append(co141)
        
        #######12th row########
        co142= make_turtle("co142")
        co142.setpos(-123,-69 )
        coinlist.append(co142)
        co143= make_turtle("co143")
        co143.setpos(-75,-69 )
        coinlist.append(co143)
        co144= make_turtle("co144")
        co144.setpos(75,-69 )
        coinlist.append(co144)
        co145= make_turtle("co145")
        co145.setpos(123,-69 )
        coinlist.append(co145)
        
        ######13th row#########
        co146= make_turtle("co146")
        co146.setpos(-168,-92 )
        coinlist.append(co146)
        co147= make_turtle("co147")
        co147.setpos(-144,-92 )
        coinlist.append(co147)
        co148= make_turtle("co148")
        co148.setpos(-123,-92 )
        coinlist.append(co148)
        co149= make_turtle("co149")
        co149.setpos(-100,-92 )
        coinlist.append(co149)
        co150= make_turtle("co150")
        co150.setpos(-75,-92)
        coinlist.append(co150)
        co151= make_turtle("co151")
        co151.setpos(-50,-92 )
        coinlist.append(co151)
        co152= make_turtle("co152")
        co152.setpos(-28,-92 )
        coinlist.append(co152)
        
        #####14th row########
        co153= make_turtle("co153")
        co153.setpos(-123,-118 )
        coinlist.append(co153)
        co154= make_turtle("co154")
        co154.setpos(-28,-118 )
        coinlist.append(co154)
        co155= make_turtle("co155")
        co155.setpos(123,-118)
        coinlist.append(co155)
        
        ######15th row########
        co156= make_turtle("co156")
        co156.setpos(-168,-142 )
        coinlist.append(co156)
        co157= make_turtle("co157")
        co157.setpos(-123,-142 )
        coinlist.append(co157)
        co158= make_turtle("co158")
        co158.setpos(-100,-142 )
        coinlist.append(co158)
        co159= make_turtle("co159")
        co159.setpos(-75,-142 )
        coinlist.append(co159)
        co160= make_turtle("co160")
        co160.setpos(-50,-142 )
        coinlist.append(co160)
        co161= make_turtle("co161")
        co161.setpos(-28,-142)
        coinlist.append(co161)
        co162= make_turtle("co162")
        co162.setpos(-3,-142 )
        coinlist.append(co162)
        co163= make_turtle("co163")
        co163.setpos(19,-142 )
        coinlist.append(co163)
        co164= make_turtle("co164")
        co164.setpos(48,-142 )
        coinlist.append(co164)
        co165= make_turtle("co165")
        co165.setpos(75,-142 )
        coinlist.append(co165)
        co166= make_turtle("co166")
        co166.setpos(79,-142)
        coinlist.append(co166)
        co167= make_turtle("co167")
        co167.setpos(101,-142)
        coinlist.append(co167)
        co168= make_turtle("co168")
        co168.setpos(123,-142)
        coinlist.append(co168)
        co1 = make_turtle("co1 ")
        co1.setpos(168,-142)
        coinlist.append(co1)
        
        
        #######16TH ROW#######
        co169= make_turtle("co169")
        co169.setpos(-168,-168)
        coinlist.append(co169)
        co170= make_turtle("co170")
        co170.setpos(-123,-168 )
        coinlist.append(co170)
        co171= make_turtle("co171")
        co171.setpos(-68,-168 )
        coinlist.append(co171)
        co172= make_turtle("co172")
        co172.setpos(70,-168 )
        coinlist.append(co172)
        co173= make_turtle("co173")
        co173.setpos(121,-168 )
        coinlist.append(co173)
        co174= make_turtle("co174")
        co174.setpos(167,-168 )
        coinlist.append(co174)
        
        ######## 17TH ROW###########
        co175= make_turtle("co175")
        co175.setpos(-168,-190 )
        coinlist.append(co175)
        co176= make_turtle("co176")
        co176.setpos(-144,-190 )
        coinlist.append(co176)
        co178= make_turtle("co178")
        co178.setpos(-123,-190)
        coinlist.append(co178)
        co179= make_turtle("co179")
        co179.setpos(-75,-190)
        coinlist.append(co179)
        co180= make_turtle("co180")
        co180.setpos(-50,-190)
        coinlist.append(co180)
        co181= make_turtle("co181")
        co181.setpos(-28,-190)
        coinlist.append(co181)
        co182= make_turtle("co182")
        co182.setpos(23,-190)
        coinlist.append(co182)
        co183= make_turtle("co183")
        co183.setpos(48,-190)
        coinlist.append(co183)
        co184= make_turtle("co184")
        co184.setpos(70,-190)
        coinlist.append(co184)
        co187= make_turtle("co187")
        co187.setpos(123,-190)
        coinlist.append(co187)
        co188= make_turtle("co188")
        co188.setpos(145,-190)
        coinlist.append(co188)
        co189= make_turtle("co189")
        co189.setpos(169,-190)
        coinlist.append(co189)

        #####18TH ROW######
        co190= make_turtle("co190")
        co190.setpos(-28,-215 )
        coinlist.append(co190)
        co191= make_turtle("co191")
        co191.setpos(19,-215)
        coinlist.append(co191)
        window.update()
################################creating pacman and enemies##################
        pacman = turtle.Turtle()
        pacman.color("yellow")
        pacman.shape(image)
        pacman.penup()
        pacman.speed(0)
        pacman.setposition(-50,-50)
        pinkghost = turtle.Turtle()
        pinkghost.penup()
        pinkghost.speed(1)
        pinkghost.setposition(-1,23)
        pinkghost.shape("pink-ghost.gif")
        redghost = turtle.Turtle()
        redghost.penup()
        redghost.speed(1)
        redghost.setposition(-25,1)
        redghost.shape("red-ghost.gif")
        orangeghost = turtle.Turtle()
        orangeghost.penup()
        orangeghost.speed(1)
        orangeghost.setposition(-5,1)
        orangeghost.shape("orange-ghost.gif")
        blueghost = turtle.Turtle()
        blueghost.penup()
        blueghost.speed(1)
        blueghost.setposition(20,1)
        blueghost.shape("blue-ghost.gif")
        
        def blueghostMov():
            if blueghost.xcor() == -4 and blueghost.ycor() ==1:
                blueghost.setheading(270)
            if blueghost.xcor() == -4 and blueghost.ycor() ==45:
                blueghost.setheading(0)
            if blueghost.xcor() == -70 and blueghost.ycor() ==45:
                blueghost.setheading(90)
            if blueghost.xcor() == -70 and blueghost.ycor() ==1:
                blueghost.setheading(0)
            if blueghost.ycor() == 1 and blueghost.xcor() ==-120:
                blueghost.setheading(90)
            if blueghost.ycor() == -100 and blueghost.xcor() ==-120:
                blueghost.setheading(0)
            if blueghost.ycor() == -100 and blueghost.xcor() ==-190:
                blueghost.setheading(90)
            if blueghost.ycor() == -240 and blueghost.xcor() ==-190:
                blueghost.setheading(180)
            if blueghost.ycor() == -240 and blueghost.xcor() ==190:
                blueghost.setheading(270)#up
            if blueghost.ycor() == -100 and blueghost.xcor() ==190:
                blueghost.setheading(0)#<-
            if blueghost.ycor() == -100 and blueghost.xcor() ==120:
                blueghost.setheading(270)#up
            if blueghost.ycor() == 100 and blueghost.xcor() ==120:
                blueghost.setheading(180)#->
            if blueghost.ycor() == 100 and blueghost.xcor() ==190:
                blueghost.setheading(270)#up
            if blueghost.ycor() == 190 and blueghost.xcor() ==190:
                blueghost.setheading(0)# left
            if blueghost.ycor() == 190 and blueghost.xcor() ==-190:
                blueghost.setheading(90)#down
            if blueghost.ycor() == 100 and blueghost.xcor() ==-190:
                blueghost.setheading(180)#left
            if blueghost.ycor() == 100 and blueghost.xcor() ==-120:
                blueghost.setheading(90)#down
            blueghost.backward(1)
        
        #############pen for writting the time left################
        tpen =turtle.Turtle()
        tpen.pu()
        tpen.color("red")
        tpen.setpos(-50,-310)
        tpen.ht()
###########################different powers#################
        
        boost=turtle.Turtle()
        boost.color("black")
        boost.penup()
        boost.setpos(0,0)
        boost.pu()
        cherry=turtle.Turtle()
        cherry.color("black")
        cherry.penup()
        cherry.setpos(0,0)
        cherry.pu()
        straberry=turtle.Turtle()
        straberry.color("black")
        straberry.penup()
        straberry.setpos(0,0)
        straberry.pu()
        apple=turtle.Turtle()
        apple.color("black")
        apple.penup()
        apple.setpos(0,0)
        apple.pu()
        ghost=turtle.Turtle()
        ghost.color("black")
        ghost.penup()
        ghost.setpos(0,0)
        ghost.pu()
        clock=turtle.Turtle()
        clock.pu()
        clock.shape("time.gif")
        clock.setpos(-190,-168)
        clock.pd()
        
        def isCollision(t1,t2):
            d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
            if d < 15:
                return True
            else:
                return False        
        
        
        score = 0#############initial score
        speed = 0###########pacman movement speed###############
        count =[]############number of coints
        life = 3############number of lifes
        now= time.time()#################time limit####
        playtime = now + 90
        a = 1
                
        
#################define movement  functions
        def speedUp():
            pacman.fd(10)
            return
        def turnleft():
            pacman.shape(imageleft)
            pacman.setheading(0)
            pacman.left(180)
            pacman.fd(1)
            return           
        def turnright():
            pacman.shape(image)
            pacman.setheading(0)
            pacman.right(0)
            pacman.fd(1)
            return
        def turnup():
            pacman.shape(imageup)
            pacman.setheading(0)
            pacman.left(90)
            pacman.fd(1)
            return 
        def turndown():
            pacman.shape(imagedown)
            pacman.setheading(0)
            pacman.left(270)
            pacman.fd(1)
            return
##################function to clear the screen on timeup##############
            
        def timeup():
            winsound.PlaySound('pacman_timeup.wav', winsound.SND_ASYNC)
            window.clear()
            window.bgcolor("black")
            window. bgpic("over.gif")
            window.delay(10)
            ########################begin last page################################
            mazepen = turtle.Turtle()
            mazepen.pencolor("yellow")
            mazepen.penup()
            mazepen.goto(-180,120)
            
            mazepen.write("Thanks For Playing",font=("Impact",35, "bold"))
            mazepen.penup()
            mazepen.goto(-110,-30)
            mazepen.pencolor("red")
            mazepen.write(" Your Total score is " + str(score),font=("Arial",15, "bold"))
            mazepen.goto(-125,-150)
            mazepen.pencolor("red")
            mazepen.pendown()
            mazepen.write("Press R to restart Playing!!!" , font=("Ariel",15,"bold"))
            mazepen.penup() 
            mazepen.goto(-120,-220)
            mazepen.pencolor("red")
            mazepen.pendown()
            mazepen.write("Press Q to Quit the game!!! ",font=("Arial",15, "bold"))
            mazepen.penup()
            ########################function to quit game on pressing Q####################3
            def quitgame():
                turtle.bye()
            ##########################3function to restart game on pressing R###################
            def restartgame():
                main()
            ######################keyboard and function assignment   
            window.listen()
            window.onkey(quitgame,"q")
            window.onkey(restartgame,"r")
            while True:
                for i in range (50):
                    mazepen.penup()
                    mazepen.hideturtle()
                    mazepen.fd(100)
                    mazepen.left(90)
        #####################################function to last page#############

        def clearscreen():
            window.clear()
            window.bgcolor("black")
            ########################begin last page################################
            mazepen = turtle.Turtle()
            mazepen.pencolor("yellow")
            mazepen.penup()
            mazepen.goto(-180,120)
            
            mazepen.write("Thanks For Playing",font=("Impact",35, "bold"))
            mazepen.penup()
            mazepen.goto(-110,-30)
            mazepen.pencolor("red")
            mazepen.write(" Your Total score is " + str(score),font=("Arial",15, "bold"))
            mazepen.goto(-125,-150)
            mazepen.pencolor("red")
            mazepen.pendown()
            mazepen.write("Press R to restart Playing!!!" , font=("Ariel",15,"bold"))
            mazepen.penup() 
            mazepen.goto(-120,-220)
            mazepen.pencolor("red")
            mazepen.pendown()
            mazepen.write("Press Q to Quit the game!!! ",font=("Arial",15, "bold"))
            mazepen.penup()
            ########################function to quit game on pressing Q####################3
            def quitgame():
                turtle.bye()
            ##########################3function to restart game on pressing R###################
            def restartgame():
                main()
            ######################keyboard and function assignment   
            window.listen()
            window.onkey(quitgame,"q")
            window.onkey(restartgame,"r")
            while True:
                for i in range (50):
                    mazepen.penup()
                    mazepen.hideturtle()
                    mazepen.fd(100)
                    mazepen.left(90)
                    
        #######################end of last page####################################

                    
        #####################set keyboard for pacman movement###################
        turtle.listen()
        turtle.onkey(turnleft,"Left")
        turtle.onkey(turnright,"Right")
        turtle.onkey(turnup,"Up")
        turtle.onkey(turndown,"Down")
        turtle.onkey(clearscreen,"space")
        turtle.onkey(speedUp,"s")

        while True:
            #############checking timer and printing on screen#############
            timeleft = int(playtime-int(time.time()))
            timestring = "Time left: %s" %timeleft
            tpen.write(timestring, False, align="left",font=("chiller",20,"normal"))
            tpen.undo()
            if time.time() < playtime:
                pacman.fd(speed)
                print (pacman.pos())
                if pacman.pos()==(-50,-50):
                    speed = 0
                elif ((-193 <= pacman.xcor() <= 190) and (185 <= pacman.ycor()<= 205)):####ROW1 RIGHT
                    speed = a
                elif ((-193 <= pacman.xcor() <= 190) and (135 <= pacman.ycor()<= 164)):####ROW3 COMPLETE
                    speed = a
                elif ((-193 <= pacman.xcor() <= -170) and (163 <= pacman.ycor()<= 186)):#####ROW 2 RIGHT
                    speed = a
                elif ((-120 <= pacman.xcor() <= -140) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT1
                    speed = a
                elif ((-22 <= pacman.xcor() <= 5) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
                    speed = a
                elif ((15 <= pacman.xcor() <= 35) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
                    speed = a
                elif ((117 <= pacman.xcor() <= 130) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
                    speed = a
                elif ((180 <= pacman.xcor() <= 193) and (163 <= pacman.ycor()<= 186)):#####ROW 2 LEFT
                    speed = a
                elif ((-193 <= pacman.xcor() <= -170) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((-120 <= pacman.xcor() <= -140) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((117 <= pacman.xcor() <= 130) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((180 <= pacman.xcor() <= 193) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((-85 <= pacman.xcor() <= -95) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((64 <= pacman.xcor() <= 85) and (113 <= pacman.ycor()<= 136)):#####ROW 4 LEFT
                    speed = a
                elif ((-193 <= pacman.xcor() <= -121) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
                    speed = a
                elif ((-85 <= pacman.xcor() <= -22) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
                    speed = a
                elif ((15 <= pacman.xcor() <= 85) and (91 <= pacman.ycor()<= 114)):#####ROW 5 LEFT
                    speed = a
        
                elif ((-73 <= pacman.xcor() <= -1) and (96 <= pacman.ycor()<= 103)):
                    speed = a
                elif ((20 <= pacman.xcor() <= 80) and (90 <= pacman.ycor()<= 103)):
                    speed = a
                elif ((120 <= pacman.xcor() <= 188) and (90 <= pacman.ycor()<= 115)):
                    speed = a
        
                    #9th row
                elif ((-193 <= pacman.xcor() <= -69) and (-3 <= pacman.ycor()<= 10)):
                    speed = a
                elif ((69 <= pacman.xcor() <= 193) and (-3 <= pacman.ycor()<= 10)):
                    speed = a
        
                    #11 th row
                elif ((-123 <= pacman.xcor() <= -117) and (-55 <= pacman.ycor()<= -38)):
                    speed = a
                elif ((-74 <= pacman.xcor() <= 73) and (-55 <= pacman.ycor()<= -38)):
                    speed = a
                elif ((120 <= pacman.xcor() <= 116) and (-55 <= pacman.ycor()<= -38)):
                    speed = a
        
                    #12th row
                    
                elif ((-120 <= pacman.xcor() <= -140) and ( -54<= pacman.ycor()<=-79 )):
                    speed = a
                elif ((117 <= pacman.xcor() <= 130) and ( -54<= pacman.ycor()<=-79 )):
                    speed = a
                elif ((180 <= pacman.xcor() <= 193) and (-54 <= pacman.ycor()<=-79)):
                    speed = a
                elif ((-85 <= pacman.xcor() <= -95) and (-54 <= pacman.ycor()<=-79 )):
                    speed = a
        
        
                    #13th row
                elif ((-194 <= pacman.xcor() <= -21) and (-108 <= pacman.ycor()<= -80)):
                    speed = a
                elif ((21 <= pacman.xcor() <= 194) and (-108 <= pacman.ycor()<= -80)):
                    speed = a            
                    
                    
                ###row 14th
                elif ((-193 <= pacman.xcor() <= -170) and (-131 <= pacman.ycor()<= -106)):
                    speed = a
                elif ((-120 <= pacman.xcor() <= -140) and (-131 <= pacman.ycor()<= -106)):
                    speed = a
                elif ((-22 <= pacman.xcor() <= 5) and (-131 <= pacman.ycor()<= -106)):
                    speed = a
                elif ((15 <= pacman.xcor() <= 35) and (-131<= pacman.ycor()<= -106)):
                    speed = a
                elif ((117 <= pacman.xcor() <= 130) and (-131 <= pacman.ycor()<= -106)):
                    speed = a
                elif ((180 <= pacman.xcor() <= 193) and (-131 <= pacman.ycor()<= -106)):           
                    speed = a
        
                      #15th row
                elif ((-194 <= pacman.xcor() <= -166) and (-152 <= pacman.ycor()<= -130)):
                    speed = a
                elif ((-122 <= pacman.xcor() <= 122) and (-152 <= pacman.ycor()<= -130)):
                    speed = a
                elif ((164 <= pacman.xcor() <= 194) and (-152 <= pacman.ycor()<= -130)):
                    speed = a
                         #16th row
                elif ((-194 <= pacman.xcor() <= -166) and (-170 <= pacman.ycor()<= -159)):
                    speed = a
                elif ((-122 <= pacman.xcor() <= -118) and (-170 <= pacman.ycor()<= -159)):
                    speed = a
                elif ((-75 <= pacman.xcor() <= -70) and (-170<= pacman.ycor()<= -159)):
                    speed = a
                elif ((69 <= pacman.xcor() <= 74) and (-170 <= pacman.ycor()<= -159)):
                    speed = a
                elif ((116 <= pacman.xcor() <= 121) and (-170 <= pacman.ycor()<= -159)):
                    speed = a
                elif ((165 <= pacman.xcor() <= 194) and (-190 <= pacman.ycor()<= -130)):
                    speed = a
        
                ######row 18th    
                elif ((-200 <= pacman.xcor() <= -170) and (-220<= pacman.ycor()<= -210)):
                    speed = a
                elif ((-120 <= pacman.xcor() <= -140) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
                elif ((117 <= pacman.xcor() <= 130) and (-220 <= pacman.ycor()<= -210)):
                    speed = a     
                elif ((180 <= pacman.xcor() <= 193) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
                elif ((-85 <= pacman.xcor() <= -95) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
                elif ((64 <= pacman.xcor() <= 85) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
        
            
                #19th ROW
                elif ((-195 <= pacman.xcor() <= 199) and (-242 <= pacman.ycor()<= -225)):
                    speed = a
            
                    
                    #17th Row
                elif ((-193 <= pacman.xcor() <= -121) and (-200 <= pacman.ycor()<= -188)):#####ROW 17 LEFT
                    speed = a
                elif ((-85 <= pacman.xcor() <= -22) and (-235 <= pacman.ycor()<= -188)):#####ROW 17 LEFT
                    speed = a
                elif ((15 <= pacman.xcor() <= 85) and (-235 <= pacman.ycor()<= -188)):#####ROW 17 right
                    speed = a
                elif ((130 <= pacman.xcor() <= 195) and (-200 <= pacman.ycor()<= -188)):#####ROW 17 right
                    speed = a 
        
        
                    #7 th row
                elif ((-123 <= pacman.xcor() <= -117) and (45 <= pacman.ycor()<= 60)):
                    speed = a
                elif ((-74 <= pacman.xcor() <= 73) and (45 <= pacman.ycor()<= 60)):
                    speed = a
                elif ((120 <= pacman.xcor() <= 116) and (45 <= pacman.ycor()<= 60)):
                    speed = a
        
                    ###col 1st
                elif ((-195<= pacman.xcor() <= 190) and (198 <= pacman.ycor()<= 93)):
                    speed = a            
                elif ((-195 <= pacman.xcor() <= 190) and (3 <= pacman.ycor()<= -2)):
                    speed = a
                elif ((-195 <= pacman.xcor() <= 190) and (-92 <= pacman.ycor()<= -242)):
                    speed = a
        
                    #2nd col
                elif ((-169 <= pacman.xcor() <= -164) and (198 <= pacman.ycor()<= 185)):
                    speed = a
                elif ((-169 <= pacman.xcor() <= -164) and (150 <= pacman.ycor()<= 139)):
                    speed = a
                elif ((-169 <= pacman.xcor() <= -164) and (95 <= pacman.ycor()<= 102)):
                    speed = a
                elif ((-169 <= pacman.xcor() <= -164) and (-5 <= pacman.ycor()<= 5)):
                    speed = a
                elif ((-169 <= pacman.xcor() <= -164) and (-96 <= pacman.ycor()<= -91)):
                    speed = a
                elif ((-169 <= pacman.xcor() <= -164) and (-220 <= pacman.ycor()<= -92)):
                    speed = a
        
                    #3rd col
                elif ((-139 <= pacman.xcor() <= -144) and (197 <= pacman.ycor()<= 180)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -144) and (136 <= pacman.ycor()<= 152)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -144) and (95 <= pacman.ycor()<=103)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -144) and (5 <= pacman.ycor()<= -4)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -144) and (-99 <= pacman.ycor()<= -89)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -144) and (-193 <= pacman.ycor()<= 188)):
                    speed = a
                elif ((-139 <= pacman.xcor() <= -21) and (-241 <= pacman.ycor()<= -235)):
                    speed = a
                    
                    
        
                elif ((-193 <= pacman.xcor() <= -160) and ( 205<= pacman.ycor()<= -270)):#colom1
                    speed = a
                elif ((-133 <= pacman.xcor() <= -118) and (-200 <= pacman.ycor() <= 190)):#colom4
                    speed = a
                elif ((118 <= pacman.xcor() <= 133)and (-200<= pacman.ycor() <= 190) ):#colom14
                    speed = a 
            ##col17
                elif ((173 <= pacman.xcor() <= 215) and ( 189<= pacman.ycor()<= 102)):
                    speed = a
                elif ((173 <= pacman.xcor() <= 215) and ( 12<= pacman.ycor()<= -15)):
                    speed = a
                elif ((173 <= pacman.xcor() <= 215) and ( -70<= pacman.ycor()<= -249)):
                    speed = a
                    
            ###col16
                elif ((165 <= pacman.xcor() <=179 ) and ( -128<= pacman.ycor()<= -199)):
                    speed = a
            ###col15
                elif ((140 <= pacman.xcor() <=152 ) and ( 180<= pacman.ycor()<= 210)):
                    speed = a  
                elif ((140 <= pacman.xcor() <=152 ) and ( 158<= pacman.ycor()<= 128)):
                    speed = a  
                elif ((140 <= pacman.xcor() <=152 ) and ( 80<= pacman.ycor()<= 122)):
                    speed = a 
                elif ((140 <= pacman.xcor() <=152 ) and ( -10<= pacman.ycor()<= 15)):
                    speed = a 
                elif ((140 <= pacman.xcor() <=152 ) and ( -116<= pacman.ycor()<= -69)):
                    speed = a 
                elif ((140 <= pacman.xcor() <=152 ) and ( -252<= pacman.ycor()<= -183)):
                    speed = a 
                
            ###col12
                elif ((60 <= pacman.xcor() <=80 ) and ( 184<= pacman.ycor()<= 206)):
                    speed = a            
                elif ((60 <= pacman.xcor() <=80 ) and ( 80<= pacman.ycor()<= -156)):
                    speed = a
                elif ((60 <= pacman.xcor() <=80 ) and ( -90<= pacman.ycor()<= 50)):
                    speed = a
                elif ((60 <= pacman.xcor() <=80 ) and ( -198<= pacman.ycor()<= -150)):
                    speed = a            
        
            ###col6
                elif ((-80 <= pacman.xcor() <=-65 ) and ( 184<= pacman.ycor()<= 206)):
                    speed = a            
                elif ((-80 <= pacman.xcor() <=-65 ) and ( 80<= pacman.ycor()<= -156)):
                    speed = a
                elif ((-80 <= pacman.xcor() <=-65 ) and ( -90<= pacman.ycor()<= 50)):
                    speed = a
                elif ((-80 <= pacman.xcor() <=-65 ) and ( -198<= pacman.ycor()<= -150)):
                    speed = a
                elif ((-80 <= pacman.xcor() <=-65 ) and ( 96<= pacman.ycor()<= 165)):
                    speed = a        
                    #colom10
                elif ((12 <= pacman.xcor() <= 32) and (150 <= pacman.ycor()<= 200)):
                    speed = a
                elif ((12 <= pacman.xcor() <= 32) and (40 <= pacman.ycor()<= 115)):
                    speed = a
                elif ((12 <= pacman.xcor() <= 32) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
                    #colom8
                elif ((-33 <= pacman.xcor() <= -13) and (150 <= pacman.ycor()<= 200)):
                    speed = a
                elif ((-33 <= pacman.xcor() <= -13) and (40 <= pacman.ycor()<= 115)):
                    speed = a 
                elif ((-33 <= pacman.xcor() <= -13) and (-153 <= pacman.ycor()<=-75)):
                    speed = a
                elif ((-33 <= pacman.xcor() <= -13) and (-220 <= pacman.ycor()<= -210)):
                    speed = a
                    #colom1
                elif ((-205 <= pacman.xcor() <= -170)and (-250 <= pacman.ycor()<=-85)):
                    speed = a
                    #colom17
                elif ((189 <= pacman.xcor() <= 210)and (-250 <= pacman.ycor()<=-85)):
                    speed = a
                else:
                    speed = 0
                    pacman.back(1)
                     
########################Pacman movement and block from outside boundry#########


    ##################blueghost pattern#################
                blueghostMov()
    ####################pinkghost movement pattern##############################
                if pinkghost.xcor() ==6 and pinkghost.ycor() == 23:
                    pinkghost.setheading(90)
                if pinkghost.xcor() ==6 and pinkghost.ycor() ==50: #50
                    pinkghost.setheading(0)
                if pinkghost.xcor() ==70 and pinkghost.ycor() ==50: #78/80
                    pinkghost.setheading(270)
                if pinkghost.xcor() ==70 and pinkghost.ycor() ==-95: #90/89
                    pinkghost.setheading(0)
                if pinkghost.xcor() ==124 and pinkghost.ycor() == -95 : #78/80
                    pinkghost.setheading(270)
                if pinkghost.xcor() ==124 and pinkghost.ycor() ==-192: #90/89
                    pinkghost.setheading(0)
                if pinkghost.xcor() ==199 and pinkghost.ycor() == -192 : #78/80
                    pinkghost.setheading(270)
                if pinkghost.xcor() ==199 and pinkghost.ycor() == -240 : #78/80
                    pinkghost.setheading(180)
                if pinkghost.xcor() ==-195 and pinkghost.ycor() == -240 : #78/80
                    pinkghost.setheading(90)
                if pinkghost.xcor() ==-195 and pinkghost.ycor() == -100 : #78/80
                    pinkghost.setheading(0)
                if pinkghost.xcor() ==-65 and pinkghost.ycor() == -100 : #78/80
                    pinkghost.setheading(90)
                if pinkghost.xcor() ==-65 and pinkghost.ycor() == 50 : #78/80
                    pinkghost.setheading(0)
    ####################redghost movement pattern##############################    
                if redghost.xcor() ==-120 and redghost.ycor() ==1:
                    redghost.seth(270)#up
                if redghost.xcor() ==-120 and redghost.ycor() ==144:
                    redghost.seth(180)#right
                if redghost.xcor() ==125 and redghost.ycor() ==144:
                    redghost.setheading(90)#down
                if redghost.xcor() ==125 and redghost.ycor() ==-140:
                    redghost.setheading(0)#left
                if redghost.xcor() ==-120 and redghost.ycor() ==-140:
                    redghost.setheading(270)#left
    ####################orangeghost movement pattern##############################
                if orangeghost.xcor() ==-4 and orangeghost.ycor() ==1:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==-4 and orangeghost.ycor() ==-45:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==-4 and orangeghost.ycor() ==-45:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==75 and orangeghost.ycor() ==-45:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==75 and orangeghost.ycor() ==-100:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==-100:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==-145:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==75 and orangeghost.ycor() ==-145:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==75 and orangeghost.ycor() ==-195:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==-195:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==-240:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==-240:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==-195:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==-75 and orangeghost.ycor() ==-195:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-75 and orangeghost.ycor() ==-145:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==-145:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==-100:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==-70 and orangeghost.ycor() ==-100:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-70 and orangeghost.ycor() ==50:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==50:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-25 and orangeghost.ycor() ==100:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==-70 and orangeghost.ycor() ==100:
                    orangeghost.setheading(90)
                if orangeghost.xcor() ==-70 and orangeghost.ycor() ==145:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==70 and orangeghost.ycor() ==145:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==70 and orangeghost.ycor() ==100:
                    orangeghost.setheading(180)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==100:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==100:
                    orangeghost.setheading(270)
                if orangeghost.xcor() ==25 and orangeghost.ycor() ==45:
                    orangeghost.setheading(0)
                if orangeghost.xcor() ==75 and orangeghost.ycor() ==45:
                    orangeghost.setheading(270)
    
                pinkghost.forward(1)
                redghost.backward(1)
                orangeghost.forward(1)          

##################for booster power
                if ((400 <= score <= 430)):
                    boost.shape("booster.gif")
                    boost.setpos(0,50)
                    boost.pendown()
                else:
                    boost.pu()
                    boost.setpos(-550,-550)
                    #boost.ht()
                if (isCollision(pacman,boost) is True):              
                    winsound.PlaySound('boost-collect.wav', winsound.SND_ASYNC)
                    boost.pu()
                    boost.ht()
                    boost.goto(-550,-550)
                    mazepen.undo()
                    score +=50 #############score +50 wehn booster taken#####
                    a += 1
                    scorestring = "score: %s" %score
                    mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal")) 
           
#####################for ghost power#######################                
                if ((70 <= timeleft <= 75)or(40 <= timeleft <= 45)):
                    ghost.setpos(0,190)
                    ghost.pd()
                    ghost.shape("ghost.gif")
                else:
                    ghost.pu()
                    ghost.setpos(-550,-550)
                if (isCollision(pacman,ghost) is True):
                    ghost.ht()
                    ghost.pu()
                    ghost.goto(-550,-550)
                    mazepen.undo()
                    score =0################score zero
                    scorestring = "score: %s" %score
                    mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal")) 
                    winsound.PlaySound('pacman_extrapac.wav', winsound.SND_FILENAME)
###################FOR CHERRY POWER#########    
                if ((20 <= timeleft <= 25)or (0 <= timeleft <= 5)):
                    cherry.setpos(0,-240)
                    cherry.pd()
                    cherry.shape("cherry.gif")
                elif (10 <= timeleft <= 15):
                    cherry.setpos(0,200)
                    cherry.pd()
                    cherry.shape("cherry.gif")                    
                else:
                    cherry.pu()
                    cherry.setpos(-550,-550)
                if (isCollision(pacman,cherry) is True):
                    cherry.ht()
                    cherry.pu()
                    score +=50
                    playtime += 10##############time increase by 10sec
                    cherry.goto(-550,-550)
                    mazepen.undo()
                    winsound.PlaySound('boost-collect.wav', winsound.SND_ASYNC)
                if isCollision(pacman,clock):
                    clock.ht()
                    clock.pu()
                    clock.goto(-550,-550)
                    score -= 50
                    playtime +=50
                    mazepen.undo()
                    mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal")) 
                if timeleft ==10:
                    winsound.PlaySound('pacman_timewarning.wav', winsound.SND_ASYNC)
                    
                    ##################strawberry power#####
                if (30<=score <=50)or (160 <= score <=180)or (220<= score<=240)or(660<=score<=680)or (1400<=score<=1420):
                    straberry.setpos(190,97)
                    straberry.pd()
                    straberry.shape("straberry.gif")
                  
                else:
                    straberry.pu()
                    straberry.setpos(-550,-550)
                      
                if (isCollision(pacman,straberry)is True):
                    straberry.ht()
                    straberry.pu()
                    score += 25    #####score increses by 10
                    straberry.goto(-550,-550)
                    mazepen.undo()
                    mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal"))
    
                    
###################apple power############
                if (60<= score <=70) or (300<=score<=310 ) or (430<= score<= 440) or (600<=score<=610):
                     apple.setpos(190,-168)
                     apple.pd()
                     apple.shape("apple.gif")
                else:
                     apple.pu()
                     apple.setpos(-550,-550)
                     
                if (isCollision(pacman,apple)is True):
                     apple.ht()
                     apple.pu()
                     score += 35 #######score increases by 35
                     apple.goto(-550,-550)
                     mazepen.undo()
                     mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal"))
                     
##############################for eating coins
                for i in (coinlist):
                    if isCollision(pacman,i):
                        coinlist.append(i)
                        i.goto(-250,-300)
                        count.append(i)
                        i.ht()
                        winsound.PlaySound('pacman_chomp.wav', winsound.SND_ASYNC)
                        score +=10#############score increase by 10
                        mazepen.undo()
                        mazepen.penup()
                        mazepen.ht()
                        mazepen.setposition(-225,235)
                        mazepen.color("white")
                        scorestring = "score: %s" %score
                        mazepen.write(scorestring, False, align="left",font=("chiller",20,"normal"))  

#####################you win technique
                if len(count) == 183:
                    window.reset()
                    window.bgpic("youwin.gif")
                    winsound.PlaySound('pacman-youwin.wav', winsound.SND_ASYNC)
                    turtle.done()
                elif(life == 0):###############when life 0 game over
                    winsound.PlaySound('pacman_timeup.wav', winsound.SND_ASYNC)
                    window.reset()
                    window.bgpic("youlost.gif")
                    turtle.done()

                    
    #####################collision with enemy################                                    
                if isCollision(pacman,pinkghost):
                    life -= 1                
                    pacman.penup()
                    pacman.setpos(0,-50)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    centerpen.undo()
                    centerpen.ht()
                    centerpen.setpos(160,235)
                    lifestring = "LIFE: %s" %life
                    centerpen.color("white")
                    centerpen.write(lifestring, False, align="left",font=("chiller",20,"normal"))
                if isCollision(pacman,redghost):
                    life -= 1                
                    pacman.penup()
                    pacman.setpos(0,-50)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    centerpen.undo()
                    centerpen.ht()
                    centerpen.setpos(160,235)
                    lifestring = "LIFE: %s" %life
                    centerpen.color("white")
                    centerpen.write(lifestring, False, align="left",font=("chiller",20,"normal"))                            
                if isCollision(pacman,orangeghost):
                    life -= 1                
                    pacman.penup()
                    pacman.setpos(0,-50)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    centerpen.undo()
                    centerpen.ht()
                    centerpen.setpos(160,235)
                    lifestring = "LIFE: %s" %life
                    centerpen.color("white")
                    centerpen.write(lifestring, False, align="left",font=("chiller",20,"normal"))                           
                if isCollision(pacman,blueghost):
                    life -= 1                
                    pacman.penup()
                    pacman.setpos(0,-50)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    winsound.PlaySound('pacman_death.wav', winsound.SND_FILENAME)
                    centerpen.undo()
                    centerpen.ht()
                    centerpen.setpos(160,235)
                    lifestring = "LIFE: %s" %life
                    centerpen.color("white")
                    centerpen.write(lifestring, False, align="left",font=("chiller",20,"normal"))                                         
                                

            else:#################when time over
                timeup()
                break
                    
            window.update()
            #################################       

    turtle.listen()
    turtle.onkey(nextpage,"space")
   
    while True:
        for i in range (50):
            mazepen.penup()
            mazepen.hideturtle()
            mazepen.fd(100)
            mazepen.left(90)

            
   
############calling the main function to start the game##################            
main()
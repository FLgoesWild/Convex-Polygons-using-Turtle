#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:01:35 2022

@author: feriellaafif
"""

import random 
import turtle
import math
import time
 
turtle.speed(0)
turtle.hideturtle()

class Point:
   def __init__(self,i,j):
     self.x = i
     self.y = j
   def __repr__(self):
     return "("+str(self.x)+","+str(self.y)+")"
   def __eq__(self,other):
     return self.x==other.x and self.y==other.y
 
#Exo 1 : Question 1 OK

def randpoint(min_x,min_y, max_x, max_y):
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    return Point(x,y)

#Exo 1 : Question 2 OK

def drawpoint(p):
    turtle.penup()
    turtle.setpos(p.x,p.y)
    turtle.dot(5,)
    turtle.penup()
    return
    
    
#Exo 1 : Question 3 OK

def drawpoly(l):
    turtle.color('black')
    turtle.penup()
    turtle.goto(l[0].x, l[0].y)
    turtle.pendown()
    for i in range(1,len(l)):
        turtle.goto(l[i].x,l[i].y)
    turtle.goto(l[0].x, l[0].y)
    turtle.penup()
    return

#Exo 1 : Question 4 -> Utiliser l = trigosort(l,p) OK

def trigosort(l,p):
    l_angle = []
    for i in range(len(l)):
        pA = l[i].x-p.x
        d = math.sqrt((l[i].x-p.x)**2+(l[i].y-p.y)**2)
        if d == 0:
            angle = 0
        else :
            angle = math.acos(pA/d)
        if l[i].y < p.y:
            angle = 2*math.pi - angle
        l_angle.append(angle)
    l_angle, l = zip(*sorted(zip(l_angle, l), key = lambda x: x[0]))
    return l 
 
#Exo 1 : Question 5 OK
    
Points = []
for j in range(100):
    Points.append(randpoint(-200, -200, 200, 200))
    drawpoint(Points[j])
Points = trigosort(Points, Point(0,0))
drawpoly(Points)

#Exo 2 : Question 1 OK


def notconvex(l):
    v1=[l[-3].x-l[-2].x,l[-3].y-l[-2].y]
    v2=[l[-1].x-l[-3].x,l[-1].y-l[-3].y]
    if (v1[0]*v2[1] - v1[1]*v2[0]) < 0:
        return False
    else:
        return True


def convexhull(l):
    l_trié = sorted(l, key = lambda l: l.y)
    p_min = l_trié[0]
    l_sommets = [p_min]
    del l_trié[0]

    l = trigosort(l_trié,p_min)
   
    l_sommets.append(l[0])

    for i in range(1,len(l)):
        l_sommets.append(l[i])
        if len(l_sommets)>3:
            while notconvex(l_sommets)==True and len(l_sommets)>3: #angle>180° donc concave
                   del l_sommets[-2]
    return l_sommets

#Exo 2 : Question 3 OK

def drawconvexhull(l):
    turtle.color('black')
    turtle.penup()
    l_trié = sorted(l, key = lambda l: l.y)
    p_min = l_trié[0]
    l_sommets = [p_min]
    turtle.goto(l_sommets[0].x, l_sommets[0].y)
    turtle.pendown()
    del l_trié[0]

    l = trigosort(l_trié,p_min)
   
    l_sommets.append(l[0])
    time.sleep(0.1)
    turtle.goto(l_sommets[1].x, l_sommets[1].y)

    for i in range(1,len(l)):
        l_sommets.append(l[i])
        time.sleep(0.1)
        turtle.goto(l_sommets[-1].x, l_sommets[-1].y)
        if len(l_sommets)>3:
            while notconvex(l_sommets)==True and len(l_sommets)>3: #angle>180° donc concave
                   del l_sommets[-2]
                   turtle.undo()
                   time.sleep(0.1)
                   turtle.undo()
                   time.sleep(0.1)
                   turtle.goto(l_sommets[-1].x, l_sommets[-1].y)
                   time.sleep(0.1)
    turtle.goto(l_sommets[0].x, l_sommets[0].y)                  
    turtle.penup()
    return l_sommets
          

#Exo 2 : Question 4 OK

for i in range(len(Points)+1):
    turtle.undo()

drawconvexhull(Points)


#Test drawconvexhull(l)

'''Points = []
for j in range(40):
    Points.append(randpoint(-200, -200, 200, 200))
    drawpoint(Points[j])
drawconvexhull(Points)'''


#Test du temps d'éxecution

'''Points = []
for j in range(250000):
    Points.append(randpoint(-200, -200, 200, 200))
start = time.process_time() 
convexhull(Points)
print("Temps d'exécution :",time.process_time()-start,"seconde(s)")'''

#Exo 3 : Question 2 OK

def AntipodalPair(l):
    y_min=0
    y_max=0
    for i in range(1,len(l)):
        if(l[y_min].y > l[i].y):
            y_min = i
        if(l[y_max].y < l[i].y):
            y_max = i
            
    return [y_min,y_max] #Position dans la liste, pas les valeurs des ordonnées

#Test AntipodalPair
    
'''Points = [Point(0,0),Point(0,-1),Point(0,-5),Point(5,5),Point(5,10)]
print(AntipodalPair(Points))'''

    
#Exo 3 : Question 3 OK

# Retourne l'angle entre vecteur V_A et le vecteur entre les points l[a] et l[b]

def angle(a,b,V_A,l): 
    V_AB = [l[b].x-l[a].x,l[b].y-l[a].y]
    scal = V_A[0]*V_AB[0] + V_A[1]*V_AB[1]
    norm = math.sqrt(V_A[0]**2+V_A[1]**2) * math.sqrt(V_AB[0]**2+V_AB[1]**2)
    tetha = math.acos(scal/norm)
    return tetha 
    
''' Test de angle
l=[Point(0,0),Point(1,0)]
Vecteur = [-1,0]
print(angle(0,1,Vecteur,l) )'''

def NextAntipodalPair(l, i, j):
    
    '''#Sert à trier les points, au cas où ils ne le seraient pas (à priori ils le sont)
    p_min = sorted(l, key = lambda l: l.y)[0]
    l = trigosort(l,p_min)'''
    
    Vecteur_ij = [l[j].x-l[i].x,l[j].y-l[i].y]
    
    Vecteur1 = [-Vecteur_ij[1],Vecteur_ij[0]]
    Vecteur2 = [x * (-1) for x in Vecteur1] #inverse de Vecteur1
    
    Tetha_i = angle(i,i-1,Vecteur1,l)
    Tetha_j = angle(j,j-1,Vecteur2,l)
    
    Tetha_min = min(Tetha_i,Tetha_j)
    
    if Tetha_min == Tetha_j:
        return [i,j-1 %(len(l))]
    else: #Si Tetha_min = Tetha_i
        return [(i-1) %(len(l)),j]
   
    
#Test AntipodalPair
       
'''l=[Point(0,0),Point(2,2),Point(3,6),Point(-1,7),Point(-2,4),Point(-3,-2)]

print(NextAntipodalPair(l,0,3))'''


#Exo 3 : Question 4 OK

def diameter(l):
    l_antipodaux = []
    l_antipodaux.append(AntipodalPair(l))
    for i in range(len(l)-1):
        l_antipodaux.append(NextAntipodalPair(l, l_antipodaux[i][0], l_antipodaux[i][1]))
    l_antipodaux_distances = []
    for i in range(len(l_antipodaux)):
        Point1 = Point(l[l_antipodaux[i][0]].x,l[l_antipodaux[i][0]].y)
        Point2 = Point(l[l_antipodaux[i][1]].x,l[l_antipodaux[i][1]].y)
        l_antipodaux_distances.append(math.sqrt( (Point2.x-Point1.x)**2 + (Point2.y-Point1.y)**2 ))
    return max(l_antipodaux_distances)

#Test Diameter

'''       
l=[Point(0,0),Point(2,2),Point(3,6),Point(-1,7),Point(-2,4),Point(-3,-2)]
print(diameter(l))'''

#Exo 3 : Question 5 OK

def drawdiameter(l):
    
    turtle.pensize(2)
    
    turtle.penup()
    
    l_antipodaux = []
    l_antipodaux.append(AntipodalPair(l))
    
    for i in range(len(l)-1):
    
        
        l_antipodaux.append(NextAntipodalPair(l, l_antipodaux[i][0], l_antipodaux[i][1]))
        
        turtle.penup()
        turtle.goto(l[l_antipodaux[i][0]].x,l[l_antipodaux[i][0]].y)
        turtle.pencolor('blue')
        turtle.pendown()
        turtle.goto(l[l_antipodaux[i][1]].x,l[l_antipodaux[i][1]].y)
        
        Vecteur_ij = [l[l_antipodaux[i][0]].x-l[l_antipodaux[i][1]].x,l[l_antipodaux[i][0]].y-l[l_antipodaux[i][1]].y]
        
        Vecteur1 = [-Vecteur_ij[1],Vecteur_ij[0]]
        Vecteur2 = [x * (-1) for x in Vecteur1]
        
        turtle.pencolor('black')
        
        turtle.penup()
        turtle.goto(l[l_antipodaux[i][0]].x,l[l_antipodaux[i][0]].y)
        turtle.pendown()
        turtle.goto(l[l_antipodaux[i][0]].x+Vecteur1[0],l[l_antipodaux[i][0]].y+Vecteur1[1])
        
        turtle.penup()
        turtle.goto(l[l_antipodaux[i][1]].x,l[l_antipodaux[i][1]].y)
        turtle.pendown()
        turtle.goto(l[l_antipodaux[i][1]].x+Vecteur2[0],l[l_antipodaux[i][1]].y+Vecteur2[1])
        
        time.sleep(0.3)
        for i in range(11):
            turtle.undo()
        
        turtle.penup()
        
    l_antipodaux_distances = []
    
    for i in range(len(l_antipodaux)):
        Point1 = Point(l[l_antipodaux[i][0]].x,l[l_antipodaux[i][0]].y)
        Point2 = Point(l[l_antipodaux[i][1]].x,l[l_antipodaux[i][1]].y)
        l_antipodaux_distances.append(math.sqrt( (Point2.x-Point1.x)**2 + (Point2.y-Point1.y)**2 ))
    
    nb = 0
    for i in range (1,len(l_antipodaux_distances)):
        if l_antipodaux_distances[i] > l_antipodaux_distances[nb]:
            nb = i
      
    
    turtle.penup()
    turtle.pencolor('red')
    turtle.goto(l[l_antipodaux[nb][0]].x,l[l_antipodaux[nb][0]].y)
    turtle.pendown()
    turtle.goto(l[l_antipodaux[nb][1]].x,l[l_antipodaux[nb][1]].y)
    turtle.penup()
    turtle.pencolor('black')
    
    turtle.pensize(1)
    
    return max(l_antipodaux_distances)

#Test DrawDiameter

'''Points = []
for j in range(50):
    Points.append(randpoint(-200, -200, 200, 200))
    drawpoint(Points[j])
Points = trigosort(Points, Point(0,0))
drawpoly(convexhull(Points))
print(drawdiameter(convexhull(Points)))'''
      
'''l=[Point(0,0),Point(80,80),Point(120,240),Point(-40,280),Point(-80,160),Point(-120,-80)]
l = trigosort(l, Point(-120,-80))
print(l)
drawpoly(l)
print(drawdiameter(l))'''

#Exercice 3 : Question 6

'''Points = []
for j in range(300000):
    Points.append(randpoint(-200, -200, 200, 200))
start = time.process_time() 
diameter(Points)
print("Temps d'exécution :",time.process_time()-start,"seconde(s)")'''

#Exercice 3 : Question 7

drawdiameter(convexhull(Points))




'''l=[Point(100,0),Point(0,100),Point(-100,0),Point(0,-100)]
p=Point(0,0)
drawpoint(p)
drawpoly(l)'''

'''l=[Point(100,100),Point(-100,100),Point(-100,-100),Point(100,-100)]

p=Point(0,0)

trigosort(l,p)

drawpoint(Point(0,0))    
'''



turtle.Screen().exitonclick()


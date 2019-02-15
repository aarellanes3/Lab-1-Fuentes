# -*- coding: utf-8 -*-
"""
#Created on Wed Jan 30 10:50:08 2019

#@author: aarel
"""
#Andres Arellanes
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k')
        
    draw_squares(ax,n-1,p//2,w)
    draw_squares(ax,n-1,p//2,w)
    draw_squares(ax,n-1,p//2,w)
    draw_squares(ax,n-1,p//2,w)
    
        
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles2(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        new_radius = radius*(2//3)
        new_center = center[0]+new_radius,radius[1]
        draw_circles2(ax,n-1,center,radius*w,w)
        draw_circles2(ax,n-1,center,new_radius,w)
        draw_circles2(ax,n-1,center,new_radius*w,w)
        draw_circles2(ax,n-1,center,new_radius*w,w)
        draw_circles2(ax,n-1,center,new-radius*w,w)
        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax,2, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circle_ diagram.png')

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        new_center= center[0]*w,center[1]
        draw_circles(ax,n-1, new_center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 100, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('shifting_circles.png')

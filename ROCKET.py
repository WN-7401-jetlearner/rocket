import pygame
from pygame.locals import*
pygame.init()
height=500
width=600
screen=pygame.display.set_mode((width,height))
running=True
#keys=[left,right,down,up]
keys = [False, False, False,False]


galaxy=pygame.image.load("C:\\Users\\muham\\OneDrive\\Pictures\\Desktop\\Jet learn WANIYA\\Python Game Developer\\images\\galaxy.png")
rocket=pygame.image.load("C:\\Users\\muham\\OneDrive\\Pictures\\Desktop\\Jet learn WANIYA\\Python Game Developer\\images\\sally.png")

x=200
y=200




while running:
 screen.blit(galaxy,(0,0))
 screen.blit(rocket,(x,y))
 for i in pygame.event.get():I
  if i.type==pygame.QUIT:
   running=False
  elif i.type==pygame.KEYDOWN:
    if i.key==K_DOWN:
      keys[2]=True
    elif i.key==K_UP:
      
    


      
  elif i.type==pygame.KEYUP:
   if i.key==K_UP:
    keys[3]=True

  if keys[2]:
    y+=5


  

      

 pygame.display.update()

 
 pygame.display.update()



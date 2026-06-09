import pygame
pygame.init()
height=500
width=600
screen=pygame.display.set_mode((width,height))
running=True
galaxy=pygame.image.load("C:\\Users\muham\\OneDrive\\Pictures\\Desktop\\Jet learn WANIYA\\Python Game Developer\\images\\galaxy.png")
rocket=pygame.image.load("C:\\Users\\muham\\OneDrive\\Pictures\\Desktop\\Jet learn WANIYA\\Python Game Developer\\images\\sally.png")
while running:
 for i in pygame.event.get():
  if i.type==pygame.QUIT:
   running=False
  pygame.display.update()

  screen.blit(galaxy,(0,0))
  screen.blit(rocket,(200,200))
  pygame.display.update()
  









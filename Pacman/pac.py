import os
import pygame
import time

from random import randint
import math

map =1
showDistGrid=1
Ghost1=1
Ghost2=0
blocker=0
showPath=1
follow=1

xGrid = 19 #19
yGrid = 25 #25
height = yGrid*40
width = xGrid*40
valPlayer=9998
pygame.init()
widthBlock=width//xGrid

Current_Grid = [[9999 for i in range(xGrid)] for j in range(yGrid)]
if map==1:
    Current_Grid=[[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-2, 10, 11, 12, 11, 10, 9, 8, 7, 8, 8, 9, 10, 11, 12, 13, 12, 11, -2], [-2, 9, -2, -2, -2, -2, -2, -2, 6, -2, 7, -2, -2, -2, -2, -2, -2, 10, -2], [-2, 8, 7, 6, 5, -2, 3, 4, 5, -2, 6, 5, 4, -2, 6, 7, 8, 9, -2], [-2, -2, 8, -2, 4, -2, 2, -2, -2, -2, -2, -2, 3, -2, 5, -2, 9, -2, -2], [-2, 7, 8, -2, 3, 2, 1, 1, 1, 1, 1, 1, 2, 3, 4, -2, 8, 7, -2], [-2, 6, -2, -2, 3, -2, -2, -2, 1, -2, 2, -2, -2, -2, 3, -2, -2, 6, -2], [-2, 5, 4, 3, 2, 1, 1, 1, 1, -2, 3, 4, 5, 5, 4, 3, 4, 5, -2], [-2, -2, -2, -2, 3, -2, 1, -2, -2, -2, -2, -2, 4, -2, 3, -2, -2, -2, -2], [9999, 9999, 9999, -2, 4, -2, 1, 1, 1, 1, 1, 2, 3, -2, 4, -2, 9999, 9999, 9999], [-2, -2, -2, -2, 5, -2, 1, -2, -2, 1, -2, -2, 4, -2, 5, -2, -2, -2, -2, -2], [8, 7, 6, 5, 4, 3, 2, -2, 1, 1, 1, -2, 5, 4, 4, 5, 6, 7, 8], [9, 8, 7, 6, 5, 4, 3, -2, 1, 1, 1, -2, 4, 3, 4, 5, 6, 7, 8], [9, 9, 8, 7, 6, 5, 4, -2, 1, 0, 9000, -2, 3, 3, 4, 5, 6, 7, 8], [-2, -2, -2, -2, 7, -2, 5, -2, -2, -2, -2, -2, 2, -2, 5, -2, -2, -2, -2, -2], [9999, 9999, 9999, -2, 8, -2, 5, 6, 5, 4, 3, 2, 3, -2, 6, -2, 9999, 9999, 9999], [-2, -2, -2, -2, 9, -2, 6, -2, -2, -2, -2, -2, 4, -2, 7, -2, -2, -2, -2], [-2, 12, 11, 10, 9, 8, 7, 8, 9, -2, 7, 6, 5, 6, 7, 8, 9, 10, -2], [-2, 13, -2, -2, 10, -2, -2, -2, 10, -2, 8, -2, -2, -2, 8, -2, -2, 11, -2], [-2, 14, 15, -2, 11, 12, 13, 12, 11, 10, 9, 10, 11, 10, 9, -2, 13, 12, -2], [-2, -2, 9999, -2, 12, -2, 14, -2, -2, -2, -2, -2, 12, -2, 10, -2, 14, -2, -2], [-2, 9999, 15, 14, 13, -2, 15, 9999, 9999, -2, 15, 14, 13, -2, 11, 12, 13, 14, -2], [-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 15, -2], [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]

y=0
if blocker>0:
    y=0
    while (y < yGrid and blocker>1):
        x=0
        while (x < xGrid):
            if(y==0 or x==0 or y == yGrid-1 or x==xGrid-1 ):
                Current_Grid[y][x] =-2
            x += 1
        y+=1
    y=0
    while(y<yGrid and blocker %2==1):
        Current_Grid[y][xGrid//2] = -2
        y+=1
counter=0
while (counter < (xGrid * yGrid)):
    x = counter // xGrid
    y = counter % xGrid
    if Current_Grid[x][y] != -2:
        Current_Grid[x][y] = 9999
    counter+=1

xPlayerStart=17
yPlayerStart=1

xGhost1Start=2
yGhost1Start=19

xGhost2Start=2
yGhost2Start=12

Current_Grid[yGhost1Start][xGhost1Start] = 0
Current_Grid[yGhost2Start][xGhost2Start] =9999-Ghost2*10000
Current_Grid[yPlayerStart][xPlayerStart] = valPlayer

follow2=0
if follow==0:
	follow2=1
	
w = pygame.display.set_mode((width, height))









def main ():

    counter=0
    while (counter < (xGrid * yGrid)):
        x = counter // xGrid
        y = counter % xGrid
        if Current_Grid[x][y] == valPlayer: 
            break
        counter+=1
    yPlayer=x
    xPlayer=y
    
    counter=0
    while (counter < (xGrid * yGrid)):
        y = counter // xGrid
        x = counter % xGrid
        if Current_Grid[y][x] == 0:
            break
        counter+=1
    yGhost=y
    xGhost=x


    run=True

    def grn(dist,yGhost,xGhost,moveGh0st,valGhost):
        if showDistGrid==1:
            font = pygame.font.Font(None, 20)

        counter = 0
        while (counter < (xGrid * yGrid)):
            y = counter // xGrid
            x = counter % xGrid            
            if Current_Grid[y][x] == valPlayer:
                break                
            counter += 1

        while (dist>0):

            if x > 0 and Current_Grid[y][x - 1] == dist:
                x -=1
                
            elif x == 0  and  Current_Grid[y][xGrid-1] == dist :
                x =xGrid-1

            elif y > 0 and Current_Grid[y - 1][x] == dist:
                y -=1
                
            elif y == 0  and  Current_Grid[yGrid-1][x] == dist :
                y =yGrid-1

            elif x < xGrid and Current_Grid[y][(x + 1)%xGrid] == dist:
                x=(x+1) %xGrid

            elif y < yGrid - 1 and Current_Grid[(y + 1)%yGrid][x] == dist:
                y=(y+1)%yGrid
                
            if showPath==1:
                pygame.draw.rect(w, (70, 170, 60), (x * widthBlock, y * widthBlock, widthBlock, widthBlock))
                
            if showDistGrid == 1 and showPath==1:
                text = font.render(str(dist), True, (90, 90, 170))
                trex = text.get_rect()
                trex.topleft = (x * widthBlock , y * widthBlock)
                w.blit(text, trex)
                
            if dist==1 and moveGh0st==1 and ((abs(yGhost-y)+1)%xGrid<3 and (abs(xGhost-x)+1)%xGrid<3 ) :
                Current_Grid[yGhost][xGhost] = 9999
                yGhost = y
                xGhost = x
                Current_Grid[yGhost][xGhost] = valGhost
                
            else:
                Current_Grid[y][x]=9999
                
            dist -= 1
            
    def path(moveGhost):
    
        run=True
        font = pygame.font.Font(None, 20)
        dist=0
        found=0
        
        counter=0
        while (counter < (xGrid * yGrid)):
            y = counter // xGrid
            x = counter % xGrid
            if Current_Grid[y][x] == valPlayer:
                break
            counter += 1


        while(run and Ghost1==1):
        
            counter = 0
            
            while(counter<(xGrid * yGrid)):

                y2 = (counter // xGrid)
                x2 = counter % xGrid
                counter+=1
                if dist>51:
                    col=255
                else:
                    col=5*dist

                if Current_Grid[y2][x2] == dist:

                    if  Current_Grid[y2][x2-1] > dist:
                    
                        if Current_Grid[y2][x2 - 1] == valPlayer:
                            run=False
                            found=1
                            
                        else:
                            
                            Current_Grid[y2][x2 - 1]=dist+1
                            
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255-col,255- col,col), (x2 * widthBlock -widthBlock, y2 * widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock -widthBlock, y2 * widthBlock)
                                w.blit(text, trex)
                                
                    if y2>0 and Current_Grid[y2-1][x2] > dist :
                    
                        if Current_Grid[y2 - 1][x2] == valPlayer:
                            run=False
                            found = 1
                        
                        else:

                            Current_Grid[y2 - 1][x2] = dist + 1
                            
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255-col,255- col,col), (x2 * widthBlock, y2 * widthBlock -widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock, y2 * widthBlock - widthBlock)
                                w.blit(text, trex)
                                
                    if Current_Grid[y2][(x2  + 1)% xGrid] > dist:
                    
                        if Current_Grid[y2][(x2  + 1)% xGrid] == valPlayer:
                            run=False
                            found = 1
                        
                        else:
                            
                            Current_Grid[y2][(x2  + 1)% xGrid] = dist + 1
                            
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255-col, 255-col,col), (x2 * widthBlock +widthBlock, y2 * widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock + widthBlock, y2 * widthBlock)
                                w.blit(text, trex)
                                
                    if y2<yGrid-1 and  Current_Grid[y2+1][x2] > dist:
                    
                        if Current_Grid[y2+ 1][x2] == valPlayer:
                            run=False
                            found = 1
                            
                        else:
                            
                            Current_Grid[y2+ 1][x2] = dist + 1
                            
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255-col,255- col,col), (x2 * widthBlock, y2 * widthBlock +widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock, y2 * widthBlock + widthBlock)
                                w.blit(text, trex)

            dist += 1
            if dist>999:
                break

        if Ghost1==1:
	        if (found==1):
	            grn(dist-1,yGhost,xGhost,moveGhost,0)    
	        pygame.draw.rect(w, (170, 60, 80), (x * widthBlock, y * widthBlock, widthBlock, widthBlock))
	        pygame.draw.rect(w, (200, 90, 50), (xGhost * widthBlock, yGhost * widthBlock, widthBlock, widthBlock))
	        
        if (Ghost2==1):
        	res()
	        dist=0
	        yGhost2=0
	        xGhost2=0
	        run=True
	        found = 0
	        distMani=1
	        
	        counter = 0
        	while (counter < (xGrid * yGrid)):
	            y = counter // xGrid
	            x = counter % xGrid
	            if Current_Grid[y][x] == -1:
	                break
	            counter += 1
	        yGhost2 = y
	        xGhost2 = x
	
        while (run and Ghost2==1):

            counter = 0
            while (counter < (xGrid * yGrid)):

                y2 = (counter // xGrid)

                x2 = counter % xGrid
                counter += 1
                if dist > 51:
                    col = 255
                else:
                    col = 5 * dist



                if Current_Grid[y2][x2] == dist-distMani  :

                    if Current_Grid[y2][x2 - 1] > dist:
                        if Current_Grid[y2][x2 - 1] == valPlayer:
                            run = False
                            found = 1
                        else:
                            
                            Current_Grid[y2][x2 - 1] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255 - col, 255 - col, col), (x2 * widthBlock - widthBlock, y2 * widthBlock, widthBlock, widthBlock))

                                text = font.render(str(dist), True, (50, 50, 50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock - widthBlock, y2 * widthBlock)
                                w.blit(text, trex)
                    if y2 > 0 and Current_Grid[y2 - 1][x2] > dist:
                        if Current_Grid[y2 - 1][x2] == valPlayer:
                            run = False
                            found = 1
                        else:
                            
                            Current_Grid[y2 - 1][x2] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255 - col, 255 - col, col), (x2 * widthBlock, y2 * widthBlock - widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50, 50, 50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock, y2 * widthBlock - widthBlock)
                                w.blit(text, trex)
                    if Current_Grid[y2][(x2 + 1) % xGrid] > dist:
                        if Current_Grid[y2][(x2 + 1) % xGrid] == valPlayer:
                            run = False
                            found = 1
                        else:

                            Current_Grid[y2][(x2 + 1) % xGrid] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255 - col, 255 - col, col), (x2 * widthBlock + widthBlock, y2 * widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50, 50, 50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock + widthBlock, y2 * widthBlock)
                                w.blit(text, trex)
                    if y2 < yGrid - 1 and Current_Grid[y2 + 1][x2] > dist:
                        if Current_Grid[y2 + 1][x2] == valPlayer:
                            run = False
                            found = 1
                        else:
                           
                            Current_Grid[y2 + 1][x2] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w, (255 - col, 255 - col, col), (x2 * widthBlock, y2 * widthBlock + widthBlock, widthBlock, widthBlock))
                                text = font.render(str(dist), True, (50, 50, 50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock, y2 * widthBlock + widthBlock)
                                w.blit(text, trex)

            dist += 1
            distMani=0

            if dist > 999:
                break

        if (found == 1 and Ghost2==1):
            grn(dist - 1, yGhost2, xGhost2, moveGhost,-1)
        if (Ghost2==1):
        	pygame.draw.rect(w, (170, 60, 80), (x * widthBlock, y * widthBlock, widthBlock, widthBlock))
        	pygame.draw.rect(w, (200, 90, 50), (xGhost2 * widthBlock, yGhost2 * widthBlock, widthBlock, widthBlock))

    def res():
        counter = 0
        while (counter < (xGrid * yGrid)):
            y = counter // xGrid
            x = counter % xGrid
            if Current_Grid[y][x] > 0 and Current_Grid[y][x] < valPlayer:
                Current_Grid[y	][x] = 9999
            counter += 1
    click=0
    pr=0
    ticker=0
    clock = pygame.time.Clock()
    pv = 1
    movePlayer = 0
    tic=0
    while(run):
        res()

        ticker=(ticker+1)%45*follow + follow2
        clock.tick(60)
        if(tic>0):
            tic-=1
        counter=0
        while (counter < (xGrid * yGrid)):
            x = counter // xGrid
            y = counter % xGrid
            if Current_Grid[x][y] == 0:
                break
            counter += 1
        yGhost = x
        xGhost = y
        counter=0
        yy=0
        Mouse_Loc = pygame.mouse.get_pos()
        while(counter<(xGrid * yGrid)):
            x=counter//xGrid
            y=counter%xGrid
            if Current_Grid[x][y]==-2:
                pygame.draw.rect(w, (20, 35, 80), (y * widthBlock, x * widthBlock, widthBlock, widthBlock))
            elif (counter%2==0 and yy%2==0) or (counter%2!=0 and yy%2!=0):
                pygame.draw.rect(w, (12, 15, 40), (y * widthBlock, x * widthBlock, widthBlock, widthBlock))
            else:
                pygame.draw.rect(w, (5, 8,15), (y * widthBlock, x * widthBlock, widthBlock, widthBlock))
            counter+=1

        keypress = pygame.key.get_pressed()
        if click==1:
            yy = Mouse_Loc[1] // widthBlock
            counter = Mouse_Loc[0] // widthBlock % xGrid
            if counter>=xGrid or yy>=yGrid:
                pr=5
            if pr==0 :

                if (counter!=yGhost or yy!=xGhost):
                    Current_Grid[yy][counter] = -2
            elif pr==1 and Current_Grid[yy][counter] == -2 :
                Current_Grid[yy][counter] = 9999
        if pr==2:
            yy = Mouse_Loc[1] // widthBlock
            counter = Mouse_Loc[0] // widthBlock % xGrid
            if(Current_Grid[yy][counter]!=-2 and Current_Grid[yy][counter]!=0):
                Current_Grid[yPlayer][xPlayer] = 9999
                yPlayer = yy
                xPlayer =  counter
                Current_Grid[yPlayer][xPlayer] = valPlayer
        if pr == 3:
            yy = Mouse_Loc[1] // widthBlock  *pv
            counter = Mouse_Loc[0] // widthBlock % xGrid *pv
            if (Current_Grid[yy][counter] != -2 and Current_Grid[yy][counter] != valPlayer):
                Current_Grid[yGhost][xGhost] = 9999
                yGhost = yy
                xGhost = counter
                Current_Grid[yGhost][xGhost] = 0
        if ticker==0:
            mov3Ghost=1
        else:
            mov3Ghost=0
        if movePlayer==1and tic==0and Current_Grid[yPlayer + 1][xPlayer] != -2 and Current_Grid[yPlayer + 1][xPlayer] != 0 and Current_Grid[yPlayer + 1][xPlayer] != -1 :
            tic=15
            Current_Grid[yPlayer][xPlayer] = 9999
            yPlayer += 1
            Current_Grid[yPlayer][xPlayer] = valPlayer
        elif movePlayer==2 and tic==0and Current_Grid[yPlayer - 1][xPlayer] != -2 and Current_Grid[yPlayer - 1][xPlayer] != 0 and Current_Grid[yPlayer - 1][xPlayer] != -1:
            Current_Grid[yPlayer][xPlayer] = 9999
            yPlayer -= 1
            tic = 15
            Current_Grid[yPlayer][xPlayer] = valPlayer
        elif movePlayer==3  and tic==0 and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != -2 and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != 0 and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != -1:
            Current_Grid[yPlayer][xPlayer] = 9999
            xPlayer = (xPlayer+1)% xGrid
            tic = 15
            Current_Grid[yPlayer][xPlayer% xGrid] = valPlayer
        elif movePlayer==4  and tic==0 and xPlayer!=0 and Current_Grid[yPlayer][xPlayer - 1] != -2 and Current_Grid[yPlayer][xPlayer - 1] != 0and Current_Grid[yPlayer][xPlayer - 1] != -1:
            Current_Grid[yPlayer][xPlayer] = 9999
            xPlayer -= 1
            tic = 15
            Current_Grid[yPlayer][xPlayer] = valPlayer
        elif movePlayer==4  and tic==0 and xPlayer==0 and  Current_Grid[yPlayer][xGrid - 1] != -2  and  Current_Grid[yPlayer][xGrid - 1] != 0 and  Current_Grid[yPlayer][xGrid - 1] != -1:
            Current_Grid[yPlayer][xPlayer] = 9999
            xPlayer = xGrid - 1
            tic = 15
            Current_Grid[yPlayer][xPlayer] = valPlayer





        for event in pygame.event.get():

            if keypress[pygame.K_q]:
                pr=1
                click=1
                
            elif keypress[pygame.K_e]:
                pr=0
                click=1
                
            elif keypress[pygame.K_t]:
                pr=2
                ticker=1
                
            elif keypress[pygame.K_r]:
                pr=3
                
            elif keypress[pygame.K_SPACE] :
                mov3Ghost=1
                
            else:
            
                click=0
                pr=0
                mov3Ghost=0
                
            if keypress[pygame.K_s]  and Current_Grid[yPlayer + 1][xPlayer] != -2 and Current_Grid[yPlayer + 1][xPlayer] != 0  and Current_Grid[yPlayer + 1][xPlayer] != -1  :
                movePlayer=1
            elif keypress[pygame.K_w] and Current_Grid[yPlayer - 1][xPlayer] != -2 and Current_Grid[yPlayer - 1][xPlayer] != 0 and Current_Grid[yPlayer - 1][xPlayer] != -1:
                movePlayer=2
            elif keypress[pygame.K_d] and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != -2 and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != 0  and Current_Grid[yPlayer][(xPlayer  + 1)% xGrid] != -1:
                movePlayer=3
            elif keypress[pygame.K_a] and Current_Grid[yPlayer][xPlayer - 1] != -2 and Current_Grid[yPlayer][xPlayer - 1] != 0 and Current_Grid[yPlayer][xPlayer - 1] != -1:
                movePlayer=4
            else:
                movePlayer=0

            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = False
        path(mov3Ghost)
        pygame.display.update()

main()
print(Current_Grid)
pygame.quit()

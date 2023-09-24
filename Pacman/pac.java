import java.lang.Thread;
import java.lang.Math;
import java.awt.event.*;
import javax.swing.*;

public class pac extends JFrame implements KeyListener {

    int xGrid = 19;
    int yGrid = 25;
    int valPlayer = 9000;
    int valGhost = 0;
    int caught = 0;
	int keyInp=0;
	int timer=0;
	int points=0;
	int ghostClock=20;
	int playerClock=12;
	int pgLoc[] = new int[4];
    int[][] Grid = {{-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}, {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9000, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, {-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2}, {-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2}, {-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2}, {-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2}, {-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2}, {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, {-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2}, {9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 0, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999}, {-2, -2, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2}, {9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, {9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, {9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, {-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2}, {9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999}, {-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2}, {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, {-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2}, {-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2}, {-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2}, {-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2}, {-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2}, {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, {-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}};
    int[][] pGrid={
    {-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2},
{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9000, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, 
{-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2},
{-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2},
{-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2},
{-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2},
{-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2},
{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2},
{0,0,0, -2, 9999, -2, 9999, 9999, 0, 9999, 9999, 9999, 9999, -2, 9999, -2, 0,0,0},
{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, 0, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2},
{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 0,0,0, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 0,0,0, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 0,0,0, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2},
{0,0,0, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 0,0,0},
{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2},
{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
{-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2}, 
{-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2},
{-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2},
{-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2},
{-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2},
{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
{-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}};
    String go(int j)
    {   String s=" ";
    	switch(j)
    	{
    	case 5:
    	s+="G";
    	break;
    	case 6:
    	s+="A";
    	break;
    	case 7:
    	s+="M";
    	break;
    	case 8:
    	s+="E";
    	break;
    	case 9:
    	s+=" ";
    	break;
    	case 10:
    	s+="O";
    	break;
    	case 11:
    	s+="V";
    	break;
    	case 12:
    	s+="E";
    	break;
    	case 13:
    	s+="R";
    	break;
    	
    	}
    	return(s);
    
    }
    String go2(int j)
    {   String s=" ";
    	switch(j)
    	{
    	case 5:
    	s+="Y";
    	break;
    	case 6:
    	s+="O";
    	break;
    	case 7:
    	s+="U";
    	break;
    	case 8:
    	s+=" ";
    	break;
    	case 9:
    	s+="W";
    	break;
    	case 10:
    	s+="O";
    	break;
    	case 11:
    	s+="N";
    	break;
    	
    	}
    	return(s);
    
    }
    

    int[] printer(int printx){

        int pgLoc[] = new int[4];

        for (int i = 0; i < yGrid; i++) {

            for (int j = 0; j < xGrid; j++) {
                String s = "██";

                if (pGrid[i][j] != -2 && pGrid[i][j] != 9999)
                    s = "  ";
                else if (pGrid[i][j] != -2 && pGrid[i][j] != 0)
                    s = " *";

                if (Grid[i][j] == valPlayer) {
                    s = "▓▓";
                    pgLoc[0] = i;
                    pgLoc[1] = j;

                } else if (Grid[i][j] == valGhost) {
                    s = "[]";
                    pgLoc[2] = i;
                    pgLoc[3] = j;
                }
                if(j>4 && j<14 && caught==1 &&points<230 && i==12)
                s=go(j);
                if(j>5 && j<13 && points==230 && i==12)
                {s=go2(j-1);
                caught=1;}

                if (printx == 1)
                    print(s);
                if (printx==1 && i==12 && j==xGrid-1)
                print(" Score: "+points);
            }

            if (printx == 1) {
                println("");
            }
        }
        return (pgLoc);
    }
	
	void reTrace(int dist)
	{
		if (dist==0)
			caught=1;
		
		
		int x=pgLoc[1];
		int y=pgLoc[0];
		int yGhost=pgLoc[2];
		int xGhost=pgLoc[3];
		while(dist>0 && timer%ghostClock==0)
		{
			if (Grid[y][(xGrid+x - 1)%xGrid] == dist)
				x = (xGrid+x - 1)%xGrid;			
			
			else if (Grid[(yGrid+y - 1)%yGrid][x] == dist)
				y = (yGrid+y - 1)%yGrid;
			
			else if (Grid[y][(x + 1) % xGrid] == dist)
				x = (x + 1) % xGrid;
			
			else if (Grid[(y + 1) % yGrid][x] == dist)
				y = (y + 1) % yGrid;
			
			if (dist <2   && ((Math.abs(yGhost - y) + 1) % xGrid < 3 && (Math.abs(xGhost - x) + 1) % xGrid < 3))
			{
				Grid[yGhost][xGhost] = 9999;
				yGhost = y;
				xGhost = x;
				Grid[yGhost][xGhost] = valGhost;
				
			}
			
			else
				Grid[y][x] = 9999;
			
			dist-=1;
		}
	}
	
	void pathFinder()
	{
		boolean run = true;
		
		int dist=0;
		int found=0;
		int y=pgLoc[0];
		int x=pgLoc[1];
		while(run)
		{
			int counter = 0;
			while (counter < (xGrid * yGrid)) 	 	 
			{
				int y2 = (counter / xGrid);
				int x2 = counter % xGrid;
				counter += 1;
				
				if (Grid[y2][x2] == dist)
				{
					if (x2 > 0 && Grid[y2][x2 - 1] > dist)
					{						
                        if (Grid[y2][x2 - 1] == valPlayer)
						{						
                            run = false;
                            found = 1;
						}
                        else
                            Grid[y2][x2 - 1] = dist + 1;
                    }
					
                    if( y2 > 0 && Grid[y2 - 1][x2] > dist)
					{
                        if (Grid[y2 - 1][x2] == valPlayer)
						{
                            run = false;
                            found = 1;
						}
                        else
                            Grid[y2 - 1][x2] = dist + 1;
                    }
					
                    if (Grid[y2][(x2 + 1) % xGrid] > dist)
					{
                        if (Grid[y2][(x2 + 1) % xGrid] == valPlayer)
						{
                            run = false;
                            found = 1;
						}
                        else
                            Grid[y2][(x2 + 1) % xGrid] = dist + 1 ;
					}

                    if( y2 < yGrid - 1 && Grid[y2 + 1][x2] > dist)
					{
                        if( Grid[y2 + 1][x2] == valPlayer)
						{
                            run = false;
                            found = 1;
						}
                        else
                            Grid[y2 + 1][x2] = dist + 1;
                    }
				}
			}

			dist+=1;
			if (dist>300)
				break;
		}
		
		
		if(found==1)
			reTrace(dist-1);
		
	}
	
	void println(String s)
	{
		System.out.println(s);
	}
	void print(String s)
	{
		System.out.print(s);
	}
	
	void reset()
	{
		
		for(int i=0;i<25;i++)
		{
	
			for(int j=0;j<19;j++)
			{
				if(Grid[i][j]>0 && Grid[i][j]!=valPlayer)
					Grid[i][j]=9999;
			}
		}
	}
	
	void playerMovement()
	{
		
		switch(keyInp)
		{
			case 65:
			if(Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]!=-2 && Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]!=valGhost && timer%playerClock==0)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]==9999)
				{
				pGrid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]=0;
				points+=1;
				}
				Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]=valPlayer;				 
			}
			break;
			
			case 87:
			if(Grid[pgLoc[0]-1][pgLoc[1]]!=-2 && Grid[pgLoc[0]-1][pgLoc[1]]!=valGhost && timer%playerClock==0)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]-1][pgLoc[1]]==9999)
				{
				pGrid[pgLoc[0]-1][pgLoc[1]]=0;
				points+=1;
				}
				Grid[pgLoc[0]-1][pgLoc[1]]=valPlayer;				 
			}
			break;
			
			case 68:
			if(Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]!=-2 && Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]!=valGhost && timer%playerClock==0)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]][(pgLoc[1]+1)%xGrid]==9999)
				{
				pGrid[pgLoc[0]][(pgLoc[1]+1)%xGrid]=0;
				points+=1;
				}
				Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]=valPlayer;
			}
			break;
			
			case 83:
			if(Grid[pgLoc[0]+1][pgLoc[1]]!=-2 && Grid[pgLoc[0]+1][pgLoc[1]]!=valGhost && timer%playerClock==0)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]+1][pgLoc[1]]==9999)
				{
				pGrid[pgLoc[0]+1][pgLoc[1]]=0;
				points+=1;
				}
				Grid[pgLoc[0]+1][pgLoc[1]]=valPlayer;
			 
			}
		}
		
	}


    void gameLogic() throws InterruptedException
	{
		print("");
		System.out.println("\033[H\033[2J");
        while (caught==0) {
			
			reset();
			ghostClock=20 - points/50;
			playerClock=12- points/50;
			pgLoc = printer(0);
			System.out.println("\033[H");
			playerMovement();
			pathFinder();
			if (timer<60)
				timer+=1;
			else
				timer=1;
			pgLoc = printer(1);
			Thread.sleep(15);
			
        }
		System.out.println("\033[H\033[2J");
		pgLoc=printer(1);
    }
	
	pac()  throws InterruptedException
	{
		this.setVisible(true) ;
		this.addKeyListener(this);
		gameLogic();	
		dispose();
	}
	
	public static void main(String args[])  throws InterruptedException
	{
		new pac();
		
		
	}
	
	@Override
	public void keyTyped(KeyEvent e) 
	{
	
	}
	@Override
	public void keyPressed(KeyEvent e) 
	{
		keyInp=e.getKeyCode();	
		//print("" +keyInp);	
	}
	@Override
	public void keyReleased(KeyEvent e) 
	{
	
	}
}


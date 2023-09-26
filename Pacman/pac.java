import java.lang.Thread;
import java.lang.Math;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;


public class pac extends JFrame implements KeyListener 
{
    Random rand = new Random();
    int xGrid = 19;
    int yGrid = 25;
    int valPlayer = 9000;
    int valGhost = 0;
    int caught;
	int keyInp;
	int timer;
	int points;
	int blink;
	int total;
	int[][] Grid=new int[yGrid][xGrid];
    int[][] pGrid=new int[yGrid][xGrid];
	int map;//=rand.nextInt(2) +1;
	int movement;
	int gClock;
	int pClock;
	int ghostClock;
	int playerClock;
	int score;
	int bonus;
	int pgLoc[] = new int[4];
	void varInit()
	{
	    caught = 0;
		keyInp=0;
		timer=0;
		points=0;
		blink=0;
		total=999;
		map=rand.nextInt(2) +1;
		movement=0;
		gClock=18;
		pClock=12;
		ghostClock=20;
		playerClock=12;
		score=0;
		bonus=1;
	}
	int[] pInit()
	{
		
		int p[]={rand.nextInt(yGrid),rand.nextInt(xGrid)};		
		if(Grid[p[0]][p[1]]==9999 && (p[0]<9||p[1]<6||(p[1]>12)||p[0]>14))
		{
			Grid[pgLoc[0]][pgLoc[1]]=Grid[p[0]][p[1]];
			Grid[p[0]][p[1]]=valPlayer;
		}
		else
			p=pInit();
		
		return(p);

		
	}    

    int[] printer(int printx)
    {
    	if (printx == 1) 
            {
                print("\033[35C");
            }

        int pgLoc[] = new int[4];
        for (int i = 0; i < yGrid; i++) 
        {
            for (int j = 0; j < xGrid; j++) 
            {
                String s = "\033[0;39m██";

                if (pGrid[i][j] != -2 && pGrid[i][j] != 9999)
                    s = "\033[0;39m  ";

                else if (pGrid[i][j] != -2 && pGrid[i][j] != 0)
                    s = "\033[1;36m *";

                if (Grid[i][j] == valPlayer) 
                {
                    s = "\033[1;"+(32+blink)+"m██";
                    pgLoc[0] = i;
                    pgLoc[1] = j;
                } 
                else if (Grid[i][j] == valGhost) 
                {                    
                    s = "\033[1;31m██";
                    pgLoc[2] = i;
                    pgLoc[3] = j;
                }

                if(j>4 && j<14 && caught==1 &&points<total && i==12)
                	s=go(j);

                if(j>5 && j<13 && points==total && i==12)
                {	s=go2(j-1);
                	caught=1;
            	}

            	if(j>3&& j<15 && caught==1 && i==13)
                	s=go3(j+1);

                if (printx == 1)
                    print(s);

                if (printx==1 && i==12 && j==xGrid-1)
                	print("\033[0;39m Score: "+score);
            }

            if (printx == 1) 
            {
                print("\n\033[35C");
            }
        }
        return (pgLoc);
    }
    void mainMenu() throws InterruptedException
    {
    	System.out.print("\033[H\033[2J");

    	while(keyInp!=10)
    		{
    			timer=(timer+1)%2;
    			mainM();
    			Thread.sleep(333);
    			System.out.print("\033[H");
    		}
    	keyInp=0;

    }

    void mainM()
    {
    	print("\033[35C");
    	int y=0;
    	int x=0;
            
        for (int i = 0; i < yGrid; i++) 
        {	x=0;
            for (int j = 0; j < xGrid; j++) 
            { x+=1;
                String s ="\033[1;"+(32+(x+y+timer)%2)+"m██";;

                if (title[i][j] != -2)
                    s = "\033[0;39m  ";   
                if(j>3 && j<15 && i==22)
                	s=gos(j+1);             
                print(s);
            }
            y+=1;
			print("\n\033[35C");            
        }
        
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
	{	blink=(blink+1)%2;	
		switch(keyInp)
		{
			case 65:
			if(Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]!=-2 && Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]!=valGhost )
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]==9999)
				{
				pGrid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]=0;
				points+=1;
				score+=(bonus*10);
				}
				Grid[pgLoc[0]][(xGrid+pgLoc[1]-1)%xGrid]=valPlayer;		
				movement=1;		 
			}
			break;
			
			case 87:
			if(Grid[pgLoc[0]-1][pgLoc[1]]!=-2 && Grid[pgLoc[0]-1][pgLoc[1]]!=valGhost)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]-1][pgLoc[1]]==9999)
				{
				pGrid[pgLoc[0]-1][pgLoc[1]]=0;
				points+=1;
				score+=(bonus*10);
				}
				Grid[pgLoc[0]-1][pgLoc[1]]=valPlayer;	
				movement=1;			 
			}
			break;
			
			case 68:
			if(Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]!=-2 && Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]!=valGhost)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]][(pgLoc[1]+1)%xGrid]==9999)
				{
				pGrid[pgLoc[0]][(pgLoc[1]+1)%xGrid]=0;
				points+=1;
				score+=(bonus*10);
				}
				Grid[pgLoc[0]][(pgLoc[1]+1)%xGrid]=valPlayer;
				movement=1;
			}
			break;
			
			case 83:
			if(Grid[pgLoc[0]+1][pgLoc[1]]!=-2 && Grid[pgLoc[0]+1][pgLoc[1]]!=valGhost)
			{
				Grid[pgLoc[0]][pgLoc[1]]=9999;
				if (pGrid[pgLoc[0]+1][pgLoc[1]]==9999)
				{
				pGrid[pgLoc[0]+1][pgLoc[1]]=0;
				points+=1;
				score+=(bonus*10);
				
				}
				Grid[pgLoc[0]+1][pgLoc[1]]=valPlayer;
				movement=1;			 
			}			
		}		
	}


    void gameLogic() throws InterruptedException
	{
		
		int past=0;
		pgLoc = printer(0);
		init();
		pInit();
		pgLoc = printer(0);
		pGrid[pgLoc[0]][pgLoc[1]]=9998;
		total-=1;
		System.out.print("\033[H\033[2J");
        while (caught==0) 
        {			
			reset();
			movement=0;			
			ghostClock=Math.max(gClock - points/40,1);
			playerClock=Math.max(pClock- points/40,1);
			pgLoc = printer(0);
			System.out.print("\033[H");

			if(timer%playerClock==0)
			{
				past=points;
				playerMovement();
				if (past==points && movement==1)
					bonus=1;
				else if(movement==1)
					bonus+=1;
			}
			pathFinder();
			if (timer<60)
				timer+=1;
			else
				timer=1;
			pgLoc = printer(1);
			Thread.sleep(15);			
        }
		System.out.print("\033[H\033[2J");
		pgLoc=printer(1);
		print("\033[0G");
		int run=1;
		
		
	
    }
	
	pac()  throws InterruptedException
	{
		this.setVisible(true) ;
		this.addKeyListener(this);
		varInit();
		mainMenu();
		int run=1;
		while(run==1)
		{	varInit();
			init_map();			
			gameLogic();
			while(run==1)
		{
			//print(keyInp+"");
			if(keyInp==89)
				break;
			else if(keyInp==78)
				run=0;
		}
		}	
		System.out.print("\033[H\033[2J");
		dispose();
	}
	
	public static void main(String args[])  throws InterruptedException
	{
		new pac();
	}
	
	
	public void keyTyped(KeyEvent e) 
	{}
	
	public void keyPressed(KeyEvent e) 
	{
		keyInp=e.getKeyCode();
			
	}
	
	public void keyReleased(KeyEvent e) 
	{}
	
	String gos(int j)
    {   String s="\033[1;31m";
    	switch(j)
    	{
    		case 5:
    			s+="PR";
    			break;
    		case 6:
    			s+="ES";
    			break;
    		case 7:
    			s+="S ";
    			break;
    		case 8:
    			s+="EN";
    			break;
    		case 9:
    			s+="TE";
    			break;
    		case 10:
    			s+="R ";
    			break;
    		case 11:
    			s+="TO";
    			break;
    		case 12:
    			s+=" S";
    			break;
    		case 13:
	    		s+="TA";
    			break;	
    		case 14:
	    		s+="RT";
    			break; 
    		case 15:
	    		s+="! ";
    			break;   	
    	}
    	return(s); 	    
    }

    String go(int j)
    {   String s="\033[1;31m ";
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
    {   String s="\033[1;32m ";
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

String go3(int j)
    {   String s="\033[1;33m";
    	switch(j)
    	{
    		case 5:
    			s+="Pl";
    			break;
    		case 6:
    			s+="ay";
    			break;
    		case 7:
    			s+=" A";
    			break;
    		case 8:
    			s+="ga";
    			break;
    		case 9:
    			s+="in";
    			break;
    		case 10:
    			s+="? ";
    			break;
    		case 11:
    			s+="Y:";
    			break;
    		case 12:
    			s+="Ye";
    			break;
    		case 13:
	    		s+="s ";
    			break;	
    		case 14:
	    		s+="N:";
    			break; 
    		case 15:
	    		s+="No";
    			break;   	
    	}
    	return(s); 	    
    }

    void init_map()
	{
		for (int i = 0; i < yGrid; i++) 
        {
            for (int j = 0; j < xGrid; j++) 
            { 
            	if(map==2)
            		Grid[i][j]=map2[i][j];
            	else
            		Grid[i][j]=map1[i][j];
				
			}
		}
	}
	void init()
	{
		total=0;
		for (int i = 0; i < yGrid; i++) 
        {
            for (int j = 0; j < xGrid; j++) 
            { pGrid[i][j]=Grid[i][j];
				if(pGrid[i][j]==9999)
					total+=1;
			}
		}
	}
	
    int[][] map2={
   	 {9998, 9998, 9998, 9998, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 9998, 9998, 9998, 9998},
     {9998,9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, 9998}, 
     {9998, 9998, 9998, 9998, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, 9998, 9998, 9998, 9998}, 
     {9998, 9998, 9998, 9998, -2, 9999, -2, 9999, 9999, -2, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998, 9998},
     {-2, -2, -2, -2, -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2, -2, -2, -2, -2},
     {9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999},
     {-2, -2, 9999, -2, -2, -2, -2, 9999, -2, -2, -2, 9999, -2, -2, -2, -2, 9999, -2, -2}, 
     {-2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2},
     {-2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2}, 
     {-2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2},
     {-2, -2, -2, 9999, -2, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, -2, 9999, -2, -2, -2},
     {9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
     {-2, -2, 9999, -2, -2, -2, 9999, -2, 9998, 0, 9998, -2, 9999, -2, -2, -2, 9999, -2, -2}, 
     {9998, -2, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, -2, 9998}, 
     {9998, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, 9998}, 
     {9998, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, 9998},
     {-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2},
     {9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999},
     {-2, -2, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, -2, -2},
     {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, 
     {-2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2}, 
     {-2, 9999, -2, 9999, -2, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, -2, 9999, -2, 9999, -2},
     {-2, 9999, -2, 9999, -2, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, -2, 9999, -2, 9999, -2}		,
     {-2, 9999, 9999, 9999, -2,9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, -2, 9999, 9999, 9999, -2},
     {-2, -2, -2, -2, -2, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, 9998, -2, -2, -2, -2, -2}};

	int[][] map1={{-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}, 
	{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9000, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, 
	{-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2},
	{-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2},
	{-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2}, 
	{-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2},
	{-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2}, 
	{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2}, 
	{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2}, 
	{9998, 9998, 9998, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998}, 
	{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2}, 
	{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 0, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	{9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2}, 
	{9998, 9998, 9998, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998}, 
	{-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2}, 
	{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
	{-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2},
	{-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2},
	{-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2},
	{-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2}, 
	{-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2}, 
	{-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
	{-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}};

	int[][] title= {{9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	 {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	 {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	  {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	  {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	       {9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999}, 
	       {9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999},
	        {9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999}, 
	        {9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999}, 
	        {9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999},
	         {9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999}, 
	         {9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999}, 
	         {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	         {9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999},
	          {9999, -2, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999},
	           {9999, -2, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999},
	            {9999, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, 9999, 9999, -2, 9999}, 
	            {9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999}, 
	            {9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999}, 
	            {9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9998, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999},
	   {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999}, 
	   {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	    {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	     {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999},
	      {9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999}};
	
	
}


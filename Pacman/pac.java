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
    int[][] Grid = {{-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2},
            {-2, 10, 11, 12, 11, 10, 9, 8, 7, 9000, 8, 9, 10, 11, 12, 13, 12, 11, -2}, {-2, 9, -2, -2, -2, -2, -2, -2, 6, -2, 7, -2, -2, -2, -2, -2, -2, 10, -2},
            {-2, 8, 7, 6, 5, -2, 3, 4, 5, -2, 6, 5, 4, -2, 6, 7, 8, 9, -2}, {-2, -2, 8, -2, 4, -2, 2, -2, -2, -2, -2, -2, 3, -2, 5, -2, 9, -2, -2},
            {-2, 7, 8, -2, 3, 2, 1, 1, 1, 1, 1, 1, 2, 3, 4, -2, 8, 7, -2}, {-2, 6, -2, -2, 3, -2, -2, -2, 1, -2, 2, -2, -2, -2, 3, -2, -2, 6, -2},
            {-2, 5, 4, 3, 2, 1, 1, 1, 1, -2, 3, 4, 5, 5, 4, 3, 4, 5, -2}, {-2, -2, -2, -2, 3, -2, 1, -2, -2, -2, -2, -2, 4, -2, 3, -2, -2, -2, -2},
            {9999, 9999, 9999, -2, 4, -2, 1, 1, 1, 1, 1, 2, 3, -2, 4, -2, 9999, 9999, 9999},
            {-2, -2, -2, -2, 5, -2, 1, -2, -2, 1, -2, -2, 4, -2, 5, -2, -2, -2, -2, -2}, {8, 7, 6, 5, 4, 3, 2, -2, 1, 1, 1, -2, 5, 4, 4, 5, 6, 7, 8},
            {9, 8, 7, 6, 5, 4, 3, -2, 1, 1, 1, -2, 4, 3, 4, 5, 6, 7, 8}, {9, 9, 8, 7, 6, 5, 4, -2, 1, 7, 0, -2, 3, 3, 4, 5, 6, 7, 8},
            {-2, -2, -2, -2, 7, -2, 5, -2, -2, -2, -2, -2, 2, -2, 5, -2, -2, -2, -2, -2},
            {9999, 9999, 9999, -2, 8, -2, 5, 6, 5, 4, 3, 2, 3, -2, 6, -2, 9999, 9999, 9999},
            {-2, -2, -2, -2, 9, -2, 6, -2, -2, -2, -2, -2, 4, -2, 7, -2, -2, -2, -2}, {-2, 12, 11, 10, 9, 8, 7, 8, 9, -2, 7, 6, 5, 6, 7, 8, 9, 10, -2},
            {-2, 13, -2, -2, 10, -2, -2, -2, 10, -2, 8, -2, -2, -2, 8, -2, -2, 11, -2},
            {-2, 14, 15, -2, 11, 12, 13, 12, 11, 10, 9, 10, 11, 10, 9, -2, 13, 12, -2},
            {-2, -2, 9999, -2, 12, -2, 14, -2, -2, -2, -2, -2, 12, -2, 10, -2, 14, -2, -2},
            {-2, 9999, 15, 14, 13, -2, 15, 9999, 9999, -2, 15, 14, 13, -2, 11, 12, 13, 14, -2},
            {-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 15, -2},
            {-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2},
            {-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2}
    };

    int[] printer(int printx) throws InterruptedException {

        int arx[] = new int[4];

        for (int i = 0; i < yGrid; i++) {

            for (int j = 0; j < xGrid; j++) {
                String s = "██";

                if (Grid[i][j] != -2 && Grid[i][j] != valPlayer && Grid[i][j] != valGhost)
                    s = "  ";

                if (Grid[i][j] == valPlayer) {
                    s = "▓▓";
                    arx[0] = i;
                    arx[1] = j;

                } else if (Grid[i][j] == valGhost) {
                    s = "[]";
                    arx[2] = i;
                    arx[3] = j;
                }

                if (printx == 1)
                    System.out.print(s);
            }

            if (printx == 1) {
                System.out.print("\n");
            }
        }
        return (arx);
    }
	
	void reTrace(int dist, int arx[],int nx) throws InterruptedException
	{
		if (dist==0)
			caught=1;
		
		
		int x=arx[1];
		int y=arx[0];
		int yGhost=arx[2];
		int xGhost=arx[3];
		while(dist>0)
		{
			if ( x> 0 && Grid[y][x - 1] == dist)
					x -= 1;
				
			else if (x == 0 && Grid[y][xGrid - 1] == dist)
				x = xGrid - 1;
			
			else if (y > 0 && Grid[y - 1][x] == dist)
				y -= 1;
			
			else if (y == 0 && Grid[yGrid - 1][x] == dist)
				y = yGrid - 1;
			
			else if (x < xGrid && Grid[y][(x + 1) % xGrid] == dist)
				x = (x + 1) % xGrid;
			
			else if (y < yGrid - 1 && Grid[(y + 1) % yGrid][x] == dist)
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
	
	void pathFinder(int arx[],int nx)  throws InterruptedException
	{
		boolean run = true;
		
		int dist=0;
		int found=0;
		int y=arx[0];
		int x=arx[1];
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
			reTrace( dist-1,arx,nx);
		
	}
	
	void print(String s)
	{
		System.out.println(s);
	}
	public void reset()
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


    void gameLogic() throws InterruptedException {
		print("");
		System.out.println("\033[H\033[2J");
        int arx[] = new int[4];
        while (caught==0) {
			reset();
			arx = printer(0);
			Thread.sleep(100);
			System.out.println("\033[H");
			pathFinder(arx,1);
			arx = printer(1);
			
        }
		System.out.println("\033[H\033[2J");
		arx=printer(1);
    }
	pac() throws InterruptedException
	{
		this.setVisible(true) ;
		this.addKeyListener(this);
		gameLogic();
		
		
	}
	
	public static void main(String args[]) throws InterruptedException
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


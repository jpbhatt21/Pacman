import java.io.*;

public class pacman
{
	
	  static int xGrid=19;
	  static int yGrid=25;
	  static int valPlayer=9000;
	  static int valGhost=0;
	  static int caught=0;
	 static int[][] Grid={{-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2},
        {-2,10,11,12,11,10,9,8,7,9000,8,9,10,11,12,13,12,11,-2},{-2,9,-2,-2,-2,-2,-2,-2,6,-2,7,-2,-2,-2,-2,-2,-2,10,-2},
        {-2,8,7,6,5,-2,3,4,5,-2,6,5,4,-2,6,7,8,9,-2},{-2,-2,8,-2,4,-2,2,-2,-2,-2,-2,-2,3,-2,5,-2,9,-2,-2},
        {-2,7,8,-2,3,2,1,1,1,1,1,1,2,3,4,-2,8,7,-2},{-2,6,-2,-2,3,-2,-2,-2,1,-2,2,-2,-2,-2,3,-2,-2,6,-2},
        {-2,5,4,3,2,1,1,1,1,-2,3,4,5,5,4,3,4,5,-2},{-2,-2,-2,-2,3,-2,1,-2,-2,-2,-2,-2,4,-2,3,-2,-2,-2,-2},
        {9999,9999,9999,-2,4,-2,1,1,1,1,1,2,3,-2,4,-2,9999,9999,9999},
        {-2,-2,-2,-2,5,-2,1,-2,-2,1,-2,-2,4,-2,5,-2,-2,-2,-2,-2},{8,7,6,5,4,3,2,-2,1,1,1,-2,5,4,4,5,6,7,8},
        {9,8,7,6,5,4,3,-2,1,1,1,-2,4,3,4,5,6,7,8},{9,9,8,7,6,5,4,-2,1,7,0,-2,3,3,4,5,6,7,8},
        {-2,-2,-2,-2,7,-2,5,-2,-2,-2,-2,-2,2,-2,5,-2,-2,-2,-2,-2},
        {9999,9999,9999,-2,8,-2,5,6,5,4,3,2,3,-2,6,-2,9999,9999,9999},
        {-2,-2,-2,-2,9,-2,6,-2,-2,-2,-2,-2,4,-2,7,-2,-2,-2,-2},{-2,12,11,10,9,8,7,8,9,-2,7,6,5,6,7,8,9,10,-2},
        {-2,13,-2,-2,10,-2,-2,-2,10,-2,8,-2,-2,-2,8,-2,-2,11,-2},
        {-2,14,15,-2,11,12,13,12,11,10,9,10,11,10,9,-2,13,12,-2},
        {-2,-2,9999,-2,12,-2,14,-2,-2,-2,-2,-2,12,-2,10,-2,14,-2,-2},
        {-2,9999,15,14,13,-2,15,9999,9999,-2,15,14,13,-2,11,12,13,14,-2},
        {-2,9999,-2,-2,-2,-2,-2,-2,9999,-2,9999,-2,-2,-2,-2,-2,-2,15,-2},
        {-2,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,-2},
        {-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2}};

	static int[] printer(int printx)
	{
	
		int arx[]=new int[4];

		for(int i=0;i<yGrid;i++)
		{
	
			for(int j=0;j<xGrid;j++)
			{
				String s= "██";
				
				if (Grid[i][j]!=-2 && Grid[i][j]!=valPlayer && Grid[i][j]!=valGhost )
					s="  ";
				
				if (Grid[i][j]==valPlayer)
				{
					s="▓▓";
					arx[0]=i;
					arx[1]=j;
					
				}
					
				else if (Grid[i][j]==valGhost)
				{
					s="[]";
					arx[2]=i;
					arx[3]=j;
				}
					
				if (printx==1)
					System.out.print(s);
			}
				
				if (printx==1)
				{
				System.out.print("\n"); 
				}
		}
		return(arx);
	}
	
	
	public static void main(String args[]) 
	{		
		int arx[]=new int[4];
		while(true)
		{
			System.out.println("\033[H\033[2J");
			arx=printer(1) ;
		}
		
	}
}


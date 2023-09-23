import java.io.*;

public class test 
{
	
	  static int xGrid=19;
	  static int yGrid=25;
	  static int valPlayer=9000;
	  static int valGhost=0;
	  static int caught=0;
	 static int[][] Grid=new int[yGrid][xGrid];
	  
	  static void init()
	  {
		  
		  for(int i=0;i<yGrid;i++)
		{
			for(int j=0;j<xGrid;j++)
			{
				Grid[i][j]=9999;
			}
		}
		Grid[0][0]=valPlayer;
		Grid[yGrid-1][xGrid-1]=valGhost;
		Grid[(yGrid-1)/2][(xGrid-1)/2]=-2;
	  }
	  
	  


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
		init();
		
		int arx[]=new int[4];
		while(true)
		{
			System.out.println("\033[H\033[2J");
			arx=printer(1) ;
		}
		
		
	}
}


package robSoccer

class Direction {

	int dir_x;
	int dir_y;
	
	Direction(int x, int y)
	{
		dir_x=x;
		dir_y=y;
	}
	
	void setDirection(int x, int y)
	{
		this.dir_x=x;
		this.dir_y=y;
	}
	
	Direction getDirection(int x, int y)
	{
		this.dir_x=x;
		this.dir_y=y;
	}
}

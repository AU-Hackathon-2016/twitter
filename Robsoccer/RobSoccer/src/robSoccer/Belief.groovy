package robSoccer

class Belief {

	Location location;
	Direction direction;
	int speed;
	
	Belief(Location loc, Direction dir, int speed)
	{
		this.location =loc;
		this.direction = dir;
		this.speed = speed;
	}
	
	Belief getBelief()
	{
		return this;
	}
	
	
	void setBelief(Location loc, Direction dir, int speed)
	{
		this.location =loc;
		this.direction = dir;
		this.speed = speed;
	}	
	
}

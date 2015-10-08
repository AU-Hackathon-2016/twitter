package robSoccer

class Ball implements Agent {

	Belief belief;
	
	Ball(Belief bef)
	{
		this.belief=bef;
	}
	
	void setBelief(Belief bef)
	{
		this.belief=bef;
	}
	
	Belief getBelief()
	{
		return this.belief;
	}
	
}

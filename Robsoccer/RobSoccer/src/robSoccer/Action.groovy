package robSoccer

class Action {
	
	 String actionDescription;
	
	Action(String actionDes)
	{
		this.actionDescription=actionDes;
	}
	
	Belief updateBelief(Agent agent,Belief b)
	{
		agent.setBelief(b);
		
	}
	
}

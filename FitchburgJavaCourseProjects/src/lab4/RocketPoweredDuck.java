package lab4;
/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */

public class RocketPoweredDuck extends Duck {
    
    
    public RocketPoweredDuck() {
    	setFlyBehavior(new FlyRocketPowered());
		setQuackBehavior(new WhooshQuack());

		
	}
    public void display() {
		System.out.println("I'm a Rocket Powered duck");
	}
    
}
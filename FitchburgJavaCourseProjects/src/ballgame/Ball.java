package ballgame;
/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */

import java.awt.Color;
import java.awt.Graphics;

public class Ball {
	//declaring parameters.
	public int size;
	public int xIncrement;
	public int yIncrement;
	public int xPosition;
	public int yPosition;
	
	
	
	public Ball( int size, int increment ){
		this.size = size;
		this.xIncrement = increment;
		this.yIncrement = increment;
		xPosition = 100;
		yPosition = 100;
	}
//getters
	public int getxIncrement() {
		return xIncrement;
	}
	
	public int getyIncrement() {
		return yIncrement;
	}
	
	//position getters
	public int getTop() {
		return yPosition;
	}

	public int getBottom() {
		return yPosition + size;
	}

	public int getLeft() {
		return xPosition;
	}

	public int getRight() {
		return xPosition + size;
	}
	
	//Reversing horizontal direction
	public void reverseDirectionX() {
		xIncrement *= -1;
	}

	//Reversing vertical direction
	public void reverseDirectionY() {
		yIncrement *= -1;
	}

	//Returns horizontal center
	public int getHorizontalCenter() {
		return getLeft() + (size / 2);
	}

	//Returns vertical center
	public int getVerticalCenter() {
		return getTop() + (size / 2);
	}

	public void draw(Graphics graphics) {
		graphics.setColor(Color.RED);	//Color of the ball
		graphics.fillOval(xPosition, yPosition, size, size);	//Drawing the ball
	}
	
	public void changePosition() {
		changeDirection(Display.length, Display.height);
		//Changing the position
		xPosition += xIncrement;
		yPosition += yIncrement;
	}
	
	//Detecting the contact with window walls
	public void changeDirection(int length, int height) {
		if (getLeft() <= 0 || getRight() >= length)
			reverseDirectionX();	//Changing horizontal direction
		else if (getTop() <= 0 || getBottom() >= height)
			reverseDirectionY();	//Changing vertical direction
	}
}

		

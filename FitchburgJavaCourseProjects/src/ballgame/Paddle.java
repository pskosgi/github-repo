package ballgame;
/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */

import java.awt.Color;
import java.awt.Graphics;

public class Paddle {
	// Declaring Properties
	private int length; 
	private int height; 
	private int xPosition;
	private int yPosition;

	public Paddle(int length, int height, int xPosition, int yPosition) {
		this.length = length;
		this.height = height;
		this.xPosition = xPosition;
		this.yPosition = yPosition;
	}

	// Position getters
	public int getTop() {
		return yPosition - (height / 2);
	}

	public int getBottom() {
		return yPosition + (height / 2);
	}

	public int getLeft() {
		return xPosition - (length / 2);
	}

	public int getRight() {
		return xPosition + (length / 2);
	}

	public void draw(Graphics graphics) {
		graphics.setColor(Color.BLUE); // declaring color of the paddle
		graphics.fillRect(getLeft(), getTop(), length, height); // Drawing paddle
	}

	public void changePosition(int x) {
		// Detecting the edge of the window
		if (x - (length / 2) >= 0 && x + (length / 2) <= Display.length)
			xPosition = x; // Changing the position
	}
}

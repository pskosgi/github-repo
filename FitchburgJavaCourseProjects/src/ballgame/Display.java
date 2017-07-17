package ballgame;
/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */

import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class Display extends JPanel {

	private static final long serialVersionUID = 1L;
	public static final int length = 800;
	public static final int height = 400;
	private JFrame frame;
	private Controller controller;

	public Display(Controller controller) {
		this.controller = controller;
		frame = new JFrame("PADDLE BALL GAME");
		setSize(length, height);
		frame.setSize(length + 20, height + 40);
		frame.add(this); // Adding game window to frame
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}

	@Override
	protected void paintComponent(Graphics graphics) {
		super.paintComponent(graphics);
		graphics.setColor(Color.BLACK);
		graphics.fillRect(0, 0, getWidth(), getHeight()); // Drawing game window
		controller.draw(graphics);
	}
}

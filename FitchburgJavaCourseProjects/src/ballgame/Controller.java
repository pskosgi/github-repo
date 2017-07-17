	package ballgame;
	/**
	 * @author Prashanthi sudha kosgi
	 * date :06/23/2017.
	 * 
	 */
	import java.awt.Graphics;
	import java.awt.event.ActionEvent;
	import java.awt.event.ActionListener;
	import java.awt.event.MouseEvent;
	import java.awt.event.MouseMotionListener;
	
	import javax.swing.Timer;
	
	public class Controller implements ActionListener, MouseMotionListener {
		// creating references
		private Ball ball;
		private Paddle paddle;
		private Display display;
		private Timer timer;
	
		public Controller() {
			// Instantiating the components
			ball = new Ball(40, 3);
			paddle = new Paddle(100, 12, 300, 30);
			display = new Display(this);
			timer = new Timer(25, this);
			timer.start(); // Starting the Timer for Ball
			display.addMouseMotionListener(this); // Registering the mouse event for paddle
		}
	
		@Override
		public void actionPerformed(ActionEvent actionEvent) {
			// Detecting the contact between paddle and ball
			if (ball.getTop() == paddle.getBottom()
					|| (ball.getTop() < paddle.getBottom() && ball.getTop() >= paddle.getTop()))
				if (ball.getHorizontalCenter() >= paddle.getLeft() && ball.getHorizontalCenter() <= paddle.getRight())
					ball.reverseDirectionY(); // Reversing the ball after contact
			ball.changePosition(); // updating the ball position
			display.repaint(); // repainting the game window
		}
	
		@Override
		public void mouseDragged(MouseEvent mouseDraggedEvent) {
			paddle.changePosition(mouseDraggedEvent.getX()); // repainting the game window
			display.repaint(); // repainting the game window
		}
	
		@Override
		public void mouseMoved(MouseEvent mouseMovedEvent) {
			paddle.changePosition(mouseMovedEvent.getX()); // Updating the paddle position
			display.repaint(); // repainting the game window
		}
	
		public void draw(Graphics graphics) {
			if (ball != null)
				ball.draw(graphics); // Drawing the ball
			if (paddle != null)
				paddle.draw(graphics); // Drawing the paddle
		}
	}

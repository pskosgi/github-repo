package diceroll;

import javax.swing.JOptionPane;
import javax.swing.JTextArea;

/**
 * Program2 for dice
 * @author Prashanthi Sudha Kosgi
 * Date : 6/2/2017
 */
public class Diceroll {
	
	public static void main(String args[]) {
		// Get user input for number of times dice should be rolled.
		String numberOfTimes = JOptionPane.showInputDialog("Please enter the number of times dice should roll");
		int numOfTimesDiceRolled = Integer.parseInt(numberOfTimes);
		// System.out.println("Number of time dice should be rolled: " + numOfTimesDiceRolled);

		int arrRoll[] = new int[13];

		// pass array and number of times dice rolled
		diceFunction(arrRoll, numOfTimesDiceRolled);

		// Display logic
		JTextArea area = new JTextArea();
		String output = "Dice Result \t  No.of times sum rolled";
		for (int i = 2; i < arrRoll.length; i++) {
			output = output + "\n" + i + "\t " + arrRoll[i];
			// System.out.println("index "+i+ " Value "+ arr[i]);
		}
		area.setText(output);
		JOptionPane.showMessageDialog(null, area, "Number of times sum rolled", JOptionPane.PLAIN_MESSAGE);

	}

	/**
	 * Rolls the dices for given number of times and counts the number of each value rolled 
	 * @param arr
	 * @param num
	 */
	private static void diceFunction(int[] arr, int num) {
		int sumofDice = 0;
		for (int i = 0; i < num; i++) {
			int dice1 = (int) (Math.random() * 6 + 1);
			int dice2 = (int) (Math.random() * 6 + 1);
			sumofDice = dice1 + dice2;
		//	int rollnumber = i + 1;
		//	System.out.println(rollnumber + " roll sum :" + sumofDice);
			for (int j = 2; j < arr.length; j++) {
				if (sumofDice == j) {
					arr[j] = arr[j] + 1;
				}
			}

		}
	}
}
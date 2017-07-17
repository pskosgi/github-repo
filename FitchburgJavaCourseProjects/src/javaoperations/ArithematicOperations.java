package javaoperations;
import java.util.Scanner;

/**
 * Program1 for Arithematic Operations
 * @author Prashanthi Sudha Kosgi
 * Date : 6/2/2017
 *
 */
public class ArithematicOperations {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		int integer1, integer2, integer3;
		int sum;
		float average;
		int product;

		System.out.println("Enter First integer1: ");
		integer1 = input.nextInt();

		System.out.println("Enter second integer2: ");
		integer2 = input.nextInt();

		System.out.println("Enter third integer3: ");
		integer3 = input.nextInt();

		   // Sum of three integers
		sum = integer1 + integer2 + integer3;
		System.out.println("The sum of three integers is : " + sum);
		
		
         //Average of three integers
		
		average = (float) (integer1 + integer2 + integer3) / 3;
		System.out.format("The average of three integers is %.2f%n",  average);
        
		//Product of three integers
		
		product = integer1 * integer2 * integer3;
		System.out.println("The product of three integers is : " + product);

		// **Largest number**

		if (integer1 > integer2 && integer1 >integer3) {
			System.out.println("Largest of the three Integers is : " + integer1);
		}
		if (integer2 > integer1 && integer2 > integer3) {
			System.out.println("Largest of the three Integers is : " + integer2);
		}
		if (integer3 > integer1 && integer3 > integer2) {
			System.out.println("Largest of the three Integers is : " + integer3);
		}

		// //**Smallest number**
		if (integer1 < integer2 && integer1 < integer3) {
			System.out.println("Smallest of the three Integers is : " + integer1);
		}
		if (integer2 < integer1 && integer2 < integer3) {
			System.out.println("Smallest of the three Integers is : " + integer2);
		}
		if (integer3 < integer1 && integer3 < integer2) {
			System.out.println("Smallest of the three Integers is  : " + integer3);
		}

		input.close();

	}

}

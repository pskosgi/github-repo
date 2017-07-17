/**
 * Program for Calculating employee weekpay.
 * @author Prashanthi Sudha Kosgi
 * Date : 6/9/2017
 *
 */


package inheritance;

public class Employee {

	// Declaring variables
	private String department;
	double payRate;
	private String name;
	private double weekpay;
	

	public Employee(String name, String department, double payRate) {
		this.name = name;
		this.department = department;
		this.payRate = payRate;
	}

	// Accessor method(getters)
	public String getEmp() {
		return "Employee: " + name + " works in the " + department + " department" ;
	}


	// Mutator method(setters) to set employee's department.
	public void setDepartment(String department) {
		this.department = department;
	}

	public void setPayRate(double payRate) {
		this.payRate = payRate;
	}
	
	public double getPayRate() {
		return payRate;
	}
	
	public String getdepartment() {
		return department;
	}
	public String getname() {
		return name;
	}
// calculating weeklpay
	public double weeklypay(int noOfHours) {
		if (noOfHours < 40) {
			weekpay = noOfHours * payRate;
		} else if (noOfHours >= 40) {
			weekpay = 40 * payRate;
		}
		return weekpay;

	}
}

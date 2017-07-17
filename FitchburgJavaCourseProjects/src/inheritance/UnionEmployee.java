package inheritance;

public class UnionEmployee extends Employee {

	private double dues;

	public UnionEmployee(String name, String department, double payRate, double dues) {
		super(name, department, payRate);
		this.dues = dues;

	}

	// mutator method to set employee's dues
	public void setdues(double dues) {
		this.dues = dues;
	}

	public double getdues() {
		return dues;
	}
//weeklypay for union employee
	@Override
	public double weeklypay(int noOfHours) {

		double weekpay1 = 0;
		double extraHours = noOfHours - 40;

		dues = getdues();

		if (noOfHours <= 40) {

			double weeklyPayUnion = (super.weeklypay(noOfHours));
			weekpay1 = weeklyPayUnion - dues;
		}
		if (noOfHours > 40) {

			double weeklyPayUnion = (super.weeklypay(40) + (extraHours * 1.5 * payRate));
			weekpay1 = weeklyPayUnion - dues;

		}

		return weekpay1;
	}
}

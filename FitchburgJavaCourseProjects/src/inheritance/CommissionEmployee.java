package inheritance;

public class CommissionEmployee extends Employee {
	double commissionRate;
	double salesAmount;

	public CommissionEmployee(String name, String department, double payRate, double commissionRate,
			double salesAmount) {
		super(name, department, payRate);
		this.commissionRate = commissionRate;
		this.salesAmount = salesAmount;
	}

	public void setcommissionRate(double commissionRate) {
		this.commissionRate = commissionRate;
	}

	public void setsalesAmount(double salesAmount) {
		this.salesAmount = salesAmount;
	}
// calculating weeklypay for commission employee
	@Override
	public double weeklypay(int noOfHours) {
		double weeklyPay = super.weeklypay(noOfHours);
		double commionRate = getcommissionRate();
		double salesAmt = getsalesAmount();

		double newWeeklyPay = weeklyPay + (commionRate * salesAmt);

		return newWeeklyPay;

	}

	public double getcommissionRate() {
		return commissionRate;
	}

	public double getsalesAmount() {
		return salesAmount;

	}

}

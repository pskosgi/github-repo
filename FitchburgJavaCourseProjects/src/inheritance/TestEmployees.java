package inheritance;

public class TestEmployees {

	public static void main(String[] args) {
										// name,  department,  payRate,  dues
		UnionEmployee uEmp1 = new UnionEmployee("Jim", "CE", 30, 20);
		Employee uEmp2 = new UnionEmployee("Kim", "IT", 40, 15);
		Employee uEmp3 = new UnionEmployee("Tim", "JD", 45, 30);
		
							// name,  department,  payRate,  commissionRate, salesAmount
		Employee cEmp1 = new CommissionEmployee("Jane", "CE", 30,5,1100.00);
		Employee cEmp2 = new CommissionEmployee("Tommy", "IT", 40, 9,1000.00);
		Employee cEmp3 = new CommissionEmployee("Peter", "JD", 45, 16,900.00);
		
		
		TestEmployees tEmp = new TestEmployees();
		tEmp.display(uEmp1,cEmp1,35,35);
		tEmp.display(uEmp2,cEmp2,40,40);
		tEmp.display(uEmp3,cEmp3,45,45);
	}

	void display(Employee uemp, Employee cemp, int numofhours, int numofhours1) {

		System.out.println("Commission Employee Name is:" + cemp.getname());
		System.out.println("Commission Employee Department is:" + cemp.getdepartment());
		System.out.println("Weekly pay for Commission Employee:" + cemp.weeklypay(numofhours1));
		System.out.println("---------------------------------------------------------------");
		System.out.println("Union Employee Name is:" + uemp.getname());
		System.out.println("Union Employee Department is:" + uemp.getdepartment());
		System.out.println("Weekly pay for Union Employee:" + uemp.weeklypay(numofhours));
		System.out.println("---------------------------------------------------------------");

	}

}

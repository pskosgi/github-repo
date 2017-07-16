package com.java.designpattern.factory;

public class MainExecutionClass {
	public static void main(String[] args) {
		Mobile mobile = MobileFactory.createMobile(Mobile.SAMSUNG);
		
		// ConnectionFactory.getConnection("");   to get different connection objects like DB2, oracle, SQL
		
		if (mobile instanceof Samsung) {
			System.out.println("mobile is instance of samsung...");
			// now you can work on this samsung object...
		} else if (mobile instanceof Nokia) {
			System.out.println("mobile is instance of Nokia...");
		} else if (mobile instanceof IPhone) {
			System.out.println("mobile is instance of Iphone...");
		} else {
			System.out.println("No object created...");
		}
		
		System.out.println("Model Number " +mobile.getModelNumber());
	}
}

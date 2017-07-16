package com.java.designpattern.factory;

public class MobileFactory {
	public static Mobile createMobile(String type){
		
			System.out.println("type Request : "+type);
			if(Mobile.IPHONE.equals(type)){
				System.out.println("Returning IPhone object...");
				IPhone iPhone =new IPhone(2, "A9", "A9 GPu");
				return iPhone;
			}else if(Mobile.NOKIA.equals(type)){
				System.out.println("Returning Nokia object...");
				Nokia nokia =new Nokia(2,"ARM");
				return nokia;
			}else if(Mobile.SAMSUNG.equals(type)){
				System.out.println("Returning Samsung object...");
				Samsung samsung =new Samsung("Intel");
				return samsung;
			}else{
				return null;
			}
		
	}
}

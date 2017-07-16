package com.java.designpattern.factory;

public class IPhone implements Mobile{
	private int ramSize;
	private String processor;
	private String GPU;
	public IPhone(int ramSize, String processor, String GPU){
		this.ramSize = ramSize;
		this.processor = processor;
		this.GPU = GPU;
	}
	
	@Override
	public String getModelNumber(){
		return "i7Plus";
	}
	
	@Override
	public int getMemorySize(){
		return 500;
	}
	
}

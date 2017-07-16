package com.java.designpattern.factory;

public class Nokia implements Mobile{
	private int ramSize;
	private String processor;
	
	public Nokia(int ramSize, String processor){
		this.ramSize = ramSize;
		this.processor = processor;
	}
	
	@Override
	public String getModelNumber(){
		return "Lumia324";
	}
	
	@Override
	public int getMemorySize(){
		return 125;
	}
	
	public int getNokiaMemorySize(){
		return 125;
	}
}

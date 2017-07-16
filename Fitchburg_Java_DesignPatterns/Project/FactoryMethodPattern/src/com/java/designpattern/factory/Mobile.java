package com.java.designpattern.factory;

public interface Mobile {
	public static final String IPHONE="IPHONE";
	public static final String NOKIA="nokia";
	public static final String SAMSUNG="samsung";
	
	public String getModelNumber();
	
	public int getMemorySize();
}

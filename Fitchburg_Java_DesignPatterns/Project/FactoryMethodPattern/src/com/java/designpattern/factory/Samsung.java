package com.java.designpattern.factory;

public class Samsung implements Mobile {
	private int ramSize;
	private String processor;

	public Samsung(String processor) {
		this.processor = processor;
		this.ramSize = 2;
	}

	@Override
	public String getModelNumber() {
		return "S7";
	}

	@Override
	public int getMemorySize() {
		return 250;
	}
}

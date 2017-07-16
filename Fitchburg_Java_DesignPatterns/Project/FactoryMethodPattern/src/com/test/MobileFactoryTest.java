package com.test;

import static org.junit.Assert.*;

import org.junit.Test;

import com.java.designpattern.factory.IPhone;
import com.java.designpattern.factory.Mobile;
import com.java.designpattern.factory.MobileFactory;
import com.java.designpattern.factory.Nokia;
import com.java.designpattern.factory.Samsung;

public class MobileFactoryTest {

	@Test
	public void testCreateMobileForSamsung() {
		// this method returns a object or null depending upon the input string
		Mobile mobile = MobileFactory.createMobile(Mobile.SAMSUNG);
		boolean a = mobile instanceof Samsung;
		boolean b = mobile instanceof Nokia;
		boolean c = mobile instanceof IPhone;

		// expected is 'a' is true and b, c should be false
		assertTrue("It should be true because, it is Samsung instance.", a);
		assertFalse("", b);
		assertFalse("", c);

		// expected is "S7"
		String modelNumber = mobile.getModelNumber();
		String expectedValue = "S7";
		assertEquals("Comapring both values", expectedValue, modelNumber);

	}

	@Test
	public void testCreateMobileForNokia() {
		// here testing createMobile method of mobile class
		// create aruments for that method
		// call the method. (either by instance or class name)
		// Check or add return
		String arg1 = Mobile.NOKIA;
		Mobile mobile = MobileFactory.createMobile(arg1);

		// checking for instance.

		boolean a = mobile instanceof Samsung;
		boolean b = mobile instanceof Nokia;
		boolean c = mobile instanceof IPhone;

		// expected is 'b' is true and a, c should be false
		assertFalse("", a);
		assertTrue("It should be true because, it is Nokia instance", b);
		assertFalse("", c);

		// expected 125
		int memorySize = mobile.getMemorySize();
		int expectedValue = 125;
		assertEquals("checking both the values", expectedValue, memorySize);
	}

	@Test
	public void testCreateMobileForIphone() {
		String arg2 = Mobile.IPHONE;
		Mobile mobile = MobileFactory.createMobile(arg2);
		boolean a = mobile instanceof Samsung;
		boolean b = mobile instanceof Nokia;
		boolean c = mobile instanceof IPhone;

		// expected is 'c' is true and a, b should be false
		assertFalse("", a);
		assertFalse("", b);
		assertTrue("It should be true because, it is Iphone instance", c);

	}

	@Test
	public void testCreateMobileForOthers() {
		String arg = "plus23";
		Mobile mobile = MobileFactory.createMobile(arg);
		String expectedValue = null;
		assertEquals("checking values", expectedValue, mobile);

	}

	@Test
	public void testCreateMobileForNull() {
		String arg = null;
		Mobile mobile = MobileFactory.createMobile(arg);
		String expectedValue = null;
		assertEquals("checking values", expectedValue, mobile);

	}
}

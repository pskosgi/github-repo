package lab4;
 /**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */
 
import static org.junit.Assert.*;
import org.junit.Test;
public class MyClassTest {
	/**
	 * Test method for {@link junit.test.MyClass#multiply(int, int)}
	 */
	@Test
	public void testMultiply() {
		MyClass tester = new MyClass();
		assertEquals("Result",50, tester.multiply(10, 5));
		//fail("Not yet implemented");
	}
}

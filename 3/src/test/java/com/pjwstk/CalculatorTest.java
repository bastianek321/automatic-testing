package com.pjwstk;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class CalculatorTest {
    private Calculator calculator = new Calculator();

    @Test
    public void testAddition(){
        double result = calculator.add(10, 10);
        Assertions.assertEquals(20, result);
    }

    @Test
    public void testSubtraction(){
        double result = calculator.subtract(10, 10);
        Assertions.assertEquals(0, result);
    }

    @Test
    public void testMultiplication(){
        double result = calculator.multiply(10, 10);
        Assertions.assertEquals(100, result);
    }

    @Test
    public void testDivision(){
        try{
            double result = calculator.divide(10, 0);
            Assertions.assertEquals(1, result);
        } catch (ArithmeticException e){
            System.out.println(e.getMessage());
        }
    }

    @Test
    public void testDivide_threeByThree_shouldBeOne(){
        try {
            double result = calculator.divide(3,3);
            Assertions.assertEquals(1, result);
        } catch (ArithmeticException e){
            System.out.println(e.getMessage());
        }
    }

    @Test
    public void testAdd_twoAndThree_shouldBeFive(){
        double result = calculator.add(2, 3 );
        Assertions.assertEquals(5, result);
    }

    @Test
    public void testSubtract_twoAndThree_shouldBeMinusOne(){
        double result = calculator.subtract(2, 3 );
        Assertions.assertEquals(-1, result);
    }

    @Test
    public void testMultiply_twoAndThree_shouldBeSix(){
        double result = calculator.multiply(2, 3 );
        Assertions.assertEquals(6, result);
    }

}

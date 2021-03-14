package com.pjwstk;

import org.junit.Before;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

public class CalculatorTest {
    private Calculator calculator;

    @Before
    public void initialize(){
        calculator = new Calculator();
    }


    @Test
    public void testAddition(){
        double result = calculator.add(10, 10);
        Assertions.assertEquals(20, result);
    }


}

package com.pjwstk;

public class Calculator {

    public Calculator(){}

    public double add(double a, double b) {
        return a + b;
    }

    public double subtract(double a, double b) {
        return a - b;
    }

    public double multiply(double a, double b) {
        return a * b;
    }

    public double divide(double a, double b) throws ArithmeticException {
        if (b == 0) throw new ArithmeticException("You can't divide by 0");
        return a / b;
    }
    public String stringifyAddition(double number){
        return String.valueOf(number);
    }
    public boolean isOdd(int number){
        return number % 2 == 1;
    }
}

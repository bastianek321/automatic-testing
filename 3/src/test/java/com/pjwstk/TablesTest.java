package com.pjwstk;

import org.junit.Before;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TablesTest {

    private Tables tables = new Tables();
    int[] array = {4,5,3,1};

    @Test
    public void checkIfTablesIsNotNull(){
        Assertions.assertNotNull(tables);
    }

    @Test
    public void sortTest(){
        int[] result = tables.sort(array);
        int[] expected = {1,3,4,5};
        Assertions.assertArrayEquals(expected, result);
    }

    @Test
    public void replaceAllTest(){
        int[] result = tables.replaceAll(array, 5, 6);
        int[] expected = {4,6,3,1};
        Assertions.assertArrayEquals(expected, result);
    }

    @Test
    public void arrayHasNumberTest(){
        Assertions.assertTrue(tables.hasN(array, 4));
    }

    @Test
    public void testArrayHasNumber_numberArrayWasInitiatedWith_shouldBeTrue(){
        Assertions.assertTrue(tables.hasN(array, 5));
    }

    @Test
    public void arrayHasNotGotANumber(){
        Assertions.assertFalse(tables.hasN(array, 20));
    }

    @Test
    public void testArrayHasNumber_numberArrayWasNotInitiatedWith_shouldBeFalse(){
        Assertions.assertFalse(tables.hasN(array, 10));
    }

    @Test
    public void sumTest(){
        Assertions.assertEquals(13, tables.sum(array));
    }

    @Test
    public void testArrayReverse(){
        int[] result = tables.reverse(array);
        int[] expected = {1, 3, 5, 4};
        Assertions.assertArrayEquals(expected, result);
    }
}

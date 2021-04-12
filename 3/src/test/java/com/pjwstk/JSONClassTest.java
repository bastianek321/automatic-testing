package com.pjwstk;

import org.json.JSONObject;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class JSONClassTest {

    @Test
    public void testHasKey_jsonInitiatedWith_shouldBeTrue(){
        JSONObject object = new JSONObject("{ \"John\" : \"Doe\" }");
        JSONClass json = new JSONClass();
        Assertions.assertTrue(json.hasKey(object,"John"));
    }

    @Test
    public void testIsEmpty_jsonInitiatedWith_shouldBeFalse(){
        JSONObject object = new JSONObject("{ \"Albert\" : \"Doe\" }");
        JSONClass json = new JSONClass();
        Assertions.assertFalse(json.notEmpty(object));
    }

    @Test
    public void testHasKey_jsonInitiatedWith_shouldBeFalse(){
        JSONObject object = new JSONObject("{ \"John\" : \"Doe\" }");
        JSONClass json = new JSONClass();
        Assertions.assertFalse(json.hasKey(object,"George"));
    }
}

package com.pjwstk;

import org.json.*;

import java.util.Iterator;

public class JSONClass {

    public JSONClass() {
    }

    public boolean hasKey(JSONObject object, String desiredKey){
        boolean hasKey = true;
        for (Iterator<String> it = object.keys(); it.hasNext(); ) {
            String key = it.next();
            if(key.equals(desiredKey)){
                break;
            } else {
                hasKey = false;
            }
        }
        return hasKey;
    }

    public boolean notEmpty(JSONObject object){
        return object.isEmpty();
    }
}

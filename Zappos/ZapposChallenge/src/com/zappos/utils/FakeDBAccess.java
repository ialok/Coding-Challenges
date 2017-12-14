package com.zappos.utils;

import java.util.Date;

public class FakeDBAccess {

    public Date getLastLoginForUser(String userId) {

        if(Math.random() < .5)
            return new Date(System.currentTimeMillis());

        return new Date(System.currentTimeMillis()-42*60*60*1000);
    }
    public void setLastLoginForUser(String userId, Date date) throws Exception {
// do nothing
    }
}

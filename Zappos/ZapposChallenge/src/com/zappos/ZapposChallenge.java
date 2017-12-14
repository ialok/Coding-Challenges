package com.zappos;

import com.zappos.cache.LRUCache;
import com.zappos.utils.FakeDBAccess;

import java.util.Date;

/**
 * Created by ialok on 12/3/17.
 */
public class ZapposChallenge {
    private static Login login;

    public static void main(String[] args) {
        System.out.println("Initialize the login service with capacity:100");
        login = new Login(
                new LRUCache.CacheBuilder<String, Date>().capacity(100).build(),
                new FakeDBAccess());

        // Can use logger
        System.out.println();
        System.out.println("Initialize user 123");
        login.userJustLoggedIn("123");

        System.out.println("Check if user:123 has logged in last 24hr");
        System.out.println(login.hasUserLoggedInWithin24("123"));

        System.out.println("Check if user:1234 has logged in last 24hr");
        System.out.println(login.hasUserLoggedInWithin24("1234"));
    }
}

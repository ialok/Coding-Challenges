package com.zappos;

import com.zappos.cache.Cache;
import com.zappos.cache.LRUCache;
import com.zappos.utils.FakeDBAccess;
import com.zappos.utils.LoginService;

import java.util.Date;

/**
 * Created by ialok on 12/3/17.
 */
public class Login implements LoginService {

    private Cache<String, Date> cache;
    private FakeDBAccess dbConnection;

    public Login(Cache<String, Date> cache, final FakeDBAccess dbConnection) {
        this.cache = cache;
        this.dbConnection = dbConnection;
    }

    @Override
    public boolean hasUserLoggedInWithin24(final String userId) {
        /*
         * check cache - if present compute date diff and return
         * else fetch from database and insert in cache and compute date diff and return
         */

        Date lastLogin = cache.get(userId);
        if (lastLogin == null) {
            lastLogin = dbConnection.getLastLoginForUser(userId);
            cache.put(userId, lastLogin);
        }
        return lastLogin.getTime() > (System.currentTimeMillis() - DateConstants.MILLI_SECONDS_PER_DAY);
    }

    @Override
    public void userJustLoggedIn(final String userId) {
        /*
         *  Puts the login date of the user in the cache
         */
        cache.put(userId, new Date());
    }

    private static class DateConstants {
        public static long MILLI_SECONDS_PER_DAY = 24 * 60 * 60 * 1000L;
    }
}
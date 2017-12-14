package com.zappos.cache;

import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by ialok on 12/3/17.
 */

public class LRUCache<Key, Value> implements Cache<Key, Value>, Runnable{
    private long maxCapacity = 100L;
    private long size = 0L;
    private long pollingInteraval = 0L;
    private LinkedHashMap<Key, Value> cache;

    @Override
    public void put(final Key key, final Value value) {
        if (this.cache.containsKey(key)) {
            this.cache.remove(key);
            this.size -= 1L;
        }
        else if (this.size() == this.getCapacity()) {
            Iterator<Key> iterator = this.cache.keySet().iterator();
            iterator.next();
            iterator.remove();
            this.size -= 1L;
        }
        cache.put(key, value);
        this.size += 1L;
    }

    @Override
    public Value get(final Key key) {
        Value value = this.cache.get(key);
        if (value != null) {
            this.put(key, value);
        }
        else {
            value = null;
        }
        return value;
    }

    @Override
    public void invalidate(final Key key) {
        if (this.cache.containsKey(key)) {
            this.cache.remove(key);
            this.size -= 1L;
        }
    }

    @Override
    public void invalidateAll() {
        this.cache.clear();
        this.size = 0L;
    }

    @Override
    public long size() {
        return this.size;
    }

    private long getCapacity() {
        return this.maxCapacity;
    }

    @Override
    public void run() {
        if (pollingInteraval>0) {
            Timer timer = new Timer();
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    invalidateAll();
                }
            }, pollingInteraval);
        }
    }
    /*
        CacheBuilder seems forced for the current challenge
        but could have been expanded to include ttl, concurrency etc.
     */
    public static class CacheBuilder<Key, Value> {
        private long maxCapacity;
        private LinkedHashMap<Key, Value> cache;
        private long pollingInteraval;

        public CacheBuilder() {
            this.cache = new LinkedHashMap<Key, Value>();
        }

        public CacheBuilder capacity(final long capacity) {
            this.maxCapacity = capacity;
            return this;
        }

        public CacheBuilder polling(final long pollingInterval) {
            this.pollingInteraval = pollingInterval;
            return this;
        }

        public Cache<Key, Value> build() {
            return new LRUCache(this);
        }
    }

    private LRUCache(final CacheBuilder builder) {
        this.maxCapacity = builder.maxCapacity;
        this.size = 0L;
        this.cache = builder.cache;
        this.pollingInteraval = builder.pollingInteraval;
    }

}
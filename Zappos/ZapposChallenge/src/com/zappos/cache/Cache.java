package com.zappos.cache;

/**
 * Created by ialok on 12/3/17.
 */

public interface Cache<Key, Value> {

    /**
     * Creates a mapping between the key and the value. If the key already
     * existed in the cache, the old value gets overwritten
     *
     * @param key
     * @param value
     * @return
     *      Nothing
     */
    public void put(Key key, Value value);

    /**
     * Returns the value for the key present in the cache. If no such key exists
     * null is returned
     *
     * @param key
     * @return
     *      Value Value associated to the key or null if no such key exists
     */
    public Value get(Key key);

    /**
     * Invalidates a key in the cache. Do nothing if key is not present
     *
     * @param key
     * @return
     *      Nothing
     */
    public void invalidate(Key key);

    /**
     * Invalidates all keys in the cache.
     * Similar to initializing a new cache/mapping
     *
     * @return
     *      Nothing
     */
    public void invalidateAll();

    /**
     * Checks for the number of elements in a cache
     *
     * @return
     *      long Number of elements in the cache
     */
    public long size();
}

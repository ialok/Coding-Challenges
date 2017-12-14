# Zappos Coding Challenge

Content: ZapposChallenge.jar, README.md, Zipped source

Run: java -cp ZapposChallenge.jar com.zappos.ZapposChallenge
Output: java -cp ZapposChallenge.jar com.zappos.ZapposChallenge
```
Initialize the login service with capacity:100

Initialize user 123
Check if user:123 has logged in last 24hr
true
Check if user:1234 has logged in last 24hr
true
```
The code is structured in the following packages
  - com.zappos.cache
  -- Contains the *cache* interface and the implementing (*LRU*) class
  - com.zappos.utils
  -- Contains the code given in the challenge (Interface and FakeDB)

The cache interface provides basic methods necessary for the cache. We implement LRU Cache as the cache needed
for this challenge. LRUCache implement the cache interface and provides CacheBuilder for the initialization.

#### Design Choice

  - Cache interface so that different types of cache logic (LRU, LFU etc) have similar contract
  - CacheBuilder for more flexible cache initialization (no more multiple overloaded constructors)
  - Choice of having a polling interval where polling interval > 0 means invalidate all elements of cache
  -- The polling tied to invalidateAll can be disasterous for performance in a large scale application

#### Questions:
1. What was the reasoning behind your implementation of the cache?
    Fetching data from database each time will be suboptimal in some cases. One of the reason for this is that
    database reside on the disk and disk access is slower than memory access.
    We can map the user 

2. How does your cache improve performance?
    A user request doesn't hit the database each time. For example: if a client request asks for user-id "ABC"
    we first check the cache to see if an entry tied to that user-id exists. If it does we return value based
    on the necessary calculations (last login in 24hr).

    If the cache did not exist, each request will go to the database. Database access can be slower than in-memory(cache)
    access and we may see significant performance hit.

3. What are the various usage patterns that make the cache more or less effective in terms of performance?
    Possible usage patterns that can make the cache less effective are:
    1. New userid in each request (the request will have to go to the database)
    2. A request may not come for quite sometime and it might get purged (LRU). To our luck the request may arrive again 
       after it is purged and then never to be seen again to long time. When can this happen:-> write a script runs as a
       cron job and strict timeout requirement for any call. 
    3. First request (cold start) and if the polling invalidates each entry in cache, performance will not be great

swap
==========

### Scenario
Swap usage alert

```
Monit Resource limit matched alert resources at Sun, 20 May 2014 05:46:46 on server2,
Description: swap usage of 28.1% matches resource limit [swap usage>20.0%]
```


### Actions performed by this picklebot
1. Gather the current swap statistics from 'vmstat' and analyze if the server is actively swapping or not
2. If the server is actively swapping, then list the top 10 memory consuming processes and escalate incident to next level on-call engineer for further actions.
3. If the server is not actively swapping, then resolve the incident

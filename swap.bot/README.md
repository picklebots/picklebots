swap.bot
==========

### Scenario
Swap usage alert

### Actions performed by this picklebot
1. Gather the current swap statistics from 'vmstat'
2. If the server is actively swapping, then list the top 10 memory consuming processes and escalate incident to next level on-call engineer for further actions.
3. If the server is not actively swapping, then resolve the incident

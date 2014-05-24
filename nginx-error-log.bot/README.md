nginx-error-log.bot
==========

### Scenario
When we have monit to watch the ngnix error log, we end up getting notified for the unwanted routes which are accessed by bots/script kiddies.
This picklebot consumes the monit alert and only escalates only when request for a valid application route results in error.

### Actions performed by this picklebot
1. Gather the routes which resulted in error based on the alert timestamp.
2. Ignore the monit incidents which have succeeded.
3. If the routes collected are valid one in the application as specified inside the playbook, escalate it , else resolve the incident. 

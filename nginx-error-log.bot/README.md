nginx-error-log.bot
==========

### Scenario
When we have monit to watch the ngnix error log file (/var/log/nginx/error.log), we end up getting notified whenever the log file changes. But errors due to robots/script kiddies probing the domain are just noisy. This picklebot consumes the monit alert and escalates only when a request for the valid application url results in an error.

### Actions performed by this picklebot
1. Read the log file and gather the urls which resulted in error based on the alert timestamp.
2. If the errored out urls are relevant to the application, then escalate it. Otherwise resolve the incident. 
3. It also ignores the subsequent success alert (when there is no more change in error log for few minutes), since it's not relevant in this case.

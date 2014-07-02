nginx-error-log.bot
==========

### Scenario
When we have [monit](https://mmonit.com/monit) to watch the ngnix error log file (/var/log/nginx/error.log), we end up getting notified whenever the log file changes. But errors due to robots/script kiddies probing the domain are just noisy. This picklebot consumes all the nginx error alerts and escalates only when it is relevant (a request for the valid application url results in an error).

```
Monit Timestamp failed alert nginx_error at Thu, 22 May 2014 07:35:17 on server1,
Description: timestamp test failed for /var/log/nginx/error.log
```

### Actions performed by this picklebot
1. Read the log file and gather the urls which resulted in error based on the alert timestamp.
2. If the errored out urls are relevant to the application, then escalate the incident along with log contents.
3. Otherwise, the errors are due to attempts by script kiddies. So resolve the incident. 

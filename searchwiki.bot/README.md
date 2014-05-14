searchwiki.bot
==========

### Scenario
Search for the incident description in the internal company wiki and add results (if found) to the incident notes

### Actions performed by this picklebot
1. Extracts required details from the pagerduty incident that's triggered
2. Searches the wiki using extracted description and filters just the links available in search results.
3. Add the links as a note to pagerduty incident
4. Escalates the incident to next level (an on-call engineer) to look further into the incident

NOTE: This picklebot searches against unix.stackexchange.com for the purpose of demonstration. This can be changed to the url relevant for internal company wiki as required.    

### Dependencies
Xidel - HTML/XML data extraction tool - http://videlibri.sourceforge.net/xidel.html

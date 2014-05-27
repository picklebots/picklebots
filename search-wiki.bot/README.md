searchwiki.bot
==========


### Scenario
When an incident gets triggered, do a search in the internal company wiki using keywords from the incident description and annotate incident with search results

Video: https://www.youtube.com/watch?v=RBeCoEcZvv0


### Actions performed by this picklebot
1. Extracts required details from the pagerduty incident that's triggered
2. Searches the wiki using extracted keywords and filters just the links available in search results.
3. Add the links as a note to pagerduty incident
4. Escalates the incident to next level (an on-call engineer) to look further into the incident

NOTE: This picklebot searches against unix.stackexchange.com for the purpose of demonstration. This can be changed to the url relevant for internal company wiki as required.    

### Dependencies
Xidel - HTML/XML data extraction tool - http://videlibri.sourceforge.net/xidel.html

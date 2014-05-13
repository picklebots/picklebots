swapbot
==========

A  sample picklebot to auot heal monitoring sawp alerts. 
This checks for current paging data from 'vmstat'. If the pagiing is still happening after the alert, ticket is updated with top 10 memory consuming processes and escalated to the next level engineer.Else the ticket is resolved by picklebot.


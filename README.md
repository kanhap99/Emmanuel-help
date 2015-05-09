# Emmanuel-help
This repo contains code which I wrote as part of JIS Tech service clubs efforts to help Yayasan emmanuel manage their digital mobile library.

Yayasan Emmanuel needed help removing duplicate copies of books from their bibliography records and categorizing item headers of all duplicates as one item header. 
-This script uses the python pandas library to read data from the csv and manipulate it, before storing it in another csv.
-Duplicates are removed by searching for a simple regex search pattern which exists on the copies of all duplicates and concatenating their item headers to the item header of the original copy.

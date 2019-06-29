# DevOps Lab 2019 (May-August)
# Overall system data

## Description

Simple Python app which monitors the system. Output is written to the plain text file or json file.
psutil library is used inside

App creates snapshots of the following systems parameters each 5 minutes(by default, can be changed): 

1) Overall CPU load 

2) Overall memory usage 

3) Overall virtual memory usage 

4) IO information 

5) Network information 

## Installation

`pip install SystemInfo-1.0-py3-none-any.whl`

## Settings

Initial config parameters are located in 'config.json' file: -type of output file (json or txt)
                                                             -interval (in seconds) 
You can configure type of output file (json or txt) and interval (in seconds) 

## Output examples

Examples of the output:

`output.txt`:

SNAPSHOT 1: TIMESTAMP 06/22/2019, 18:14:38: Overall cpu load - 11.2 %; 
 Overall disk memory usage (bytes) - sdiskusage(total=701940367360, used=254688751616, 
 free=411571302400, percent=38.2)... (output shortened)


`output.json`:

SNAPSHOT 1: TIMESTAMP 06/22/2019, 18:14:38: Overall cpu load - 11.2 %; 
 Overall disk memory usage (bytes) - sdiskusage(total=701940367360, used=254688751616, 
 free=411571302400, percent=38.2)... (output shortened)
 


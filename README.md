# Election Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following tasks to complete the
election audit of a recent local congressional election that took place in Arapahoe, Denver and Jefferson counties Colorado (basically Denver and its suburbs, shown below).

<br />

<img src ="https://github.com/carlosjennings1991/Election_Analysis/blob/main/Resources/counties_outlined_red.png" width="600" height="434">

<br />

The goal of the analysis was to do the following:

  1. Calculate the total number of votes cast. 
  2. Get a complete list of candidates who received votes. 
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won. 
  5. Determine the winner of the election based on popular vote. 
  
 ### Resources 
 * Data Source: [election_results.csv](https://github.com/carlosjennings1991/Election_Analysis/blob/main/Resources/election_results.csv) (feel free to download)
 * Software: Python 3.7.6, Visual Studio Code, 1.51.1
 
 ### Summary
 The analysis of the election show that:
 * There were 369,711 votes cast in the eletion. 
 * The candidates were:
   * Charles Casper Stockham
   * Diana DeGette
   * Raymon Anthony Doane
   
 * The candidate results were: 
   * Charles Casper Stockham received 23.0% of the vote and 85,213 votes total.
   * Diana DeGette received 73.8% of the vote and 272,892 votes total.
   * Raymon Anthony Doane received 3.1% of the vote and 11,606 votes total.
   
 * The winner of the election was:
   * Diana DeGette received 73.8% of the vote and 272,892 votes total.
   
 ![election results screenshot](https://github.com/carlosjennings1991/Election_Analysis/blob/main/Resources/results_screenshot.png)  
   
 Those script that analyzes the code and produces the above stats can be found here - [python file](https://github.com/carlosjennings1991/Election_Analysis/blob/main/PyPoll_Challenge.py)
    
## Challenge Overview

## Challenge Summary

The good news about this script it that it can be used anywhere as long as the source .csv file is formulated in the same way. All you need for this to work is a spreadsheet with three things. 

* A Unique ID for each cast vote. 
* The County in which the vote took place.
* The candidate who received the vote. 

An simple way this could have been improved if the candidate's performance and vote totals were analyzed per county. 


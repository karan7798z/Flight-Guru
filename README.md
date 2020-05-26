# Flight-Guru
Final Project for the course - Advanced Database Systems at Texas A&amp;M University

The project aims at creating a system that would help the customer with their travel plans. As we know, flight delays can result in disruption of someone’s travel plan. The system that we plan on designing and implementing will aid the customer by suggesting the flights with minimum chances of delay based on past data. Also, it will suggest the best destination to visit during a particular time of the year and the best flights to take for it.

## Algorithm
* First, we perform etl on the datasets to remove unwanted values and attributes, and load the data in appropriately in the tables.
* The transformed data sets are loaded on the MariaDB Galera Cluster, which has been setup on 3 AWS EC2 Instances.
* Input is taken from the user through a web page and passed to an API. Input
includes - Origin, Destination and Travel Date.
* API executes the SQL queries on the database and sends the output back to the
webpage, to display the charts - Best Flights, and Best Destinations.

## Prerequisites
An account on AWS to setup MariaDB Galera cluster of three nodes on EC2 platform that will store the database.

## Installing
* Python 3.6.
* Required Packages to be installed: numpy, pandas, scipy, Flask.

## Phases
* Download dataset from [here](https://www.kaggle.com/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018), extract the zip file and copy it to host

### 1. ETL:
* **etl.py**: This python file reads the dataset from 2018 to 2014 using dataframe, removes unwanted attributes, extract month from date column and adds a new column into the Dataframe. The Dataframes for each year is split into two halves and loaded into new csv. The reason to split the dataset is to make it easy to load it on the cluster.
* **SQL Statements**: In this file, there are 3 create table scripts. These scripts create 3 tables - flight (which will contain the overall flight data), airline (which will contain the airline Codes and Names) and airport (which will contain the airport Codes and Names). These tables are created, by following the ERD Representations shown in the files – Project Phase I – Logical ERD.png & Project Phase I – Physical ERD.png that contain the Logical and Physical ERD’s respectively. After these 3 create table scripts, there are 3 Load data scripts that load these tables one by one, with their respective intended data source csv files.

### 2. API:
* **api2.py**: This file contains the code written for hosting API’s. We have used Python’s Flask Library for this. We have created 3 API’s -
   1. **/getAllAirports**: This API is called by the front end for fetching the list of airports to be displayed in the drop downs of Origin and Destination. It essentially calls/executes the SQL Query that fetches Airport Code and Name from airport table.
   2. **/getBestFlights**: This API is called by the front end for fetching the best airlines (ones that have least delay, top 5 of those). It essentially calls/executes the SQL query that fetches Airline Name, Airline Code, Average Delay faced (average of departure delay and arrival delay) from the join of flight and airline table.
   3. **/getTopDestinations**:This API is called by the front end for fetching the list of best destinations that the user can plan on visiting. This essentially calls/executes the SQL query that fetches the list of destinations, on the basis of the maximum flights that have flown to a destination, from user’s origin location, during his intended period of travel. It is based on the assumption that the more the number of flights going to a location, more popular that place is at a given time.
 
### 3. UI:
* The UI displays the information collated from the API calls, through charts. There are 2 main charts. One that displays Best Flights for a user, and another that displays the Best Destinations that a user can visit. The Best destination list is clickable, and clicking on a destination from that list, displays the best flights for that destination in return.
* The entire UI repository, is contained in the zip file – **birds-master.zip**.

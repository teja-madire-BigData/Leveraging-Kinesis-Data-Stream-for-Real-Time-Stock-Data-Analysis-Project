# Leveraging-Kinesis-Data-Stream-for-Real-Time-Stock-Data-Analysis-Project

## Introduction

In this project, I executed an End-To-End Data Engineering Project on Real-Time Stock Market Data using Kinesis Data Stream.

I have used different technologies such as Python, Amazon Web Services (AWS), Kinesis Data Stream, Lambda, Glue, Athena, and SQL

## Architecture 
<img src="Architecture.jpeg">

## Technology Used
- Programming Language - Python
- Amazon Web Service (AWS)
  
1. S3 (Simple Storage Service)
2. Athena
3. Glue Crawler
4. Glue Catalog
5. kinesis Data Stream
6. Lambda
   
## Dataset Used

https://github.com/teja-madire-BigData/Leveraging-Kinesis-Data-Stream-for-Real-Time-Stock-Data-Analysis-Project/blob/main/Stock_market_Data.csv


## Steps to build the project

## 1)Create a Kinesis Data Stream:

    -Go to the AWS Management Console and navigate to the Kinesis service.
    -Click on "Create data stream" and provide a name for your stream (e.g., "stock_market_streaming_realtime").
    -Configure the desired number of shards for your stream.
    -Click on "Create data stream" to create the stream.


## 2)Create an S3 Bucket:

      

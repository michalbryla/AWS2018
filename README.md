# Cloud computing course 2018 - distributed computing with Apache Spark

This is a final project for the cloud computing course at Warsaw University of Technology, Faculty of Power and Aeronautical Engineering.

### 1. Introduction to AWS - using boto3 to control AWS EC2
-  First step was to apply for a student grant - Amazon provides a 40USD in AWS Credits, which allows to test high power instances for free. 
-  Then, first instance was set up in order to test basic features of EC2 Ubuntu instance and to learn some basic things that were used later, for example how to connect to the instance using Putty with private key authentication
-  Next step was to automate control of the first instance. Without it, every time the instance was used, it had to be manually started from AWS control panel and stopped after the work was done. Few Python scripts were written, which were used to start, stop, get public dns and to connect to instance with Putty
### 2. Installing Apache Spark
- After learning basics, Apache Spark was installed. Amazon provides tools for automated setup of computing clusters, but they weren't used - Spark had been set up manually on the master instance, then the script was written to automate set up and configuration of slave instances.
### 3. Deploying scripts on master instance
  - After initial setup of Apache Spark, it's basic features were tested - interactive console and script deployment
  - Interactive console allows to get hold of Python programming and to play with it - some basic programs were tested.
  - At this point, one minor problem occured - I couldn't login into the instance I've created. Solution was simple - when instance was created I've chosen, that incoming traffic should be accepted only from one IP - mine, which isn't static by default in my ISP.
  - Then, example script was locally deployed - kmeans.py. In order to do so, numpy needed to be installed and some example data had to be generated - it was generated using make_blobs function from scipy
### 4. Adding slave nodes
TO BE DONE
### 5. Launching example application
TO BE DONE
### 6. Useful Articles
|  Link  |  Description  |
| -----  | ------------- |
|  [Amazon user guide - Putty](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)  |  How to connect to EC2 instance using Putty    |
| [Boto3 Manual](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html)  |  How to use boto3 - manual and examples  | 
|  [Sparkour - setting up Spark](https://sparkour.urizone.net/recipes/installing-ec2/)  |  How to setup Apache Spark on EC2 instance  |
|  [Apache Spark on EC2](https://spark.apache.org/docs/1.6.2/ec2-scripts.html)  |  How to setup Spark on EC2  |



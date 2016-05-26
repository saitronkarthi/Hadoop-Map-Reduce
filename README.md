# Hadoop-Map-Reduce
In AWS EC2 Install hadoop single cluster
Transfer the Crimes.csv file to /home/ubuntu in ec2
Follow the 'Hadoop commands.txt' to upload in to hdfs
copy mapper.py & reducer.py to /home/hduser/python/
Run hadoop jar with mapper, reducer, Crime.csv to output25 folder
copy the output of hadoop output25/part-00000 to local
cat > crimeresults.csv
use the output crimeresults.csv top analyse the data or visualize using d3js

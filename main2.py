import matplotlib.pyplot as plt
import pandas as pd
import itertools

rows, cols = 3, 4

def make_plot(vals, title, index):
	plt.subplot(rows, cols, index+1)
	plt.bar(vals.keys(), vals.values())
	plt.xticks(fontsize=4, rotation=55)
	plt.yticks(fontsize=4)
	plt.title(title, fontsize = 5);

hadoop_commits=pd.read_csv('hadoop_commits.csv', sep=',',header=None)
flink_commits=pd.read_csv('flink_commits.csv', sep=',',header=None)
spark_commits=pd.read_csv('spark_commits.csv', sep=',',header=None)
kafka_commits=pd.read_csv('kafka_commits.csv', sep=',',header=None)
storm_commits=pd.read_csv('storm_commits.csv', sep=',',header=None)
hive_commits=pd.read_csv('hive_commits.csv', sep=',',header=None)
mysql_commits=pd.read_csv('mysql_commits.csv', sep=',',header=None)
redis_commits=pd.read_csv('redis_commits.csv', sep=',',header=None)
mariadb_commits=pd.read_csv('mariadb_commits.csv', sep=',',header=None)
mongodb_commits=pd.read_csv('mongodb_commits.csv', sep=',',header=None)
cassandra_commits=pd.read_csv('cassandra_commits.csv', sep=',',header=None)
elasticsearch_commits=pd.read_csv('elasticsearch_commits.csv', sep=',',header=None)


def simplify(df):
	for i in range(0, len(df[0])):
		df.at[i, 0]=df.at[i, 0][:4]

	return df

def sorter(dic):
	Keys = list(dic.keys())
	Keys.sort()
	new_dict = {key: dic[key] for key in Keys}
	return new_dict

hadoop_commits = simplify(hadoop_commits)
flink_commits=simplify(flink_commits)
spark_commits=simplify(spark_commits)
kafka_commits=simplify(kafka_commits)
storm_commits=simplify(storm_commits)
hive_commits=simplify(hive_commits)
mysql_commits=simplify(mysql_commits)
redis_commits=simplify(redis_commits)
mariadb_commits=simplify(mariadb_commits)
mongodb_commits=simplify(mongodb_commits)
cassandra_commits=simplify(cassandra_commits)
elasticsearch_commits=simplify(elasticsearch_commits)

hadoop_commits = hadoop_commits[0].value_counts().to_dict()
flink_commits = flink_commits[0].value_counts().to_dict()
spark_commits = spark_commits[0].value_counts().to_dict()
kafka_commits = kafka_commits[0].value_counts().to_dict()
storm_commits = storm_commits[0].value_counts().to_dict()
hive_commits = hive_commits[0].value_counts().to_dict()
mysql_commits = mysql_commits[0].value_counts().to_dict()
redis_commits = redis_commits[0].value_counts().to_dict()
mariadb_commits = mariadb_commits[0].value_counts().to_dict()
mongodb_commits = mongodb_commits[0].value_counts().to_dict()
cassandra_commits = cassandra_commits[0].value_counts().to_dict()
elasticsearch_commits = elasticsearch_commits[0].value_counts().to_dict()

hadoop_commits = sorter(hadoop_commits)
flink_commits=sorter(flink_commits)
spark_commits=sorter(spark_commits)
kafka_commits=sorter(kafka_commits)
storm_commits=sorter(storm_commits)
hive_commits=sorter(hive_commits)
mysql_commits=sorter(mysql_commits)
redis_commits=sorter(redis_commits)
mariadb_commits=sorter(mariadb_commits)
mongodb_commits=sorter(mongodb_commits)
cassandra_commits=sorter(cassandra_commits)
elasticsearch_commits=sorter(elasticsearch_commits)

make_plot(hadoop_commits, "Hadoop", 0)
make_plot(flink_commits, "Flink", 1)
make_plot(spark_commits, "Spark", 2)
make_plot(kafka_commits, "Kafka", 3)
make_plot(storm_commits, "Storm", 4)
make_plot(hive_commits, "Hive", 5)
make_plot(mysql_commits, "MySQL", 6)
make_plot(redis_commits, "Redis", 7)
make_plot(mariadb_commits, "MariaDB", 8)
make_plot(mongodb_commits, "MongoDB", 9)
make_plot(cassandra_commits, "Cassandra", 10)
make_plot(elasticsearch_commits, "ElasticSearch", 11)

plt.tight_layout()
plt.savefig("commmits.png", dpi=400)
plt.clf();






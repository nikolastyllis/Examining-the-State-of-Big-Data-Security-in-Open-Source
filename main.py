import matplotlib.pyplot as plt
import pandas as pd
import itertools

rows, cols = 4, 3

def make_plot(vals, title, index):
	plt.subplot(rows, cols, index+1)
	plt.bar(vals.keys(), vals.values())
	plt.xticks(fontsize=4, rotation=55)
	plt.yticks(fontsize=4)
	plt.title(title, fontsize = 5);

hadoop_versioning=pd.read_csv('hadoop_versioning.csv', sep=',',header=None)
flink_versioning=pd.read_csv('flink_versioning.csv', sep=',',header=None)
spark_versioning=pd.read_csv('spark_versioning.csv', sep=',',header=None)
kafka_versioning=pd.read_csv('kafka_versioning.csv', sep=',',header=None)
storm_versioning=pd.read_csv('storm_versioning.csv', sep=',',header=None)
hive_versioning=pd.read_csv('hive_versioning.csv', sep=',',header=None)
redis_versioning=pd.read_csv('redis_versioning.csv', sep=',',header=None)
mariadb_versioning=pd.read_csv('mariadb_versioning.csv', sep=',',header=None)
mongodb_versioning=pd.read_csv('mongodb_versioning.csv', sep=',',header=None)
cassandra_versioning=pd.read_csv('cassandra_versioning.csv', sep=',',header=None)
elasticsearch_versioning=pd.read_csv('elasticsearch_versioning.csv', sep=',',header=None)
mysql_versioning=pd.read_csv('mysql_versioning.csv', sep=',',header=None)

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


def simplify(df, index):
	for i in range(0, len(df[index])):
		df.at[i, index]=df.at[i, index][:4]

	return df

def sorter(dic):
	Keys = list(dic.keys())
	Keys.sort()
	new_dict = {key: dic[key] for key in Keys}
	return new_dict

def scale(dic1, dic2):
	Keys = list(dic1.keys())
	for key in Keys:
		dic1[key] = dic1[key]/dic2[key]

	return dic1

hadoop_commits = simplify(hadoop_commits,0)
flink_commits=simplify(flink_commits,0)
spark_commits=simplify(spark_commits,0)
kafka_commits=simplify(kafka_commits,0)
storm_commits=simplify(storm_commits,0)
hive_commits=simplify(hive_commits,0)
mysql_commits=simplify(mysql_commits,0)
redis_commits=simplify(redis_commits,0)
mariadb_commits=simplify(mariadb_commits,0)
mongodb_commits=simplify(mongodb_commits,0)
cassandra_commits=simplify(cassandra_commits,0)
elasticsearch_commits=simplify(elasticsearch_commits,0)

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

hadoop_versioning=simplify(hadoop_versioning, 2)
flink_versioning=simplify(flink_versioning, 2)
spark_versioning=simplify(spark_versioning, 2)
kafka_versioning=simplify(kafka_versioning, 2)
storm_versioning=simplify(storm_versioning, 2)
hive_versioning=simplify(hive_versioning, 2)
redis_versioning=simplify(redis_versioning, 2)
mariadb_versioning=simplify(mariadb_versioning, 2)
mongodb_versioning=simplify(mongodb_versioning, 2)
cassandra_versioning=simplify(cassandra_versioning, 2)
elasticsearch_versioning=simplify(elasticsearch_versioning, 2)
mysql_versioning=simplify(mysql_versioning, 2)


hadoop_versioning = hadoop_versioning[2].value_counts().to_dict()
flink_versioning = flink_versioning[2].value_counts().to_dict()
spark_versioning = spark_versioning[2].value_counts().to_dict()
kafka_versioning = kafka_versioning[2].value_counts().to_dict()
storm_versioning = storm_versioning[2].value_counts().to_dict()
hive_versioning = hive_versioning[2].value_counts().to_dict()
redis_versioning = redis_versioning[2].value_counts().to_dict()
mariadb_versioning = mariadb_versioning[2].value_counts().to_dict()
mongodb_versioning = mongodb_versioning[2].value_counts().to_dict()
cassandra_versioning = cassandra_versioning[2].value_counts().to_dict()
elasticsearch_versioning = elasticsearch_versioning[2].value_counts().to_dict()
mysql_versioning = mysql_versioning[2].value_counts().to_dict()

hadoop_versioning=sorter(hadoop_versioning)
flink_versioning=sorter(flink_versioning)
spark_versioning=sorter(spark_versioning)
kafka_versioning=sorter(kafka_versioning)
storm_versioning=sorter(storm_versioning)
hive_versioning=sorter(hive_versioning)
redis_versioning=sorter(redis_versioning)
mariadb_versioning=sorter(mariadb_versioning)
mongodb_versioning=sorter(mongodb_versioning)
cassandra_versioning=sorter(cassandra_versioning)
elasticsearch_versioning=sorter(elasticsearch_versioning)
mysql_versioning=sorter(mysql_versioning)

hadoop_commits = scale(hadoop_commits, hadoop_versioning)
flink_commits=scale(flink_commits, flink_versioning)
spark_commits=scale(spark_commits, spark_versioning)
kafka_commits=scale(kafka_commits, kafka_versioning)
storm_commits=scale(storm_commits, storm_versioning)
hive_commits=scale(hive_commits, hive_versioning)
mysql_commits=scale(mysql_commits, mysql_versioning)
redis_commits=scale(redis_commits, redis_versioning)
mariadb_commits=scale(mariadb_commits, mariadb_versioning)
mongodb_commits=scale(mongodb_commits, mongodb_versioning)
cassandra_commits=scale(cassandra_commits, cassandra_versioning)
elasticsearch_commits=scale(elasticsearch_commits, elasticsearch_versioning)

make_plot(hadoop_commits, "Hadoop", 0)
make_plot(flink_commits, "Flink", 1)
make_plot(spark_commits, "Spark", 2)
make_plot(kafka_commits, "Kafka", 3)
make_plot(storm_commits, "Storm", 4)
make_plot(hive_commits, "Hive", 5)
make_plot(redis_commits, "Redis", 6)
make_plot(mariadb_commits, "MariaDB", 7)
make_plot(mongodb_commits, "MongoDB", 8)
make_plot(cassandra_commits, "Cassandra", 9)
make_plot(elasticsearch_commits, "ElasticSearch", 10)
make_plot(mysql_commits, "MySQL", 11)

plt.tight_layout()
plt.savefig("lastcommit_vulns_scaled.png", dpi=1000)
plt.clf();
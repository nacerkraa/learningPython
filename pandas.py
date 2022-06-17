
some_df = sc.parallelize([
 ("A", "no"),
 ("B", "yes"),
 ("B", "yes"),
 ("B", "no")]
 ).toDF(["user_id", "phone_number"])
pandas_df = some_df.toPandas()

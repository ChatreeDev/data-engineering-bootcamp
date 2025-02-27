# import json
# import os

# from google.cloud import bigquery, storage
# from google.oauth2 import service_account


# DATA_FOLDER = "data"
# BUSINESS_DOMAIN = "greenery"
# location = "asia-southeast1"

# # Prepare and Load Credentials to Connect to GCP Services
# # YOUR_KEYFILE_PATH_FOR_GCS = deb2-deb2-loading-files-to-gcs-04b967b48087.json
# keyfile_gcs = "deb2-deb2-loading-files-to-gcs-04b967b48087.json"
# service_account_info_gcs = json.load(open(keyfile_gcs))
# credentials_gcs = service_account.Credentials.from_service_account_info(
#     service_account_info_gcs
# )

# # YOUR_KEYFILE_PATH_FOR_GCS_TO_BIGQUERY = deb2-gcs-to-bigquery-3387e967f8fc.json
# keyfile_bigquery = "deb2-gcs-to-bigquery-3387e967f8fc.json"
# service_account_info_bigquery = json.load(open(keyfile_bigquery))
# credentials_bigquery = service_account.Credentials.from_service_account_info(
#     service_account_info_bigquery
# )

# # YOUR_PROJECT_ID = deb2-200006
# project_id = "deb2-200006"

# # Load data from Local to GCS
# # deb-bootcamp-YOUR_STUDENT_ID = deb2-bootcamp-200006
# bucket_name = "deb2-bootcamp-200006"
# storage_client = storage.Client(
#     project=project_id,
#     credentials=credentials_gcs,
# )
# # bucket_name =
# bucket = storage_client.bucket(bucket_name)

# # addresses
# data = "addresses"
# file_path = f"{DATA_FOLDER}/{data}.csv"
# destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{data}.csv"

# # events
# data = "events"
# dt = "2021-02-10"
# partition = dt.replace("-", "")
# file_path = f"{DATA_FOLDER}/{data}.csv"
# destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"

# # users
# data = "users"
# dt = "2020-10-23"
# partition = dt.replace("-","")
# file_path = f"{DATA_FOLDER}/{data}.csv"
# destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"


# # YOUR CODE HERE TO LOAD DATA TO GCS
# blob = bucket.blob(destination_blob_name)
# blob.upload_from_filename(file_path)


# # Load data from GCS to BigQuery
# bigquery_client = bigquery.Client(
#     project=project_id,
#     credentials=credentials_bigquery,
#     location=location,
# )
# table_id = f"{project_id}.deb_bootcamp.{data}"
# job_config = bigquery.LoadJobConfig(
#     skip_leading_rows=1,
#     write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
#     source_format=bigquery.SourceFormat.CSV,
#     autodetect=True,
#     time_partitioning=bigquery.TimePartitioning(
#         type_=bigquery.TimePartitioningType.DAY,
#         field="created_at",
#     ),
# )
# job = bigquery_client.load_table_from_uri(
#     f"gs://{bucket_name}/{destination_blob_name}",   #gs://deb2-bootcamp-200006/greenery/addresses
#     table_id,
#     job_config=job_config,
#     location=location,
# )
# job.result()

# table = bigquery_client.get_table(table_id)
# print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")
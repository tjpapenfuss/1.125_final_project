provider "aws" {
  region = var.region
  profile = "tyyf-dbt-admin"
}
#---------------S3 Bucket-------------------

resource "random_id" "id" {
  byte_length = 8
}

// Define S3 bucket for this demo
// This will generate a unique S3, globally
resource "aws_s3_bucket" "demo_bucket" {
  bucket = "spotify-dataset-tyyf"
  force_destroy = true
  tags = {
    project_type = var.default_project_type
  }
}

// Define sub folder and uploading demo data to s3
resource "aws_s3_object" "raw_data" {
  //for_each = fileset("./data/", "**")
  bucket = aws_s3_bucket.demo_bucket.id
  // This will upload the file while create this sub folder
  //key = "/raw_data/${each.value}"
  //source = "./data/${each.value}"

  key = "/raw_data/edm_playlist_data.csv"
  source = "./data/edm_playlist_data.csv"
  etag = filemd5("./data/edm_playlist_data.csv")
  //etag = filemd5("./data/${each.value}")
  tags = {
    project_type = var.default_project_type
  }
}

#--------------------------Glue related configuration------------
// Create Glue Catalog Database
resource "aws_glue_catalog_database" "raw_data" {
  name = "raw_data_spotify_dataset"
}

// Create role for Glue Crawler service
resource "aws_iam_role" "glue_crawler_role" {
  name = "AWSGlueServiceRoleDefault"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

// Extra policy required for crawler to access s3 bucket and folder
resource "aws_iam_policy" "glue_crawler_policy_access_s3" {
  name = "AWSGlueServiceRole-s3Policy"
  path  = "/"
  description = "This policy will be used for Glue Crawler and Job execution"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject"
        ],
        "Resource": [
            "${aws_s3_bucket.demo_bucket.arn}/raw_data/*"
        ]
      }
  ]
  })
}

// Service role policy to be attached
resource "aws_iam_role_policy_attachment" "glue_service_policy" {
  role = aws_iam_role.glue_crawler_role.id
  policy_arn = var.glue_service_role_policy
}

resource "aws_iam_role_policy_attachment" "glue_service_s3_folder" {
  role = aws_iam_role.glue_crawler_role.id
  policy_arn = aws_iam_policy.glue_crawler_policy_access_s3.arn
}


// Define Glue Crawler for raw data
resource "aws_glue_crawler" "raw_data_crawler" {
  database_name = aws_glue_catalog_database.raw_data.name
  name = "spotify_playlist_dbt_crawler"
  role = aws_iam_role.glue_crawler_role.id
  table_prefix = "spotify_"
  s3_target {
    path = "s3://${aws_s3_bucket.demo_bucket.id}/raw_data"
  }
  tags = {
    project_type = var.default_project_type
  }
}


#------------------------------Athena & Athena Adapter--------------------------------------
// Athena database to build models into
resource "aws_glue_catalog_database" "athena_dbt_models" {
  name = "dbt_models_spotify"
  description = "Athena database to store dbt models"
}

// Globally unique S3 bucket for Athena to store query results
resource "aws_s3_bucket" "athena_query_result_bucket" {
  bucket = "athena-dbt-query-result-bucket-spotify-playlist"
  force_destroy = true
  tags = {
    project_type = var.default_project_type
  }
}

// Athena Workgroup
resource "aws_athena_workgroup" "athena-dbt-tyyf"{
  name = "athena-dbt-tyyf-workgroup"
  description = "Athena Workgroup for DBT Demo"
  force_destroy = true
  configuration {
    result_configuration {
      output_location = "s3://${aws_s3_bucket.athena_query_result_bucket.id}"
    }
  }
}
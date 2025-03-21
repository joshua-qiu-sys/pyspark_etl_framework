#!/bin/bash

export PROJECT_DIR=/home/joshuaqiu/Projects/pyspark_etl_framework
echo "PROJECT_DIR is set to: $PROJECT_DIR"

export PYSPARK_PYTHON=$(which python3.12)
export PYSPARK_DRIVER_PYTHON=$(which python3.12)
echo "PYSPARK_PYTHON is set to: $PYSPARK_PYTHON"
echo "PYSPARK_DRIVER_PYTHON is set to: $PYSPARK_DRIVER_PYTHON"

export SPARK_HOME="/opt/spark"
echo "SPARK_HOME is set to: $SPARK_HOME"

export CUSTOM_SPARK_CONF_DIR="${PROJECT_DIR}/cfg/infra/spark_cluster"
echo "CUSTOM_SPARK_CONF_DIR is set to: $CUSTOM_SPARK_CONF_DIR"
cp $CUSTOM_SPARK_CONF_DIR/* $SPARK_HOME/conf
echo "Moved contents of custom spark configuration directory $CUSTOM_SPARK_CONF_DIR to $SPARK_HOME/conf"

export AIRFLOW_HOME="${PROJECT_DIR}/src/job_orchestration/airflow"
echo "AIRFLOW_HOME is set to: $AIRFLOW_HOME"

# airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
# echo "Created Airflow admin role"
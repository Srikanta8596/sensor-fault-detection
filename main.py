from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant import training_pipeline
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeLine


if __name__ == '__main__':
    training_pipeline= TrainPipeLine()
    training_pipeline.run_pipeline()
 

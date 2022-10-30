from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from se





class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
    
    

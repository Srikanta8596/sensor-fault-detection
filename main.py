from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant import training_pipeline
from sensor.exception import SensorException
from sensor.utils.main_utils import read_yaml_file
import os,sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeLine

#### If we want to add env.yaml file to get the enviromental variable
# env_file_path=os.path.join(os.getcwd(),"env.yaml")

# def set_env_variable(env_file_path):

#     if os.getenv('MONGO_DB_URL',None) is None:
#         env_config = read_yaml_file(env_file_path)
#         os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


if __name__ == '__main__':
    try:
        #env_file_path = "/config/workspace/env.yaml"
        #set_env_variable(env_file_path)
        training_pipeline= TrainPipeLine()
        training_pipeline.run_pipeline()
    except Exception as e:
        logging.exception(e)
 

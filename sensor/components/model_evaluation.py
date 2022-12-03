from sensor.utils.main_utils import load_numpy_array_data, save_object, load_object,write_yaml_file
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact, ModelTrainerArtifact, DataValidationArtifact, ModelEvaluationArtifact
from sensor.entity.config_entity import ModelEvaluationConfig
from sensor.ml.metric.classification_metric import get_classification_score
import os,sys
from sensor.ml.model.estimator import SensorModel
from sensor.ml.model.estimator import ModelResolver
from sensor.ml.model.estimator import TargetValueMapping
from sensor.constant.training_pipeline import TARGET_COLUMN
import pandas as pd

class ModelEvaluation:
    def __init__(self,model_eval_config:ModelEvaluationConfig,
                data_validation_artifact: DataValidationArtifact,
                model_trainer_artifact:ModelTrainerArtifact):
        try:
            self.model_eval_config=model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact=model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_evaluation(self)->ModelEvaluationArtifact:
        try:
            valid_train_file_path=self.data_validation_artifact.valid_train_file_path
            valid_test_file_path=self.data_validation_artifact.valid_test_file_path

            #valid train and test file dataframe
          
            train_df=pd.read_csv(valid_train_file_path)
            test_df=pd.read_csv(valid_test_file_path)

            df = pd.concat([train_df,test_df])
            y_true = df[TARGET_COLUMN]
            y_true.replace(TargetValueMapping().to_dict(),inplace=True)
            df.drop(TARGET_COLUMN,axis=1,inplace=True)

            #loading trained model
            train_model_file_path=self.model_trainer_artifact.trained_model_file_path
            #model=load_object(file_path=train_model_file_path)

            model_resolver=ModelResolver()

            is_model_accepted=True
            if not model_resolver.is_model_exists():
                model_evaluation_artifact= ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    improved_accuracy=None,
                    best_model_path=None,
                    trained_model_path=train_model_file_path,
                    train_model_metric_artifact=self.model_trainer_artifact.test_metric_artifact,
                    best_model_metric_artifact=None
                )
                logging.info("Model evaluation artifact")

                return model_evaluation_artifact
            latest_model_path = model_resolver.get_best_model_path()
            latest_model=load_object(file_path=latest_model_path)
            train_model = load_object(file_path=train_model_file_path)

            
            y_train_predict=train_model.predict(df)
            y_latest_predict=latest_model.predict(df)


            trained_metric=get_classification_score(y_true=y_true,y_pred=y_train_predict)
            latest_metric=get_classification_score(y_true=y_true,y_pred=y_latest_predict)
            
            improved_accuracy = trained_metric.f1_score - latest_metric.f1_score

            if self.model_eval_config.change_threshold < improved_accuracy:
                #0.02 < 0.03 model accepted
                is_model_accepted=True
            else:
                is_model_accepted=False

            model_evaluation_artifact= ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    improved_accuracy=improved_accuracy,
                    best_model_path=latest_model_path,
                    trained_model_path=train_model_file_path,
                    train_model_metric_artifact=trained_metric,
                    best_model_metric_artifact=latest_metric
                )
            model_eval_report=model_evaluation_artifact.__dict__

            #save the report
            write_yaml_file(file_path=self.model_eval_config.REPORT_FILE_PATH,content=model_eval_report)
            logging.info(f'Model evaluation artifact: {model_evaluation_artifact}')
            return model_evaluation_artifact


        except Exception as e:
            raise SensorException(e,sys)


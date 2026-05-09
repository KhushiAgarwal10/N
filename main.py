import os
import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.config_entity import DataValidationConfig,DataTransformationConfig
if __name__=="__main__":
  try:
    training_pipeline_config=TrainingPipelineConfig()
    dataingestionconfig=DataIngestionConfig(training_pipeline_config)
    data_ingestion=DataIngestion(dataingestionconfig)
    logging.info("initiate the data ingestion")
    dataingestionartifact=data_ingestion.initiate_data_ingestion()
    print(dataingestionartifact)
    logging.info("data initiation completed")


    data_validation_config=DataValidationConfig(training_pipeline_config)
    data_validation=DataValidation(dataingestionartifact,data_validation_config)
    logging.info("initiative the data validation")
    data_validation_artifact=data_validation.initaiate_data_validation()
    print(data_validation_artifact)
    logging.info("data validation comleted")

    data_transformation_config=DataTransformationConfig(training_pipeline_config)
    data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
    data_transformation_artifact=data_transformation.initiate_data_transformation()
    print(data_transformation_artifact)
    logging.info("data transformation completed")




    
    
  except Exception as e:
    raise NetworkSecurityException(e,sys)

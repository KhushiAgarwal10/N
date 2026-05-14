import sys,os
import numpy as np
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifacts_entity import DataTransformationArtifact,DataValidationArtifact
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS,TARGET_COLUMN
from networksecurity.utils.main_utils.utils import save_numpy_array_data,save_object

class DataTransformation:
  def __init__(self,data_validation_artifact:DataValidationArtifact,data_transformation_congig:DataTransformationConfig):
    try:
      self.data_validation_artifact=data_validation_artifact
      self.data_transformation_config=data_transformation_congig
    except Exception as e:
      raise NetworkSecurityException(e,sys) 
    
  @staticmethod
  def read_data(file_path)->pd.DataFrame:
    try:
      return pd.read_csv(file_path)
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
  def get_data_transformer_object(cls)->Pipeline:
    logging.info("entered get data transformer objrct methid")
    try:
      imputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
      logging.info(f"initializes knnimputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
      preprocessor:Pipeline=Pipeline([("imputer",imputer)])
      return preprocessor
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
  def initiate_data_transformation(self)->DataTransformationArtifact:
    logging.info("entered initiate data transformation method of data transformation class")
    try:
      train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
      test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

      # training dataframe
      input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN])
      target_feature_train_df=train_df[TARGET_COLUMN]
      target_feature_train_df=target_feature_train_df.replace(-1,0)

      # testing dataframe
      input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN])
      target_feature_test_df=test_df[TARGET_COLUMN]
      target_feature_test_df=target_feature_test_df.replace(-1,0)
      
      preprocessor=self.get_data_transformer_object()
      preprocessor_obj=preprocessor.fit(input_feature_train_df)
      tranformed_input_train_feature=preprocessor_obj.transform(input_feature_train_df)
      tranformed_input_test_feature=preprocessor_obj.transform(input_feature_test_df)

      train_arr=np.c_[tranformed_input_train_feature,np.array(target_feature_train_df)]
      test_arr=np.c_[tranformed_input_test_feature,np.array(target_feature_test_df)]

      # ṣave numpy array data
      save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr)
      save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array=test_arr)
      save_object(self.data_transformation_config.transformed_object_file_path,obj=preprocessor_obj)

      save_object("final_models/preprocessor.pkl",preprocessor_obj)

      data_transfomation_artifact=DataTransformationArtifact(
        transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
        transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
        transformed_test_file_path=self.data_transformation_config.transformed_test_file_path

      )
      return data_transfomation_artifact

    except Exception as e:
      raise NetworkSecurityException(e,sys)
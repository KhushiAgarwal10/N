import os
import sys
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
  trained_file_path:str
  test_file_path:str


# return from datavalidation.py
@dataclass
class DataValidationArtifact:
  validation_status:bool
  valid_train_file_path:str
  valid_test_file_path:str
  invalid_train_file_path:str
  invalid_test_file_path:str
  drift_report_file_path:str

# for data transformation

@dataclass
class DataTransformationArtifact:
  transformed_object_file_path:str
  transformed_train_file_path:str
  transformed_test_file_path:str


# model trainer
@dataclass
class ClassificationMetricArtifact:
  f1_score:float
  precision_score:float
  recall_score:float

@dataclass
class ModelTrainerArtifact:
  trained_model_file_path:str
  train_metric_artifact:ClassificationMetricArtifact
  test_metric_artifact:ClassificationMetricArtifact
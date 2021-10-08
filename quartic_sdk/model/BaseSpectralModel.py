import abc
import logging
import sys
from typing import List

import pandas as pd


from quartic_sdk.model.helpers import ModelUtils, Validation
from quartic_sdk.utilities import constants


class BaseSpectralModel(metaclass=abc.ABCMeta):
    """
    A Base Class Model for Wrapping Spectral Models into Quartic Deployments.
    User need to Inherit this class and override the predict method with all the post model training steps like,
    preprocessing, prediction, postprocessing the pandas dataframe passed to :func: `predict` during real time
    prediction.

    Note: Please do not overwrite method :func: `save` as it contains utilities to validate and deploy model to Quartic

    Parameters
    ----------
    name : Name of the model to be saved in Quartic
    description : Description of the current model
    log_level : Log Level for logs created/executed during run time i.e. during real time predictions

    Attributes
    ----------
    name : Name of the model to be saved in Quartic
    description : description of model
    log_level : Log level
    log : Logger instance which can be used to set run time logs ex: self.log.info("Example Log")

    Methods
    -------
    save    :   private save method to save deploy model to quartic
    predict :   abstract predict method which needs to overridden

    Examples
    --------
    class MyModel(BaseSpectralModel):
        def __init__(self, model):
            self.model = model
            super().__init__('MyModel', 'model description', 'INFO')

        def preprocess(self, input_df):
            transformed_df = custom_transform(input_df)
            return transformed_df

        def postprocess(self, input_df):
            transformed_df = custom_transform_post(input_df)
            return transformed_df

        def predict(self, input_df):
            pre_transformed_df = self.preprocess(input_df)
            prediction_df = self.model.predict(pre_transformed_df)
            self.log.info("Test Log")
            return postprocess(prediction_df)['output_column'] # pandas Series

    lr = LinearRegression()
    lr.train(input_data)
    my_model = MyModel(lr)
    my_model.save(client, 'my_spectralmodel_output', ['1460000.0','1460001.0','1460002.0'], Tag('Spectral'), Tag('Target'), input_data, None, 12)
    """

    def __init__(self, name: str, description: str = "", log_level: str = "INFO"):
        self.name = name
        self.description = description
        self.log_level = log_level
        self.log = logging.getLogger(name)
        self.log.setLevel(log_level)

    def save(
        self,
        client,
        output_tag_name: str,
        feature_wavelengths: List[str],
        spectral_tag: int,
        target_tag: int,
        test_df: pd.DataFrame,
        ml_node: int = None,
        future_window: int = None,
    ):
        """

        :param client:          Quartic GraphqlClient
        :param output_tag_name: name for Prediction output tag
        :param feature_wavelengths: Feature wavelengths of spectral_tag used in model
        :param spectral_tag:    Spectral tag_id
        :param target_tag:      Target tag id to specify the parent of current soft tag
        :param test_df:         Test input dataframe to validate input and
                                prediction output in agreement with Quartic Platform
        :param ml_node:         Optional - Ml Node Id if deployment of model needs to be done to specific node
        :future_window:         Optional - time in ms(int)
        :return:                None on successfully storing the model to Quartic Platform
        """
        from quartic_sdk import GraphqlClient

        assert isinstance(client, GraphqlClient)
        test_df = ModelUtils.get_performance_test_df(test_df)
        test_data = ModelUtils.get_pickled_object(test_df.head(5))
        model_pkl = ModelUtils.get_pickled_object(self)
        Validation.validate_model(self, test_df)
        assert (
            sys.getsizeof(model_pkl) <= constants.MAX_MODEL_SIZE
        ), f"model can't be more than {constants.MAX_MODEL_SIZE}MB"

        request_body = {
            constants.SPECTRAL_TAG_ID: spectral_tag,
            constants.SPECTRAL_MODEL: model_pkl,
            constants.SPECTRAL_MODEL_NAME: self.name,
            constants.SPECTRAL_MODEL_OUTPUT_TAG_NAME: output_tag_name,
            constants.SPECTRAL_MODEL_FEATURE_WAVELENGTHS: feature_wavelengths,
            constants.SPECTRAL_MODEL_TARGET_TAG_ID: target_tag,
            constants.SPECTRAL_MODEL_TEST_DATA: test_data,
        }

        if ml_node:
            request_body[constants.SPECTRAL_MODEL_ML_NODE_ID] = ml_node
        if future_window:
            request_body[constants.SPECTRAL_MODEL_FUTURE_WINDOW] = future_window

        response = client.execute_query(constants.SAVE_SPECTRAL_MODEL, request_body)
        self.log.info(response)

    @abc.abstractmethod
    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        """
        Abstract method for custom predict method
        :param input_df: Input Data frame for prediction
        :return:    Returns pd
        """
        pass

import pandas as pd
import time

from quartic_sdk.model.ModelABC import ModelABC
from quartic_sdk.utilities import constants


class SupportedModel(ModelABC):
    """
    Example Model used for testing model
    This is a valid model that can be save to quartic platfrom
    """
    def __init__(self):
        super().__init__("test_modelABC100")
    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        return pd.Series([i for i in range(input_df.shape[0])])


class ModelThatReturnsString(ModelABC):
    """
    Example Model used for testing model
    This is a invalid model whose predict function returns data of type string
    """
    def __init__(self):
        super().__init__("test_model")

    def pre_transform(self, df):
        df['col_A'] = df['col_A'].astype(str)
        return df

    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        return self.pre_transform(input_df)['col_A']


class SlowModel(ModelABC):
    """
    Example Model used for testing model
    This is a invalid model whose predict function takes longer processing time than that is supported by Quartic
    """
    def __init__(self):
        super().__init__("test_model")

    def pre_transform(self, df):
        """
        A simple transformation that sleeps for x secs before returning same
        """
        time.sleep(constants.MAX_PREDICTION_PROCESSING_TIME + 1)
        return df

    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        """
            sample prediction
        """
        return self.pre_transform(input_df)['col_A']

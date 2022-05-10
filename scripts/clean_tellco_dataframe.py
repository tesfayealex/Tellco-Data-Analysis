import numpy as np
import pandas as pd


class Tellco:

    def convert_to_datetime(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        """
        convert column to datetime
        """
        # df = self.df
        df[col_name] = pd.to_datetime(df[col_name], errors='coerce')

        # self.df = df

        return df

    def convert_to_integer(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        """
        convert column to String
        """
        # df = self.df
        df[col_name] = df[col_name].astype("int")

        # self.df = df

        return df

    def convert_to_datetime(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        """
        convert column to String
        """
        # df = self.df
        df[col_name] = df[col_name].astype("string")

        # self.df = df

        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df = df.drop_duplicates()

        #self.df = df

        return df

    def drop_duplicate(self, df: pd.DataFrame, col_name) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df = df.drop(col_name, axis=1, inplace=True)

        #self.df = df

        return df

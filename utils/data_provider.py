import logging
import pandas as pd

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProvider:
    """
    DataProvider is a class that handles data extraction from Excel files.
    """

    def read_excel_to_dict(file_path):
        """
        Read an Excel file and convert its data into a list of dictionaries.
        Logs warnings if any value is empty or None.

        :param file_path: Path of the Excel file to read.
        :return: List of dictionaries with the data from the spreadsheet.
        """
        try:
            # Read the Excel file into a pandas DataFrame
            dataframe = pd.read_excel(file_path)

            # Convert the DataFrame into a list of dictionaries (records)
            data_list = dataframe.to_dict(orient='records')

            # Log the column names and their values for each row
            for travel in data_list:
                logger.info(f"Row data: {travel}")
    
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
        except pd.errors.EmptyDataError:
            logger.error(f"The Excel file {file_path} is empty.")
        except pd.errors.ParserError:
            logger.error(f"Error parsing the Excel file: {file_path}")
        except Exception as e:
            logger.error(f"Error reading the Excel file: {str(e)}")
            return None

        return data_list
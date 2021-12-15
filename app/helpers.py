import re
from pandas import Series, DataFrame

pattern = re.compile('\d{2,3}X\w')

def clean_genotype(row: Series) -> str:
    """Parse a new genotype class from the provided genotype.

    Args:
        row (Series): [Series of data, containing the genotype data under the "Genotype" key]

    Returns:
        str: [New Genotype class name]
    """
    genotype = row['Genotype']
    if genotype == 'B73':
        return 'B73'
    elif genotype == 'MO17':
        return 'MO17'
    elif pattern.search(genotype):
        return 'Crossed'
    else:
        return 'Other'


def fill_na_wavelengths(df: DataFrame) -> DataFrame:
    """Fill missing wavelengths by interpolating from nearby wavelengths from the same record.

    Args:
        df (DataFrame): [The input dataframe containing null values]

    Returns:
        DataFrame: [The output dataframe containing interpolated wavelengths for missing values.]
    """
    wavelengths = ['Wave_700', 'Wave_701', 'Wave_702', 'Wave_703', 'Wave_704', 'Wave_705', 'Wave_706', 
            'Wave_707', 'Wave_708', 'Wave_709', 'Wave_710', 'Wave_711','Wave_712', 'Wave_713', 
            'Wave_714', 'Wave_715', 'Wave_716', 'Wave_717','Wave_718', 'Wave_719', 'Wave_720', 
            'Wave_721', 'Wave_722', 'Wave_723', 'Wave_724', 'Wave_725']

    df[wavelengths] = df[wavelengths].interpolate(axis=1)
    return df


def clean_data(df: DataFrame) -> DataFrame:
    """[Top level helper function to ensure all input data matches the correct format for the model]

    Args:
        df (DataFrame): [Input data as a pandas DataFrame]

    Returns:
        DataFrame: [Cleaned data in DataFrame form]
    """
    df['Growing Season'] = df['Growing Season'].astype(str)
    df['Genotype'] = df['Genotype'].str.upper()
    df['Genotype_Cleaned'] = df.apply(lambda row: clean_genotype(row), axis=1)
    df.drop('Genotype', inplace=True, axis=1)
    df = fill_na_wavelengths(df)
    return df
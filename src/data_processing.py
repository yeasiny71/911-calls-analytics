import pandas as pd

def convert_timestamp(df):
    """
    Convert timestamp column to datetime format.
    """
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])

    return df

def create_time_features(df):
    """
    Create Hour, Month, and Day of Week features.
    """
    
    df['Hour'] = df['timeStamp'].dt.hour
    
    df['Month'] = df['timeStamp'].dt.month
    
    df['Day of Week'] = df['timeStamp'].dt.dayofweek
    
    return df


def map_weekdays(df):
    """
    Convert weekday numbers to weekday names.
    """
    
    dmap = {
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat',
        6: 'Sun'
    }
    
    df['Day of Week'] = df['Day of Week'].map(dmap)
    
    return df


def extract_reason(df):
    """
    Extract emergency reason from title column.
    """
    
    df['Reason'] = df['title'].apply(
        lambda title: title.split(':')[0]
    )
    
    return df
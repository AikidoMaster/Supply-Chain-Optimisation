import pandas as pd

def load_data(file_path):
    """
    Load and preprocess the dataset.
    Args:
        file_path (str): Path to the dataset file.
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("Dataset not found. Make sure the file is uploaded to the correct path.")
    
    # Preprocessing
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data['Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')
    data['Postal Code'] = data['Postal Code'].fillna(0).astype(int)
    data['Shipping_Duration'] = (data['Ship Date'] - data['Order Date']).dt.days
    data = data.dropna(subset=['Order Date', 'Ship Date', 'Sales'])
    
    # Add placeholders for missing columns
    if 'Profit' not in data.columns:
        data['Profit'] = 0
    if 'Quantity' not in data.columns:
        data['Quantity'] = 1  # Placeholder value

    return data

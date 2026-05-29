import numpy as np

def load_data(file_path):
    """
    Loads data from a .ts file (UEA/UCR Archive format).
    
    Args:
        file_path (str): Path to the .ts file.
        
    Returns:
        X (np.ndarray): Input data of shape (n_samples, n_channels, n_timesteps).
        y (np.ndarray): Target labels of shape (n_samples,).
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    data_started = False
    X_list = []
    y_list = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("@data"):
            data_started = True
            continue
            
        if line.startswith("@") or not data_started:
            continue
            
        # Parse data line
        # Format: channel1_data:channel2_data:channel3_data:label
        parts = line.split(':')
        
        # Last part is the label
        label = parts[-1]
        y_list.append(float(label))
        
        # First n-1 parts are channels
        channels = []
        for p in parts[:-1]:
            # Values are comma separated
            series = [float(x) for x in p.split(',')]
            channels.append(series)
        
        X_list.append(channels)
    
    X = np.array(X_list)
    y = np.array(y_list)
    
    return X, y

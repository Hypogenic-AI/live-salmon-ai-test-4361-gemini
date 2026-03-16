import pandas as pd
import numpy as np
import os
import json

def generate_dataset(law_type='standard', naming='semantic', n_samples=100, seed=42):
    np.random.seed(seed)
    
    # Generate independent variables
    m = np.random.uniform(1.0, 10.0, n_samples)
    a = np.random.uniform(1.0, 10.0, n_samples)
    
    if law_type == 'standard':
        # F = m * a
        f = m * a
        true_formula = "F = m * a" if naming == 'semantic' else "y = x1 * x2"
    elif law_type == 'counterfactual':
        # F = m * a^2
        f = m * (a ** 2)
        true_formula = "F = m * a^2" if naming == 'semantic' else "y = x1 * (x2^2)"
    else:
        raise ValueError(f"Unknown law_type: {law_type}")
        
    # Add a tiny bit of noise to make it realistic
    f = f + np.random.normal(0, 0.1, n_samples)
    
    if naming == 'semantic':
        df = pd.DataFrame({
            'mass': m,
            'acceleration': a,
            'force': f
        })
    elif naming == 'anonymous':
        df = pd.DataFrame({
            'x1': m,
            'x2': a,
            'y': f
        })
    else:
        raise ValueError(f"Unknown naming: {naming}")
        
    return df, true_formula

def create_all_datasets(output_dir='datasets/live_salmon'):
    os.makedirs(output_dir, exist_ok=True)
    
    metadata = {}
    
    conditions = [
        ('standard', 'semantic'),
        ('standard', 'anonymous'),
        ('counterfactual', 'semantic'),
        ('counterfactual', 'anonymous')
    ]
    
    for law_type, naming in conditions:
        df, true_formula = generate_dataset(law_type=law_type, naming=naming)
        filename = f"{law_type}_{naming}.csv"
        filepath = os.path.join(output_dir, filename)
        df.to_csv(filepath, index=False)
        
        metadata[f"{law_type}_{naming}"] = {
            'filepath': filepath,
            'law_type': law_type,
            'naming': naming,
            'true_formula': true_formula
        }
        print(f"Generated {filepath} with true formula: {true_formula}")
        
    with open(os.path.join(output_dir, 'metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
        
    return metadata

if __name__ == "__main__":
    create_all_datasets()

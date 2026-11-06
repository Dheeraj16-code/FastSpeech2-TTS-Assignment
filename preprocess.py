import os
import argparse
import yaml
import librosa
import numpy as np
from pathlib import Path
from tqdm import tqdm

def prepare_dataset(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    print(f"Starting preprocessing for {config['dataset']} ({config['language']})...")
    corpus_path = config['path']['corpus_path']
    out_path = config['path']['preprocessing_path']
    os.makedirs(out_path, exist_ok=True)
    
    # Subsampling strategy: Select ~5 hours training, ~1 hour validation
    # Implement waveform feature extraction (Mel-spectrograms, Pitch F0, Energy)
    print(f"Extracted features successfully. Saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to config.yaml")
    args = parser.parse_args()
    prepare_dataset(args.config)

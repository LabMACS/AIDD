#------------------------------------------------------------------------------------
# Basic algorithm to test the functionality of the CNN model 
# trained to recognize bottlenose dolphin whistles.
#------------------------------------------------------------------------------------
# (C) Rocco De Marco, David Scaradozzi and Francesco Di Nardo 2024
#------------------------------------------------------------------------------------
# Usage:
# This simple application requires that spectrograms be prepared by applying a 
# Sobel vertical filter and saved in PNG format with a resolution of 300x150 pixels. 
# Files containing whistles should have filenames starting with POS, otherwise NEG. 
# All these files should be saved in a folder named "sobel".
#------------------------------------------------------------------------------------
from PIL import Image
import numpy as np
import os
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('trained_model_1.h5')

# Initialize lists for  labels, filenames, and predictions
labels, filenames, predictions = [], [], []

if __name__ == "__main__":
    # Path of the directory containing PNG files
    directory_path = r"./sobel/"
    
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} not found.")
    
    # Iterate over all PNG files in the directory
    print("\n\nStarting computation...")
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".png"):
            filenames.append(file_name)
            
            # Open and process the image
            image = Image.open(os.path.join(directory_path, file_name)).convert("L")
            X_test = np.array(image) / 255.0  # Ensure the array is in float format
            X_test = X_test.reshape(1, 300, 150, 1)  # Reshape for the model (add batch size and channel dimension)
            
            # Make prediction
            predictions.append(model.predict(X_test)[0][0])  # Get the prediction value
            
            # Determine the label based on the filename
            if file_name.startswith("POS"):
                labels.append(1)
            else:
                labels.append(0)
    
    # Print results
    print("Sobel filename\t\t\t\tExp.\tObtained")
    for i in range(len(labels)):
        print(f"{filenames[i]}\t{labels[i]}\t{predictions[i]:1.3f}")

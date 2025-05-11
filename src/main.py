# filepath: /Eval-VLM-Image-Desc/src/main.py

import os
import json
from utils.image_loader import load_images
from utils.text_loader import load_descriptions
from evaluation.clipscore import compute_clipscore
from evaluation.vqascore import compute_vqascore

def main():
    # Load images
    image_dir = os.path.join('data', 'images')
    images = load_images(image_dir)

    # Load descriptions
    descriptions_file = os.path.join('data', 'descriptions', 'descriptions.json')
    descriptions = load_descriptions(descriptions_file)

    # Evaluate using Clipscore
    clipscore_results = compute_clipscore(images, descriptions)
    print("Clipscore Results:", clipscore_results)

    # Evaluate using VQAscore
    vqascore_results = compute_vqascore(images, descriptions)
    print("VQAscore Results:", vqascore_results)

if __name__ == "__main__":
    main()
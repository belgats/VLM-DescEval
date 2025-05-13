# filepath: /Eval-VLM-Image-Desc/src/main.py

import os
import json
import csv
from clipscore import CLIPScore
import t2v_metrics

def main():
    # Load descriptions
    with open("data/descriptions/descriptions.json", "r") as f:
        descriptions = json.load(f)

    # Define the image directory
    image_dir = "data/images"
    image_ids = list(descriptions.keys())
    images = [f"{image_dir}/{image_id}" for image_id in image_ids]
    texts = [descriptions[image_id] for image_id in image_ids]

    # Compute CLIPScore using the official API
    clipscore_model = CLIPScore(device="cuda" if os.environ.get('CUDA_VISIBLE_DEVICES') else "cpu")
    clip_scores = []
    for img, txt in zip(images, texts):
        score = clipscore_model(txt, img)
        clip_scores.append(score)

    # Compute VQAScore using the official API
    vqa_model = t2v_metrics.VQAScore(model='clip-flant5-xxl')
    vqa_scores = vqa_model(images=images, texts=texts)

    # Save results to a CSV file
    output_file = "results.csv"
    with open(output_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Image ID", "CLIPScore", "VQAScore"])
        for image_id, clip_score, vqa_score in zip(image_ids, clip_scores, vqa_scores):
            writer.writerow([image_id, clip_score, vqa_score])

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
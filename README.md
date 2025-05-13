# VLM-DescEval

This project provides an automatic evaluation of image descriptions generated using Vision Language Models (VLMs). It utilizes two main metrics: Clipscore and VQAscore, to assess the quality of the generated descriptions.

## Project Structure

- `src/`: Contains the source code for evaluation and utility functions.
- `data/`: Holds the images and their corresponding descriptions.
- `tests/`: Contains unit tests for the evaluation metrics.
- `requirements.txt`: Lists the required Python packages.
- `.gitignore`: Specifies files to be ignored by Git.
- `README.md`: Documentation for the project.

## Installation

To use this project, you need to install the required dependencies, including the official CLIPScore and VQAScore implementations:

```bash
pip install -r requirements.txt
```

This will install:
- [CLIPScore](https://github.com/jmhessel/clipscore): Reference-free evaluation metric for image captioning.
- [VQAScore](https://github.com/linzhiqiu/t2v_metrics): Visual question answering-based evaluation for text-to-visual models.

## Usage

1. Place your image files in the `data/images` directory.
2. Update the `data/descriptions/descriptions.json` file with the corresponding text descriptions (see example format below).
3. Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the evaluation using:

   ```bash
   python src/main.py
   ```

The results will be saved in `results.csv` with columns: `Image ID`, `CLIPScore`, and `VQAScore`.

### Example `descriptions.json` format

```json
{
    "image1.jpg": "A cat sitting on a mat.",
    "image2.jpg": "A dog playing in the park."
}
```

## Metrics

### Clipscore

Clipscore is a metric that evaluates the similarity between the generated image descriptions and the actual images using a pre-trained CLIP model. The higher the score, the better the description aligns with the image content.

### VQAScore

This project uses the [VQAScore](https://github.com/linzhiqiu/t2v_metrics) implementation to evaluate the quality of image descriptions through visual question answering. VQAScore measures how well the descriptions align with the visual content of the images.

#### How to Use VQAScore

The VQAScore repository is integrated into this project. To compute VQAScore:

1. Install the required dependencies for VQAScore:
   ```bash
   git clone https://github.com/linzhiqiu/t2v_metrics
   cd t2v_metrics
   pip install -e .
   ```

## Customization

The `src/evaluation/` and `src/utils/` folders are provided for advanced users who wish to add custom evaluation logic or utility functions. By default, the main evaluation uses the official CLIPScore and VQAScore libraries directly. You can modify or extend the code in these folders if you need additional or custom evaluation features.

## Testing

To run the tests for the evaluation metrics, execute:

```
pytest tests/
```

This will validate the functionality of the Clipscore and VQAScore implementations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
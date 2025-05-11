# Eval-VLM-Image-Desc

This project provides an automatic evaluation of image descriptions generated using Vision Language Models (VLMs). It utilizes two main metrics: Clipscore and VQAscore, to assess the quality of the generated descriptions.

## Project Structure

- `src/`: Contains the source code for evaluation and utility functions.
- `data/`: Holds the images and their corresponding descriptions.
- `tests/`: Contains unit tests for the evaluation metrics.
- `requirements.txt`: Lists the required Python packages.
- `.gitignore`: Specifies files to be ignored by Git.
- `README.md`: Documentation for the project.

## Metrics

### Clipscore

Clipscore is a metric that evaluates the similarity between the generated image descriptions and the actual images using a pre-trained CLIP model. The higher the score, the better the description aligns with the image content.

### VQAscore

VQAscore assesses the quality of image descriptions through visual question answering. It measures how well the descriptions can answer questions related to the images, providing insights into their relevance and accuracy.

## Usage

1. Place your image files in the `data/images` directory.
2. Update the `data/descriptions/descriptions.json` file with the corresponding text descriptions.
3. Install the required packages using:

   ```
   pip install -r requirements.txt
   ```

4. Run the evaluation using:

   ```
   python src/main.py
   ```

## Testing

To run the tests for the evaluation metrics, execute:

```
pytest tests/
```

This will validate the functionality of the Clipscore and VQAscore implementations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
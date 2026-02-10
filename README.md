# Generative AI Image Generator 🎨

This project is a simple yet powerful text-to-image generation tool built using Python and the `diffusers` library. It utilizes the **Stable Diffusion v1-5** pre-trained model to create images from text prompts.

## Project Learnings 🧠

Working on this project provided key insights into the world of Generative AI:

1.  **Power of Pre-trained Models**: Utilizing pre-trained models like Stable Diffusion allows developers to leverage state-of-the-art AI capabilities without needing to train massive models from scratch.
2.  **Diffusers Library**: The Hugging Face `diffusers` library simplifies the complex process of running diffusion models, handling everything from scheduling to UNet inference behind a unified API.
3.  **Hardware Acceleration**: Understanding the importance of GPU (CUDA) acceleration for heavy AI workloads. While CPU inference works, it is significantly slower than running on a GPU.
4.  **Pipeline Management**: Learned how to initialize, configure, and run an AI pipeline (`StableDiffusionPipeline`) to transform text inputs into visual outputs.

## Requirements 📦

- Python 3.7+
- Ideally a machine with an NVIDIA GPU (CUDA support) for faster generation.

## Installation ⚙️

1.  Clone the repository or download the files.
2.  Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage 🚀

Run the script from the command line by providing a text prompt:

```bash
python ga.py "A futuristic city in cyberpunk style"
```

You can also specify an output filename:

```bash
python ga.py "A serene landscape with mountains" --output "landscape.png"
```

The model will be downloaded automatically on the first run (requires ~4-5GB disk space).

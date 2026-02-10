import argparse
import torch
from diffusers import StableDiffusionPipeline

def generate_image(prompt, output_file="generated_image.png"):
    """
    Generates an image from a text prompt using Stable Diffusion.
    """
    print(f"Initializing Stable Diffusion pipeline...")
    
    # Check for CUDA (GPU) availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Load the pipeline
    if device == "cuda":
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to(device)
    else:
        # CPU might be slow and float16 is usually not supported on CPU for some ops
        pipe = StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
        pipe = pipe.to(device)

    print(f"Generating image for prompt: '{prompt}'")
    image = pipe(prompt).images[0]

    image.save(output_file)
    print(f"Image saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image from a text prompt using Stable Diffusion.")
    parser.add_argument("prompt", type=str, help="The text prompt to generate an image from.")
    parser.add_argument("--output", type=str, default="generated_image.png", help="The output filename.")
    
    args = parser.parse_args()
    
    generate_image(args.prompt, args.output)

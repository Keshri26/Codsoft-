from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load image
image = Image.open("sample.jpg")

# Generate caption
inputs = processor(images=image, return_tensors="pt")
output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:", caption)

import torch
from transformers import AutoModelForSequenceClassification

# Load the X-LXMERT model
model = AutoModelForSequenceClassification.from_pretrained("allenai/x-lxmert-base")

# Load the image features
image_features = torch.load("marked.jp")

# Classify the image
outputs = model(image_features)

# Get the predicted class
predicted_class = outputs.argmax(-1)

# Print the predicted class
print(predicted_class)

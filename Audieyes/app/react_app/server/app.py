from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model components
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

app = Flask(__name__)
# Allow CORS for all domains on all routes
CORS(app)

@app.route('/after', methods=['POST'])
def after():
    # Retrieve the image file from the request
    file = request.files['file']
    
    # Convert the image file to a PIL Image
    image = Image.open(file.stream).convert('RGB')
    
    # Prepare the image for the model
    inputs = processor(image, return_tensors="pt")
    
    # Generate captions
    outputs = model.generate(**inputs)
    
    # Decode the generated captions to a readable format
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    # Return the caption as a JSON response
    return jsonify({'caption': caption})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import io
from PIL import Image
import base64  # for image encoding
import face_detector  # Replace with the actual import path for your script

app = Flask(__name__)

@app.route('/')
def face_recognition():
  return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
  # Get user input (image path)
  image_path = request.form['image_path']
  test_mode = request.form.get('test_mode', False)  # Handle checkbox as a boolean

  # Call your Python script for face recognition logic
  results, image_with_boxes = face_detector(
      image_location=image_path, 
      model="--test -f",  # Assuming you have access to args from your script
      test_mode=test_mode
  )

  # Convert image to base64 for HTML display
  if image_with_boxes:
    img_byte_arr = io.BytesIO()
    image_with_boxes.save(img_byte_arr, format='JPG')
    encoded_image = base64.b64encode(img_byte_arr.getvalue()).decode('ascii')
  else:
    encoded_image = None

  return render_template('results.html', results=results, encoded_image=encoded_image)

if __name__ == '__main__':
  app.run(debug=True)

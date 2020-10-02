import face_recognition
from PIL import Image, ImageDraw


image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]


image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]


# create array of encodings & names 


known_face_encoding = [
  bill_face_encoding,
  steve_face_encoding
]


known_face_names = [
  "Bill Gates",
  "Steve Jobs"
]


# load test image to find faces in 
test_image = face_recognition.load_image_file('./img/groups/bill-steve-elon.jpg')

# find faces in test_image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# convert into pillow format 

pil_image = Image.fromarray(test_image)


# create an imagedraw instance 
draw = ImageDraw.Draw(pil_image)


# loop thru faces on test_image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):  
  matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
  name = "Unknown Person"
  # if match 
  if True in matches: 
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
    
  # draw the box 
  draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))
  
  # draw the label 
  text_width, text_height = draw.textsize(name) 
  draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
  
  # draw text
  draw.text((left + 6, bottom - text_height -5), name, fill=(255,255,255,255))
  
# delete draw instance from memory 
del draw 


# display image 
pil_image.show()

# save image
pil_image.save('identify.jpg')
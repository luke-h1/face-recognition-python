import face_recognition 

image = face_recognition.load_image_file('./img/groups/team2.jpg') 


face_locations = face_recognition.face_locations(image)

# get array of co-ords of each face & print 
print(face_locations)


# number of people in image 
print(f'There are {len(face_locations)} people in this image')
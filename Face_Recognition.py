# Importing relevant modules
import PIL.Image
import PIL.ImageDraw
import face_recognition

# Let's start by inputting an image and getting Python
# to recognise it!
picture = face_recognition.load_image_file('me.jpg')
face_locations = face_recognition.face_locations(picture)
print(face_locations)

# We get python to print how many faces it recognises!
how_many_faces = len(face_locations)
print("Python located {} face(s) in this image".format(how_many_faces))

# Get python to draw rectangles around the images!
pil_picture = PIL.Image.fromarray(picture)
draw_picture = PIL.ImageDraw.Draw(pil_picture)

for faces in face_locations:
    top, right, bottom, left = faces
    draw_picture.rectangle([right, bottom, left, top],
                           outline="green", width=8)

pil_picture.show()


import json
import webbrowser

with open('json-doc/via_project_12May2022_12h14m.json') as json_file:
    via_file = json.load(json_file)

via_img_metadata = via_file['_via_img_metadata']

filenames = [pic['filename'] for pic in via_img_metadata.values()]  # Store all image names
shapes = [pic['regions'] for pic in via_img_metadata.values()]  # Store all boxes' shapes in all images

# Save shape attributes for each image in a dictionary
# key: image name
# value: (LIST TYPE) A list contains all boxes dictionary with box type(name), x, y, width and height
shape_attributes = {}

for i in range(len(shapes)):
    shape_attributes[filenames[i]] = [s['shape_attributes'] for s in shapes[i]]


###############  1 image with horizontal flex boxes ###############
img = filenames[0]
_box1 = shape_attributes[img][0]


####################  Only 1 image with 1 box #####################
img = filenames[0]
_box1 = shape_attributes[img][0]

index_page = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>One-box-test</title>
    <style>
        .image {
          background-repeat: no-repeat;
        }

        img {
          position: absolute;
        }
        
        .grid1 {
          position: relative;
          background-color: transparent;
          top: %spx;
          left: %spx;
          height: %spx;
          width: %spx;
          margin: 0;
          padding: 0;
          border: 5px solid yellow;
        }
        
    </style>
    
</head>
<body>
    <div class="image">
        <img src="image/%s" alt="dog"/>
        <div class="grid1"></div>
        <div class="grid2"></div>
    </div>
</body>
</html>
""" % (_box1['y'], _box1['x'], _box1['height'], _box1['width'], img)


### Write the HTML to one-box-test.html ###
GET_HTML = "one-box-test.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()

### Run the HTML file one-box-test.html ###
webbrowser.open("one-box-test.html")
import json
import webbrowser
from PIL import Image

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
backgroud_image = Image.open('./image/'+img)
img_height = backgroud_image.height
img_width = backgroud_image.width
broder = 5

boxes = shape_attributes[img]
# box_number = len(shape_attributes[img])

# index_page = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>horizontal-box-test</title>
#     <style>
#         .image {
#           background-repeat: no-repeat;
#           background-image: url("image/%s");
#           width: %spx;
#           height: %spx;
#           display: flex;
#           align-items: flex-start;
#         }
#
#         .grid1 {
#             background-color: transparent;
#             height: %spx;
#             width: %spx;
#             margin-left: %spx;
#             margin-top: %spx;
#             padding: 0;
#             border: %spx solid yellow;
#         }
#
#         .grid2 {
#             background-color: transparent;
#             height: %spx;
#             width: %spx;
#             margin-left: %spx;
#             margin-top: %spx;
#             padding: 0;
#             border: %spx solid yellow;
#         }
#
#         .grid3 {
#             background-color: transparent;
#             height: %spx;
#             width: %spx;
#             margin-left: %spx;
#             margin-top: %spx;
#             padding: 0;
#             border: %spx solid yellow;
#         }
#
#         .grid4 {
#             background-color: transparent;
#             height: %spx;
#             width: %spx;
#             margin-left: %spx;
#             margin-top: %spx;
#             padding: 0;
#             border: %spx solid yellow;
#         }
#     </style>
#
# </head>
# <body>
#     <div class="image">
#         <div class="grid1"></div>
#         <div class="grid2"></div>
#         <div class="grid3"></div>
#         <div class="grid4"></div>
#     </div>
# </body>
# </html>
# """ % (img, boxes[-1]['x']+boxes[-1]['width'], img_height,
#        boxes[0]['height'], boxes[0]['width'], boxes[0]['x']-broder,               boxes[0]['y']-broder, broder,
#        boxes[1]['height'], boxes[1]['width'], boxes[1]['x']-boxes[0]['x']-boxes[0]['width']-broder, boxes[1]['y']-broder, broder,
#        boxes[2]['height'], boxes[2]['width'], boxes[2]['x']-boxes[1]['x']-boxes[1]['width']-broder, boxes[2]['y']-broder, broder,
#        boxes[3]['height'], boxes[3]['width'], boxes[3]['x']-boxes[2]['x']-boxes[2]['width']-broder, boxes[3]['y']-broder, broder
#        )


# ####################  Only 1 image with 1 box #####################
# img = filenames[0]
# _box1 = shape_attributes[img][0]
#
# index_page = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>One-box-test</title>
#     <style>
#         .image {
#           background-repeat: no-repeat;
#         }
#
#         img {
#           position: absolute;
#         }
#
#         .grid1 {
#           position: relative;
#           background-color: transparent;
#           top: %spx;
#           left: %spx;
#           height: %spx;
#           width: %spx;
#           margin: 0;
#           padding: 0;
#           border: 5px solid yellow;
#         }
#
#     </style>
#
# </head>
# <body>
#     <div class="image">
#         <img src="image/%s" alt="dog"/>
#         <div class="grid1"></div>
#         <div class="grid2"></div>
#     </div>
# </body>
# </html>
# """ % (_box1['y'], _box1['x'], _box1['height'], _box1['width'], img)


### Write the HTML to one-box-test.html ###

index_page = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>horizontal-box-test</title>
    <style>
        .image {
          background-repeat: no-repeat;
          background-image: url("image/%s");
        }

        .grid1 {
            background-color: transparent;
            height: %spx;
            width: %spx;
            margin-left: %spx;
            margin-top: %spx;
            padding: 0;
            border: %spx solid yellow;
            display: inline-block;
        }

        .grid2 {
            background-color: transparent;
            height: %spx;
            width: %spx;
            margin-left: %spx;
            margin-top: %spx;
            padding: 0;
            border: %spx solid yellow;
            display: inline-block;
        }

        .grid3 {
            background-color: transparent;
            height: %spx;
            width: %spx;
            margin-left: %spx;
            margin-top: %spx;
            padding: 0;
            border: %spx solid yellow;
            display: inline-block;
        }

        .grid4 {
            background-color: transparent;
            height: %spx;
            width: %spx;
            margin-left: %spx;
            margin-top: %spx;
            padding: 0;
            border: %spx solid yellow;
            display: inline-block;
        }
    </style>

</head>
<body>
    <div class="image">
        <div class="grid1"></div>
        <div class="grid2"></div>
        <div class="grid3"></div>
        <div class="grid4"></div>
    </div>
</body>
</html>
""" % (img,
       boxes[0]['height'], boxes[0]['width'] - broder, boxes[0]['x'] - broder, boxes[0]['y'] - broder, broder,
       boxes[1]['height'], boxes[1]['width'] - broder, boxes[1]['x'] - boxes[0]['x'] - boxes[0]['width'] - 2*broder,
       boxes[1]['y'] - broder, broder,
       boxes[2]['height'], boxes[2]['width'] - broder, boxes[2]['x'] - boxes[1]['x'] - boxes[1]['width'] - 2*broder,
       boxes[2]['y'] - broder, broder,
       boxes[3]['height'], boxes[3]['width'] - broder, boxes[3]['x'] - boxes[2]['x'] - boxes[2]['width'] - 2*broder,
       boxes[3]['y'] - broder, broder
       )

GET_HTML = "horizontal-boxes-test-block.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()

### Run the HTML file one-box-test.html ###
webbrowser.open("horizontal-boxes-test-block.html")
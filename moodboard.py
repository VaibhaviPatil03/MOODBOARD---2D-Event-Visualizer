import random

def pattern1():
 #Trial of multiple inputs


 import requests
 import re

 from PIL import Image, ImageDraw, ImageOps
 import os
 import re
 import random
 #import spacy
 from collections import Counter
 import itertools
 import networkx as nx
 #from google_images_download import google_images_download
 from PIL import Image
 import io

 #Load spaCy English model
 #nlp = spacy.load("en_core_web_sm")

 def extract_keywords(text):
    keywords = text.split()
    return keywords



 venue_input = input("Enter input for venue: ")
 food_input = input("Enter input for food: ")
 decor_input = input("Enter input for decor: ")
 entertainment_input = input("Enter input for entertainment: ")
 service_input = input("Enter input for service: ")
 '''

 venue_input = "yacht"
 food_input = "any"
 decor_input = "any"
 entertainment_input = "any"
 service_input = "any"
 '''
 venue_keywords = extract_keywords(venue_input)
 food_keywords = extract_keywords(food_input) + extract_keywords(venue_input)
 decor_keywords = extract_keywords(decor_input) + extract_keywords(venue_input)
 entertainment_keywords = extract_keywords(entertainment_input)
 service_keywords = extract_keywords(service_input)

 if 'none' in entertainment_keywords or 'any' in entertainment_keywords:
    entertainment_keywords += ['party', 'celebrate']

 if 'none' in service_keywords or 'any' in service_keywords:
    service_keywords += ['party', 'celebrate']

 #print("entertainment keywords:", entertainment_keywords)

 food_folder = "/content/drive/MyDrive/FOOD"
 venue_folder = "/content/drive/MyDrive/VENUE"
 service_folder = "/content/drive/MyDrive/SERVICES"
 entertainment_folder = "/content/drive/MyDrive/ENTERTAINMENT"
 decor_folder = "/content/drive/MyDrive/DECOR"
 image_folder = "/content/drive/MyDrive/image"
 food_labels_file = "/content/drive/MyDrive/food.txt"
 venue_labels_file = "/content/drive/MyDrive/venue.txt"
 service_labels_file = "/content/drive/MyDrive/service.txt"
 entertainment_labels_file = "/content/drive/MyDrive/entertainmentlabel.txt"
 decor_labels_file = "/content/drive/MyDrive/decorlabel.txt"

 moodboard = {
    "food": None,
    "venue": None,
    "empty1": None,
    "decor": None,
    "entertainment": None,
    "service": None,
 }

 def read_labels_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        image_labels = []
        image_files = []
        for line in lines:
            if line.startswith("Image:"):
                image_files.append(" ".join(line.split()[1:]))
            elif line.startswith("-"):
                image_labels.append(line[2:])
            elif not line:
                yield image_files, image_labels
                image_files = []
                image_labels = []
        if image_files:
            yield image_files, image_labels


 def find_matches(folder,image_files, labels, matches, keywords):
    keyword_matches = sum([1 for label in labels if any(keyword in label.lower() for keyword in keywords)])
    for image_file in image_files:
        image_path = os.path.join(folder, image_file.strip())
        if image_path in matches:
            matches[image_path] += keyword_matches
        else:
            matches[image_path] = keyword_matches


 # Processing - Venue Images
 venue_keyword_matches = {}
 for image_files, labels in read_labels_file(venue_labels_file):
    find_matches(venue_folder, image_files, labels, venue_keyword_matches, venue_keywords)

 #print("venue_keyword_matches:", venue_keyword_matches)

 if venue_keyword_matches:
    max_matches = max(venue_keyword_matches.values())
    if max_matches > 0:
        best_venue_images = [image for image, match in venue_keyword_matches.items() if match == max_matches]
        best_venue_image = random.choice(best_venue_images)
    else:
        best_venue_image = os.path.join(image_folder, "venuedefault.png")
 else:
    best_venue_image = os.path.join(image_folder, "venuedefault.png")

 moodboard["venue"] = Image.open(best_venue_image)


 # Processing - Food Images
 food_keyword_matches = {}
 for image_files, labels in read_labels_file(food_labels_file):
    find_matches(food_folder, image_files, labels, food_keyword_matches, food_keywords)

 #print("food_keyword_matches:", food_keyword_matches)

 if food_keyword_matches:
    max_matches = max(food_keyword_matches.values())
    if max_matches > 0:
        best_food_images = [image for image, match in food_keyword_matches.items() if match == max_matches]
        best_food_image = random.choice(best_food_images)
    else:
        best_food_image = os.path.join(image_folder, "fooddefault.png")
 else:
    best_food_image = os.path.join(image_folder, "fooddefault.png")

 moodboard["food"] = Image.open(best_food_image)


 # Processing - Service Images
 service_keyword_matches = {}
 for image_files, labels in read_labels_file(service_labels_file):
    find_matches(service_folder, image_files, labels, service_keyword_matches, service_keywords)

 #print("service_keyword_matches:", service_keyword_matches)

 if service_keyword_matches:
    max_matches = max(service_keyword_matches.values())
    if max_matches > 0:
        best_service_images = [image for image, match in service_keyword_matches.items() if match == max_matches]
        best_service_image = random.choice(best_service_images)
    else:
        best_service_image = os.path.join(image_folder, "servicedefault.png")
 else:
    best_service_image = os.path.join(image_folder, "servicedefault.png")

 moodboard["service"] = Image.open(best_service_image)


 # Processing - Entertainment Images
 entertainment_keyword_matches = {}
 for image_files, labels in read_labels_file(entertainment_labels_file):
    find_matches(entertainment_folder, image_files, labels, entertainment_keyword_matches, entertainment_keywords)

 #print("entertainment_keyword_matches:", entertainment_keyword_matches)

 if entertainment_keyword_matches:
    max_matches = max(entertainment_keyword_matches.values())
    if max_matches > 0:
        best_entertainment_images = [image for image, match in entertainment_keyword_matches.items() if match == max_matches]
        best_entertainment_image = random.choice(best_entertainment_images)
    else:
        best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")
 else:
    best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")

 moodboard["entertainment"] = Image.open(best_entertainment_image)


 # Processing - Decor Images
 decor_keyword_matches = {}
 for image_files, labels in read_labels_file(decor_labels_file):
    find_matches(decor_folder, image_files, labels, decor_keyword_matches, decor_keywords)

 #print("decor_keyword_matches:", decor_keyword_matches)

 if decor_keyword_matches:
    max_matches = max(decor_keyword_matches.values())
    if max_matches > 0:
        best_decor_images = [image for image, match in decor_keyword_matches.items() if match == max_matches]
        best_decor_image = random.choice(best_decor_images)
    else:
        best_decor_image = os.path.join(image_folder, "decordefault.png")
 else:
    best_decor_image = os.path.join(image_folder, "decordefault.png")

 moodboard["decor"] = Image.open(best_decor_image)


 max_width = 0
 max_height = 0
 for image in moodboard.values():
    if image is not None:
        width, height = image.size
        max_width = max(max_width, width)
        max_height = max(max_height, height)

 num_columns = 3
 num_rows = 2
 section_width = max_width
 section_height = max_height

 width = section_width * num_columns
 height = section_height * num_rows

 moodboard_image = Image.new("RGB", (width, height), "white")

 for i, (section, image) in enumerate(moodboard.items()):
    row = i // num_columns
    col = i % num_columns
    x = col * section_width
    y = row * section_height

    if section == "empty1":
        pass
    elif section == "venue":
        if image is not None:
            image = image.resize((section_width + 903, section_height + 80), Image.LANCZOS)
            x += 110
            y +=10
            moodboard_image.paste(image, (x, y))
    elif section == "food":
        if image is not None:
            image = image.resize((section_width + 90, section_height - 220), Image.LANCZOS)
            x+=10
            y+=10
            moodboard_image.paste(image, (x, y))
    elif section == "decor":
        if image is not None:
            image = image.resize((section_width + 90, section_height + 190), Image.LANCZOS)
            x+=10
            y -= 200  #Subtract the reduction
            moodboard_image.paste(image, (x, y))
    elif section == "entertainment":
        if image is not None:
            image = image.resize((section_width - 50, section_height - 110), Image.LANCZOS)
            x += 110
            y += 100
            moodboard_image.paste(image, (x, y))
    elif section == "service":
        if image is not None:
            image = image.resize((section_width - 83, section_height - 110), Image.LANCZOS)
            x += 70
            y += 100
            moodboard_image.paste(image, (x, y))
    else:
        if image is not None:
            image = image.resize((section_width, section_height), Image.LANCZOS)
            moodboard_image.paste(image, (x, y))

 #logo
 if moodboard["venue"] is not None:
    logo_image_path = os.path.join(image_folder, "quietloudlogo.jfif")
    logo_image = Image.open(logo_image_path)
    logo_image = logo_image.resize((200, 200), Image.LANCZOS)
    logo_image = logo_image.convert("RGBA")
    faded_logo = Image.new("RGBA", logo_image.size, (255, 255, 255, 0))
    logo_alpha = 0
    blended_logo = Image.blend(logo_image, faded_logo, alpha=logo_alpha)
    moodboard_image.paste(blended_logo, (width-200, 0), blended_logo)


 #circle_image_path = os.path.join(image_folder, "pastecircle.PNG")

 from PIL import Image, ImageDraw, ImageOps

 # ...

 circle_image_path = os.path.join(image_folder, "pastecircle.PNG")
 circle_image = Image.open(circle_image_path).convert("RGBA")
 circle_image = circle_image.resize((600, 600),Image.LANCZOS)

 mask = Image.new("L", circle_image.size, 0)
 draw = ImageDraw.Draw(mask)
 draw.ellipse((0, 0, circle_image.size[0], circle_image.size[1]), fill=255)

 circle_image = ImageOps.fit(circle_image, mask.size, centering=(0.5, 0.5))
 circle_image.putalpha(mask)

 transparent_background = Image.new("RGBA", moodboard_image.size, (0, 0, 0, 0))

 x = 830
 y = 600
 transparent_background.paste(circle_image, (x, y), circle_image)

 moodboard_image = Image.alpha_composite(moodboard_image.convert("RGBA"), transparent_background)


 '''
 circular_path = os.path.join(image_folder, "circular.png")
 circular = Image.open(circular_path)
 circular = circular.resize((200, 200), Image.ANTIALIAS)
 moodboard_image.paste(circular, (1000, 1000))
 '''
 draw = ImageDraw.Draw(moodboard_image)

 display(moodboard_image)

############################################################################################################################################################

def pattern2():
 #Adding Square pattern

 #Trial of multiple inputs


 import requests
 import re

 from PIL import Image, ImageDraw, ImageOps
 import os
 import re
 import random
 #import spacy
 from collections import Counter
 import itertools
 import networkx as nx
 #from google_images_download import google_images_download
 from PIL import Image
 import io

 #Load spaCy English model
 #nlp = spacy.load("en_core_web_sm")

 def extract_keywords(text):
    keywords = text.split()
    return keywords



 venue_input = input("Enter input for venue: ")
 food_input = input("Enter input for food: ")
 decor_input = input("Enter input for decor: ")
 entertainment_input = input("Enter input for entertainment: ")
 service_input = input("Enter input for service: ")
 '''

 venue_input = "yacht"
 food_input = "any"
 decor_input = "any"
 entertainment_input = "any"
 service_input = "any"
 '''
 venue_keywords = extract_keywords(venue_input)
 food_keywords = extract_keywords(food_input) + extract_keywords(venue_input)
 decor_keywords = extract_keywords(decor_input) + extract_keywords(venue_input)
 entertainment_keywords = extract_keywords(entertainment_input)
 service_keywords = extract_keywords(service_input)

 if 'none' in entertainment_keywords or 'any' in entertainment_keywords:
    entertainment_keywords += ['party', 'celebrate']

 if 'none' in service_keywords or 'any' in service_keywords:
    service_keywords += ['party', 'celebrate']

 #print("entertainment keywords:", entertainment_keywords)

 food_folder = "/content/drive/MyDrive/FOOD"
 venue_folder = "/content/drive/MyDrive/VENUE"
 service_folder = "/content/drive/MyDrive/SERVICES"
 entertainment_folder = "/content/drive/MyDrive/ENTERTAINMENT"
 decor_folder = "/content/drive/MyDrive/DECOR"
 image_folder = "/content/drive/MyDrive/image"
 food_labels_file = "/content/drive/MyDrive/food.txt"
 venue_labels_file = "/content/drive/MyDrive/venue.txt"
 service_labels_file = "/content/drive/MyDrive/service.txt"
 entertainment_labels_file = "/content/drive/MyDrive/entertainmentlabel.txt"
 decor_labels_file = "/content/drive/MyDrive/decorlabel.txt"

 moodboard = {
    "venue": None,
    "food": None,
    "empty1": None,
    "decor": None,
    "empty2": None,
    "entertainment": None,
    "empty3": None,
    "empty4": None,
    "service": None,
 }
 def read_labels_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        image_labels = []
        image_files = []
        for line in lines:
            if line.startswith("Image:"):
                image_files.append(" ".join(line.split()[1:]))
            elif line.startswith("-"):
                image_labels.append(line[2:])
            elif not line:
                yield image_files, image_labels
                image_files = []
                image_labels = []
        if image_files:
            yield image_files, image_labels


 def find_matches(folder,image_files, labels, matches, keywords):
    keyword_matches = sum([1 for label in labels if any(keyword in label.lower() for keyword in keywords)])
    for image_file in image_files:
        image_path = os.path.join(folder, image_file.strip())
        if image_path in matches:
            matches[image_path] += keyword_matches
        else:
            matches[image_path] = keyword_matches


 # Processing - Venue Images
 venue_keyword_matches = {}
 for image_files, labels in read_labels_file(venue_labels_file):
    find_matches(venue_folder, image_files, labels, venue_keyword_matches, venue_keywords)

 #print("venue_keyword_matches:", venue_keyword_matches)

 if venue_keyword_matches:
    max_matches = max(venue_keyword_matches.values())
    if max_matches > 0:
        best_venue_images = [image for image, match in venue_keyword_matches.items() if match == max_matches]
        best_venue_image = random.choice(best_venue_images)
    else:
        best_venue_image = os.path.join(image_folder, "venuedefault.png")
 else:
    best_venue_image = os.path.join(image_folder, "venuedefault.png")

 moodboard["venue"] = Image.open(best_venue_image)



 # Processing - Food Images
 food_keyword_matches = {}
 for image_files, labels in read_labels_file(food_labels_file):
    find_matches(food_folder, image_files, labels, food_keyword_matches, food_keywords)

 #print("food_keyword_matches:", food_keyword_matches)

 if food_keyword_matches:
    max_matches = max(food_keyword_matches.values())
    if max_matches > 0:
        best_food_images = [image for image, match in food_keyword_matches.items() if match == max_matches]
        best_food_image = random.choice(best_food_images)
    else:
        best_food_image = os.path.join(image_folder, "fooddefault.png")
 else:
    best_food_image = os.path.join(image_folder, "fooddefault.png")

 moodboard["food"] = Image.open(best_food_image)


 # Processing - Service Images
 service_keyword_matches = {}
 for image_files, labels in read_labels_file(service_labels_file):
    find_matches(service_folder, image_files, labels, service_keyword_matches, service_keywords)

 #print("service_keyword_matches:", service_keyword_matches)

 if service_keyword_matches:
    max_matches = max(service_keyword_matches.values())
    if max_matches > 0:
        best_service_images = [image for image, match in service_keyword_matches.items() if match == max_matches]
        best_service_image = random.choice(best_service_images)
    else:
        best_service_image = os.path.join(image_folder, "servicedefault.png")
 else:
    best_service_image = os.path.join(image_folder, "servicedefault.png")

 moodboard["service"] = Image.open(best_service_image)


 # Processing - Entertainment Images
 entertainment_keyword_matches = {}
 for image_files, labels in read_labels_file(entertainment_labels_file):
    find_matches(entertainment_folder, image_files, labels, entertainment_keyword_matches, entertainment_keywords)

 #print("entertainment_keyword_matches:", entertainment_keyword_matches)

 if entertainment_keyword_matches:
    max_matches = max(entertainment_keyword_matches.values())
    if max_matches > 0:
        best_entertainment_images = [image for image, match in entertainment_keyword_matches.items() if match == max_matches]
        best_entertainment_image = random.choice(best_entertainment_images)
    else:
        best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")
 else:
    best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")

 moodboard["entertainment"] = Image.open(best_entertainment_image)


 # Processing - Decor Images
 decor_keyword_matches = {}
 for image_files, labels in read_labels_file(decor_labels_file):
    find_matches(decor_folder, image_files, labels, decor_keyword_matches, decor_keywords)

 #print("decor_keyword_matches:", decor_keyword_matches)

 if decor_keyword_matches:
    max_matches = max(decor_keyword_matches.values())
    if max_matches > 0:
        best_decor_images = [image for image, match in decor_keyword_matches.items() if match == max_matches]
        best_decor_image = random.choice(best_decor_images)
    else:
        best_decor_image = os.path.join(image_folder, "decordefault.png")
 else:
    best_decor_image = os.path.join(image_folder, "decordefault.png")

 moodboard["decor"] = Image.open(best_decor_image)


 max_width = 0
 max_height = 0
 for image in moodboard.values():
    if image is not None:
        width, height = image.size
        max_width = max(max_width, width)
        max_height = max(max_height, height)

 num_columns = 3
 num_rows = 3
 section_width = max_width-700
 section_height = max_height-700

 width = section_width * num_columns
 height = section_height * num_rows

 moodboard_image = Image.new("RGB", (width, height), "white")


 # Load the "squarepaste.PNG" image
 squarepaste_path = os.path.join(image_folder, "squarepaste.png")
 squarepaste_image = Image.open(squarepaste_path).convert("RGBA")

 # Resize the "squarepaste.PNG" image to the desired size
 squarepaste_width = 650
 squarepaste_height = 220
 squarepaste_image = squarepaste_image.resize((squarepaste_width, squarepaste_height), Image.LANCZOS)

 # Paste the "squarepaste.PNG" image onto the moodboard at the desired location
 paste_x = 0
 paste_y = 755
 moodboard_image.paste(squarepaste_image, (paste_x, paste_y), squarepaste_image)



 for i, (section, image) in enumerate(moodboard.items()):
    row = i // num_columns
    col = i % num_columns
    x = col * section_width
    y = row * section_height

    if section == "empty1" or section == "empty2" or section == "empty3" or section == "empty4":
        pass
    elif section == "venue":
        if image is not None:
            image = image.resize((section_width+245, section_height+100), Image.LANCZOS)
            #x += 110
            #y += 10
            moodboard_image.paste(image, (x, y))
    elif section == "food":
        if image is not None:
            image = image.resize((section_width+70, section_height+30), Image.LANCZOS)
            x += 255
            #y += 10
            moodboard_image.paste(image, (x, y))
    elif section == "decor":
        if image is not None:
            image = image.resize((section_width+313, section_height), Image.LANCZOS)
            #x += 10
            y += 110  # Subtract the reduction
            moodboard_image.paste(image, (x, y))
    elif section == "entertainment":
        if image is not None:
            image = image.resize((section_width, section_height-10), Image.LANCZOS)
            #x += 10
            y += 40
            moodboard_image.paste(image, (x, y))
    elif section == "service":
        if image is not None:
            image = image.resize((section_width, section_height-40), Image.LANCZOS)
            #x += 20
            y += 40
            moodboard_image.paste(image, (x, y))
    else:
        if image is not None:
            # Resize all sections to a square shape
            image = image.resize((section_width, section_height), Image.LANCZOS)
            moodboard_image.paste(image, (x, y))

 #logo
 if moodboard["venue"] is not None:
    logo_image_path = os.path.join(image_folder, "quietloudlogo.jfif")
    logo_image = Image.open(logo_image_path)
    logo_image = logo_image.resize((65, 65), Image.LANCZOS)
    logo_image = logo_image.convert("RGBA")
    faded_logo = Image.new("RGBA", logo_image.size, (255, 255, 255, 0))
    logo_alpha = 0
    blended_logo = Image.blend(logo_image, faded_logo, alpha=logo_alpha)
    moodboard_image.paste(blended_logo, (width-65, 0), blended_logo)


 #circle_image_path = os.path.join(image_folder, "pastecircle.PNG")

 from PIL import Image, ImageDraw, ImageOps



 circle_image_path = os.path.join(image_folder, "popperpaste.PNG")
 circle_image = Image.open(circle_image_path).convert("RGBA")
 circle_image = circle_image.resize((220, 220), Image.LANCZOS)

 mask = Image.new("L", circle_image.size, 0)
 draw = ImageDraw.Draw(mask)
 draw.ellipse((0, 0, circle_image.size[0], circle_image.size[1]), fill=255)

 circle_image = ImageOps.fit(circle_image, mask.size, centering=(0.5, 0.5))
 circle_image.putalpha(mask)

 transparent_background = Image.new("RGBA", moodboard_image.size, (0, 0, 0, 0))

 x = 500
 y = 250
 transparent_background.paste(circle_image, (x, y), circle_image)

 moodboard_image = Image.alpha_composite(moodboard_image.convert("RGBA"), transparent_background)





 '''
 circular_path = os.path.join(image_folder, "circular.png")
 circular = Image.open(circular_path)
 circular = circular.resize((200, 200), Image.ANTIALIAS)
 moodboard_image.paste(circular, (1000, 1000))
 '''
 draw = ImageDraw.Draw(moodboard_image)

 display(moodboard_image)

####################################################################################################################################################

def pattern3():
 #different rectangle

 #Trial of multiple inputs


 import requests
 import re

 from PIL import Image, ImageDraw, ImageOps
 import os
 import re
 import random
 #import spacy
 from collections import Counter
 import itertools
 import networkx as nx
 #from google_images_download import google_images_download
 from PIL import Image
 import io

 #Load spaCy English model
 #nlp = spacy.load("en_core_web_sm")

 def extract_keywords(text):
    keywords = text.split()
    return keywords



 venue_input = input("Enter input for venue: ")
 food_input = input("Enter input for food: ")
 decor_input = input("Enter input for decor: ")
 entertainment_input = input("Enter input for entertainment: ")
 service_input = input("Enter input for service: ")
 '''

 venue_input = "yacht"
 food_input = "any"
 decor_input = "any"
 entertainment_input = "any"
 service_input = "any"
 '''
 venue_keywords = extract_keywords(venue_input)
 food_keywords = extract_keywords(food_input) + extract_keywords(venue_input)
 decor_keywords = extract_keywords(decor_input) + extract_keywords(venue_input)
 entertainment_keywords = extract_keywords(entertainment_input)
 service_keywords = extract_keywords(service_input)

 if 'none' in entertainment_keywords or 'any' in entertainment_keywords:
    entertainment_keywords += ['party', 'celebrate']

 if 'none' in service_keywords or 'any' in service_keywords:
    service_keywords += ['party', 'celebrate']

 #print("entertainment keywords:", entertainment_keywords)

 food_folder = "/content/drive/MyDrive/FOOD"
 venue_folder = "/content/drive/MyDrive/VENUE"
 service_folder = "/content/drive/MyDrive/SERVICES"
 entertainment_folder = "/content/drive/MyDrive/ENTERTAINMENT"
 decor_folder = "/content/drive/MyDrive/DECOR"
 image_folder = "/content/drive/MyDrive/image"
 food_labels_file = "/content/drive/MyDrive/food.txt"
 venue_labels_file = "/content/drive/MyDrive/venue.txt"
 service_labels_file = "/content/drive/MyDrive/service.txt"
 entertainment_labels_file = "/content/drive/MyDrive/entertainmentlabel.txt"
 decor_labels_file = "/content/drive/MyDrive/decorlabel.txt"

 moodboard = {
    "food": None,
    "empty1": None,
    "decor": None,
    "venue": None,
    "entertainment": None,
    "service": None,
 }

 def read_labels_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        image_labels = []
        image_files = []
        for line in lines:
            if line.startswith("Image:"):
                image_files.append(" ".join(line.split()[1:]))
            elif line.startswith("-"):
                image_labels.append(line[2:])
            elif not line:
                yield image_files, image_labels
                image_files = []
                image_labels = []
        if image_files:
            yield image_files, image_labels


 def find_matches(folder,image_files, labels, matches, keywords):
    keyword_matches = sum([1 for label in labels if any(keyword in label.lower() for keyword in keywords)])
    for image_file in image_files:
        image_path = os.path.join(folder, image_file.strip())
        if image_path in matches:
            matches[image_path] += keyword_matches
        else:
            matches[image_path] = keyword_matches


 # Processing - Venue Images
 venue_keyword_matches = {}
 for image_files, labels in read_labels_file(venue_labels_file):
    find_matches(venue_folder, image_files, labels, venue_keyword_matches, venue_keywords)

 #print("venue_keyword_matches:", venue_keyword_matches)

 if venue_keyword_matches:
    max_matches = max(venue_keyword_matches.values())
    if max_matches > 0:
        best_venue_images = [image for image, match in venue_keyword_matches.items() if match == max_matches]
        best_venue_image = random.choice(best_venue_images)
    else:
        best_venue_image = os.path.join(image_folder, "venuedefault.png")
 else:
    best_venue_image = os.path.join(image_folder, "venuedefault.png")

 moodboard["venue"] = Image.open(best_venue_image)


 # Processing - Food Images
 food_keyword_matches = {}
 for image_files, labels in read_labels_file(food_labels_file):
    find_matches(food_folder, image_files, labels, food_keyword_matches, food_keywords)

 #print("food_keyword_matches:", food_keyword_matches)

 if food_keyword_matches:
    max_matches = max(food_keyword_matches.values())
    if max_matches > 0:
        best_food_images = [image for image, match in food_keyword_matches.items() if match == max_matches]
        best_food_image = random.choice(best_food_images)
    else:
        best_food_image = os.path.join(image_folder, "fooddefault.png")
 else:
    best_food_image = os.path.join(image_folder, "fooddefault.png")

 moodboard["food"] = Image.open(best_food_image)


 # Processing - Service Images
 service_keyword_matches = {}
 for image_files, labels in read_labels_file(service_labels_file):
    find_matches(service_folder, image_files, labels, service_keyword_matches, service_keywords)

 #print("service_keyword_matches:", service_keyword_matches)

 if service_keyword_matches:
    max_matches = max(service_keyword_matches.values())
    if max_matches > 0:
        best_service_images = [image for image, match in service_keyword_matches.items() if match == max_matches]
        best_service_image = random.choice(best_service_images)
    else:
        best_service_image = os.path.join(image_folder, "servicedefault.png")
 else:
    best_service_image = os.path.join(image_folder, "servicedefault.png")

 moodboard["service"] = Image.open(best_service_image)


 # Processing - Entertainment Images
 entertainment_keyword_matches = {}
 for image_files, labels in read_labels_file(entertainment_labels_file):
    find_matches(entertainment_folder, image_files, labels, entertainment_keyword_matches, entertainment_keywords)

 #print("entertainment_keyword_matches:", entertainment_keyword_matches)

 if entertainment_keyword_matches:
    max_matches = max(entertainment_keyword_matches.values())
    if max_matches > 0:
        best_entertainment_images = [image for image, match in entertainment_keyword_matches.items() if match == max_matches]
        best_entertainment_image = random.choice(best_entertainment_images)
    else:
        best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")
 else:
    best_entertainment_image = os.path.join(image_folder, "entertainmentdefault.png")

 moodboard["entertainment"] = Image.open(best_entertainment_image)


 # Processing - Decor Images
 decor_keyword_matches = {}
 for image_files, labels in read_labels_file(decor_labels_file):
    find_matches(decor_folder, image_files, labels, decor_keyword_matches, decor_keywords)

 #print("decor_keyword_matches:", decor_keyword_matches)

 if decor_keyword_matches:
    max_matches = max(decor_keyword_matches.values())
    if max_matches > 0:
        best_decor_images = [image for image, match in decor_keyword_matches.items() if match == max_matches]
        best_decor_image = random.choice(best_decor_images)
    else:
        best_decor_image = os.path.join(image_folder, "decordefault.png")
 else:
    best_decor_image = os.path.join(image_folder, "decordefault.png")

 moodboard["decor"] = Image.open(best_decor_image)


 max_width = 0
 max_height = 0
 for image in moodboard.values():
    if image is not None:
        width, height = image.size
        max_width = max(max_width, width)
        max_height = max(max_height, height)

 num_columns = 3
 num_rows = 2
 section_width = max_width
 section_height = max_height

 width = section_width * num_columns
 height = section_height * num_rows

 moodboard_image = Image.new("RGB", (width, height), "lavender")


 #from PIL import Image, ImageDraw, ImageOps



 for i, (section, image) in enumerate(moodboard.items()):
    row = i // num_columns
    col = i % num_columns
    x = col * section_width
    y = row * section_height

    if section == "empty1":
        pass
    elif section == "venue":
        if image is not None:
            image = image.resize((section_width + 150, section_height+50), Image.LANCZOS)
            x += 100
            y -=150
            moodboard_image.paste(image, (x, y))
    elif section == "food":
        if image is not None:
            image = image.resize((section_width + 150, section_height - 300), Image.LANCZOS)
            x+=100
            y+=100
            moodboard_image.paste(image, (x, y))
    elif section == "decor":
        if image is not None:
            image = image.resize((section_width -100, section_height+100), Image.LANCZOS)
            #x+=10
            y += 100  #Subtract the reduction
            moodboard_image.paste(image, (x, y))
    elif section == "entertainment":
        if image is not None:
            image = image.resize((section_width - 150, section_height - 350), Image.LANCZOS)
            x += 300
            y += 250
            moodboard_image.paste(image, (x, y))
    elif section == "service":
        if image is not None:
            image = image.resize((section_width - 300, section_height - 350), Image.LANCZOS)
            x += 200
            y += 250
            moodboard_image.paste(image, (x, y))
    else:
        if image is not None:
            image = image.resize((section_width, section_height), Image.LANCZOS)
            moodboard_image.paste(image, (x, y))


 #logo
 if moodboard["venue"] is not None:
    logo_image_path = os.path.join(image_folder, "quietloudlogo.jfif")
    logo_image = Image.open(logo_image_path)
    logo_image = logo_image.resize((200, 200), Image.LANCZOS)
    logo_image = logo_image.convert("RGBA")
    faded_logo = Image.new("RGBA", logo_image.size, (255, 255, 255, 0))
    logo_alpha = 0
    blended_logo = Image.blend(logo_image, faded_logo, alpha=logo_alpha)
    moodboard_image.paste(blended_logo, (width-200, 0), blended_logo)


 #circle_image_path = os.path.join(image_folder, "pastecircle.PNG")

 #from PIL import Image, ImageDraw, ImageOps

 pastetext_path = os.path.join(image_folder, "pastetext.png")
 pastetext_image = Image.open(pastetext_path).convert("RGBA")

 pastetext_width = 700
 pastetext_height = 1000
 pastetext_image = pastetext_image.resize((pastetext_width, pastetext_height), Image.LANCZOS)

 paste_x = 1300
 paste_y = 200
 moodboard_image.paste(pastetext_image, (paste_x, paste_y), pastetext_image)

 '''

 circle_image_path = os.path.join(image_folder, "pastecircle.PNG")
 circle_image = Image.open(circle_image_path).convert("RGBA")
 circle_image = circle_image.resize((600, 600), Image.ANTIALIAS)

 mask = Image.new("L", circle_image.size, 0)
 draw = ImageDraw.Draw(mask)
 draw.ellipse((0, 0, circle_image.size[0], circle_image.size[1]), fill=255)

 circle_image = ImageOps.fit(circle_image, mask.size, centering=(0.5, 0.5))
 circle_image.putalpha(mask)

 transparent_background = Image.new("RGBA", moodboard_image.size, (0, 0, 0, 0))

 x = 830
 y = 600
 transparent_background.paste(circle_image, (x, y), circle_image)

 moodboard_image = Image.alpha_composite(moodboard_image.convert("RGBA"), transparent_background)

 '''
 '''
 circular_path = os.path.join(image_folder, "circular.png")
 circular = Image.open(circular_path)
 circular = circular.resize((200, 200), Image.ANTIALIAS)
 moodboard_image.paste(circular, (1000, 1000))
 '''
 draw = ImageDraw.Draw(moodboard_image)

 display(moodboard_image)



patterns = [pattern1, pattern2, pattern3]

random_function = random.choice(patterns)
random_function()
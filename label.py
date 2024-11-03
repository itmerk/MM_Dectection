import json
import random
import os

# Paths to the images and annotations
annotations_path = "D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/test/annotations/test_annotations.json"
images_folder = "D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/test/images"

# Load COCO annotations JSON
with open(annotations_path, 'r') as f:
    coco_data = json.load(f)

# Shuffle and split images
images = coco_data['images']
random.shuffle(images)

# Define split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Split images
num_images = len(images)
train_images = images[:int(train_ratio * num_images)]
val_images = images[int(train_ratio * num_images):int((train_ratio + val_ratio) * num_images)]
test_images = images[int((train_ratio + val_ratio) * num_images):]

# Filter annotations for each split
def filter_annotations(images, annotations):
    image_ids = set(img['id'] for img in images)
    return [ann for ann in annotations if ann['image_id'] in image_ids]

train_annotations = filter_annotations(train_images, coco_data['annotations'])
val_annotations = filter_annotations(val_images, coco_data['annotations'])
test_annotations = filter_annotations(test_images, coco_data['annotations'])

# Create COCO JSON for each split
def create_coco_json(images, annotations, categories):
    return {
        'images': images,
        'annotations': annotations,
        'categories': categories
    }

# Save each split to a JSON file
os.makedirs('output_coco', exist_ok=True)
with open('output_coco/train_annotations.json', 'w') as f:
    json.dump(create_coco_json(train_images, train_annotations, coco_data['categories']), f)
with open('output_coco/val_annotations.json', 'w') as f:
    json.dump(create_coco_json(val_images, val_annotations, coco_data['categories']), f)
with open('output_coco/test_annotations.json', 'w') as f:
    json.dump(create_coco_json(test_images, test_annotations, coco_data['categories']), f)

import shutil
import os
import json
from PIL import Image

itemModelSize = 64

# Define source and destination paths
source_folder = 'staticFiles'
destination_folder = f'GlamourRP-{itemModelSize}'

# Clone the staticFiles folder to GlamourRP-{itemModelSize}
if os.path.exists(source_folder):
    shutil.copytree(source_folder, destination_folder)
else:
    print(f"Source folder '{source_folder}' does not exist.")

# Define the destination file path
destination_file_path = os.path.join(destination_folder, 'assets', 'glam', 'items' , 'glam_base.json')

# Ensure the directory exists
os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

# Generate models for each pixel
models = []
counter = 0
for i in range(itemModelSize):
    for j in range(itemModelSize):
        models.append({
            "type": "minecraft:condition",
            "property": "minecraft:custom_model_data",
            "index": counter,
            "on_true": {
                "type": "minecraft:model",
                "model": f"glam:item/pixel_base/{i}x{j}",
                "tints": [
                    {
                        "type": "minecraft:custom_model_data",
                        "default": 16777215,
                        "index": counter
                    }
                ]
            },
            "on_false": {
                "type": "minecraft:empty"
            }
        })
        counter += 1

# Define the JSON content
json_content = {
    "model": {
        "type": "minecraft:composite",
        "models": models
    }
}

# Write the JSON content to the file
with open(destination_file_path, 'w') as json_file:
    json.dump(json_content, json_file, indent=2)

# Define the destination file path
destination_file_path = os.path.join(destination_folder, 'assets', 'glam', 'items' , 'glam_item.json')

# Ensure the directory exists
os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

# Generate models for each pixel
models = []
counter = 0
for i in range(itemModelSize):
    for j in range(itemModelSize):
        models.append({
            "type": "minecraft:condition",
            "property": "minecraft:custom_model_data",
            "index": counter,
            "on_true": {
                "type": "minecraft:model",
                "model": f"glam:item/pixel_item/{i}x{j}",
                "tints": [
                    {
                        "type": "minecraft:custom_model_data",
                        "default": 16777215,
                        "index": counter
                    }
                ]
            },
            "on_false": {
                "type": "minecraft:empty"
            }
        })
        counter += 1

# Define the JSON content
json_content = {
    "model": {
        "type": "minecraft:composite",
        "models": models
    }
}

# Write the JSON content to the file
with open(destination_file_path, 'w') as json_file:
    json.dump(json_content, json_file, indent=2)

# Define the destination file path
destination_file_path = os.path.join(destination_folder, 'assets', 'glam', 'items' , 'glam_large.json')

# Ensure the directory exists
os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

# Generate models for each pixel
models = []
counter = 0
for i in range(itemModelSize):
    for j in range(itemModelSize):
        models.append({
            "type": "minecraft:condition",
            "property": "minecraft:custom_model_data",
            "index": counter,
            "on_true": {
                "type": "minecraft:model",
                "model": f"glam:item/pixel_large/{i}x{j}",
                "tints": [
                    {
                        "type": "minecraft:custom_model_data",
                        "default": 16777215,
                        "index": counter
                    }
                ]
            },
            "on_false": {
                "type": "minecraft:empty"
            }
        })
        counter += 1

# Define the JSON content
json_content = {
    "model": {
        "type": "minecraft:composite",
        "models": models
    }
}

# Write the JSON content to the file
with open(destination_file_path, 'w') as json_file:
    json.dump(json_content, json_file, indent=2)


# Define the base item model path
baseItemModelPath = os.path.join(destination_folder, 'assets', 'glam', 'models', 'item', 'pixel_base')

# Ensure the directory exists
os.makedirs(baseItemModelPath, exist_ok=True)

# Generate files for each pixel
for i in range(itemModelSize):
    for j in range(itemModelSize):
        file_path = os.path.join(baseItemModelPath, f'{i}x{j}.json')
        file_content = {
            "parent": "glam:item/pixel_base",
            "textures": {
                "layer0": f"glam:item/pixel_base/{i}x{j}"
            }
        }
        with open(file_path, 'w') as json_file:
            json.dump(file_content, json_file, indent=2)
            

# Define the base item model path
itemItemModelPath = os.path.join(destination_folder, 'assets', 'glam', 'models', 'item', 'pixel_item')

# Ensure the directory exists
os.makedirs(itemItemModelPath, exist_ok=True)

# Generate files for each pixel
for i in range(itemModelSize):
    for j in range(itemModelSize):
        file_path = os.path.join(itemItemModelPath, f'{i}x{j}.json')
        file_content = {
            "parent": "glam:item/pixel_item",
            "textures": {
                "layer0": f"glam:item/pixel_base/{i}x{j}"
            }
        }
        with open(file_path, 'w') as json_file:
            json.dump(file_content, json_file, indent=2)
            

# Define the base item model path
largeItemModelPath = os.path.join(destination_folder, 'assets', 'glam', 'models', 'item', 'pixel_large')

# Ensure the directory exists
os.makedirs(largeItemModelPath, exist_ok=True)

# Generate files for each pixel
for i in range(itemModelSize):
    for j in range(itemModelSize):
        file_path = os.path.join(largeItemModelPath, f'{i}x{j}.json')
        file_content = {
            "parent": "glam:item/pixel_large",
            "textures": {
                "layer0": f"glam:item/pixel_base/{i}x{j}"
            }
        }
        with open(file_path, 'w') as json_file:
            json.dump(file_content, json_file, indent=2)

# Define the base texture path
baseTexturePath = os.path.join(destination_folder, 'assets', 'glam', 'textures', 'item', 'pixel_base')

# Ensure the directory exists
os.makedirs(baseTexturePath, exist_ok=True)

# Generate images for each pixel
for i in range(itemModelSize):
    for j in range(itemModelSize):
        # Create a new image with transparency (RGBA)
        image = Image.new('RGBA', (itemModelSize, itemModelSize), (0, 0, 0, 0))
        # Set the pixel at (i, j) to white
        image.putpixel((j, itemModelSize-i-1), (255, 255, 255, 255))
        # Save the image
        file_path = os.path.join(baseTexturePath, f'{i}x{j}.png')
        image.save(file_path)
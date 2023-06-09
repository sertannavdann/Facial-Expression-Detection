import os
import shutil
import random
import torchvision.transforms as transforms
from PIL import Image

# Define the directories for the original and augmented data
train_dir = 'data/train/'
balanced_dir = 'data/tr_balanced/'

test_dir = 'data/test/'
balantest_dir = 'data/te_balanced/'

# Define the number of images to have per class
num_images_per_class = 1000

# Create the balanced directory if it doesn't exist
if not os.path.exists(balantest_dir):
    os.makedirs(balantest_dir)

transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.RandomApply([transforms.RandomHorizontalFlip()], p=0.5),
    transforms.RandomApply([transforms.RandomRotation(10)], p=0.1),
    transforms.RandomApply([transforms.RandomVerticalFlip()], p=0.5),
    transforms.RandomApply([transforms.RandomCrop(32, padding=4)], p=0.5),
    transforms.RandomApply([transforms.ColorJitter(brightness=0.125, contrast=0.075, saturation=0.125, hue=0.125)], p=0.5),
    transforms.RandomApply([transforms.RandomAffine(degrees=20, translate=(0.1, 0.1), scale=(0.9, 1.1), shear=10)], p=0.5),
    transforms.RandomApply([transforms.RandomPerspective(distortion_scale=0.3, p=0.5)], p=0.5),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Loop over the classes
for class_name in os.listdir(test_dir):
    class_dir = os.path.join(test_dir, class_name)
    balanced_class_dir = os.path.join(balantest_dir, class_name)
    
    # Create the balanced class directory if it doesn't exist
    if not os.path.exists(balanced_class_dir):
        os.makedirs(balanced_class_dir)
    
    # Get the number of images in the class directory
    num_images = len(os.listdir(class_dir))
    
    # If the class has fewer images than the required number of images, generate new images
    if num_images < num_images_per_class:
        num_augmented_images = num_images_per_class - num_images
        
        # Loop over the images in the class directory and generate new augmented images
        for i, image_name in enumerate(os.listdir(class_dir)):
            if i >= num_images:
                break
            image_path = os.path.join(class_dir, image_name)
            image = Image.open(image_path)
            
            # Save the original image to the balanced class directory
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            shutil.copy(image_path, balanced_image_path)
            
        # Loop over the images in the class directory and generate new augmented images
        for i in range(num_augmented_images):
            image_name = f"{class_name}_b_{i}.jpg"
            image_path = os.path.join(class_dir, random.choice(os.listdir(class_dir)))
            image = Image.open(image_path)
            
            # Apply the transformations to the image
            augmented_image = transform(image)
            
            # Save the augmented image to the balanced class directory
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            transforms.ToPILImage()(augmented_image).save(balanced_image_path)
            
    # If the class has more images than the required number of images, randomly select images to copy
    else:
        random_image_names = random.sample(os.listdir(class_dir), num_images_per_class)
        for image_name in random_image_names:
            image_path = os.path.join(class_dir, image_name)
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            shutil.copy(image_path, balanced_image_path)

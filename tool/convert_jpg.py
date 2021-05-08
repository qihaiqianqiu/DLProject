from PIL import Image
import os

root_dir = '/content/DLProject/deepfashion'

def convert_dataset(folder, new_folder):
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    for name in os.listdir(folder):
        old_name = os.path.join(folder, name)
        new_name = os.path.join(new_folder, name)

        img = Image.open(old_name)
        img = img.convert('RGB')
        img.save(new_name.strip('.png') + '.jpg')

convert_dataset(root_dir + '/raw', root_dir + '/test')
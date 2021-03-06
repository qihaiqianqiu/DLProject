from PIL import Image
import os
import sys

root_dir = '/content/DLProject/deepfashion'

def convert_dataset(folder, new_folder):
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    for name in os.listdir(folder):
        old_name = os.path.join(folder, name)
        new_name = os.path.join(new_folder, name)

        if '.png' in new_name:
            img = Image.open(old_name).convert("RGB")
            img2 = Image.open(old_name).convert("RGBA")
            x,y = img.size 
            new_point = 1.1*y / 256
            new_x = int(176*new_point)
            new_y = int(256*new_point)
            p = Image.new('RGB', (new_x,new_y), (255,255,255))
            #p = Image.new('RGB', img.size, (255,255,255))
            p.paste(img, (int(new_x/2-x/2),int(new_y/2-y/2) , int(new_x/2-x/2)+x, int(new_y/2-y/2)+y), img2)
            p.save(new_name.strip('.png') + '.jpg')
        #p.paste(img,(0,0,x,y),img2)
        if 'jpg' in new_name:
            img = Image.open(old_name).convert("RGB")
            img2 = Image.open(old_name).convert("RGBA")
            x,y = img.size
            p = Image.new('RGB', img.size, (255,255,255))
            p.paste(img,(0,0,x,y),img2)
            p.save(new_name)
 

convert_dataset(root_dir + '/raw_' + sys.argv[1], root_dir + '/'+ sys.argv[1])



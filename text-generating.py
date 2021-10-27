import os
import glob
from tqdm import tqdm

def textGenerate():
    root_path1 = r'C:\Users\Myth\Desktop\data\input\train'
    root_path2 = r'C:\Users\Myth\Desktop\data\output\train'

    save_dir = os.path.normpath(root_path1)
    save_dir2 = os.path.normpath(root_path2)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print('create folder')

    with open(r'C:\Users\Myth\Desktop\data\input\train.txt', 'w') as f:
        path1 = root_path1 + '\*png'
        path2 = root_path2 + '\*png'

        pictures_list1 = glob.glob(path1)
        pictures_list2 = glob.glob(path2)

    #     for root, dirs, files in os.walk(root_path1):
    #         for file in files:
    #             l1.append(str(file))

        with tqdm(total=len(pictures_list1)) as bar:
            idx = 0
            for pic in pictures_list1:

                name = os.path.basename(os.path.normpath(pic))
                label = os.path.basename(os.path.normpath(pictures_list2[idx]))

                f.write(os.path.join(save_dir, name) + ' ' + os.path.join(save_dir2, label) + '\n')
                idx = idx + 1
                bar.update(1)
                
if __name__=='__main__':
    textGenerate()

# coding:utf8
import os
from PIL import Image
from torch.utils import data
import numpy as np
from torchvision import transforms as T


class GenderData(data.Dataset):

    def __init__(self, root, transforms=None, train=True, test=False):
        """
        主要目标： 获取所有图片的地址，并根据训练，验证，测试划分数据
        """
        self.test = test
        imgs = [os.path.join(root, img) for img in os.listdir(root)]
        # test1: data/test1/8973.jpg
        # train: data/train/cat.10004.jpg
        '''
        if self.test:
            imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2].split('/')[-1]))#key是sort的標準，x是imgs裡面的一張圖片元素，
        else:
            imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2]))
        '''
        imgs_num = len(imgs)

        if self.test:
            self.imgs = imgs
        elif train:
            self.imgs = imgs[:int(0.7 * imgs_num)]
        else:
            self.imgs = imgs[int(0.7 * imgs_num):]

        if transforms is None:
            normalize = T.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])

            if self.test or not train:
                self.transforms = T.Compose([
                    T.CenterCrop(110),#從中心裁減
                    T.Scale(256),#放大成給定大小
                    T.ToTensor(),#1. 将图像的像素范围由[0,255]映射为[0,1] 2. 将像素的组织顺序由numpy.ndarray的(H x W x C)或PIL格式的图像转换为 (C x H x W)。
                    normalize#標準化
                ])
            else:
                self.transforms = T.Compose([
                    T.CenterCrop(110),
                    T.Scale(256),
                    T.RandomHorizontalFlip(),
                    T.ToTensor(),
                    normalize
                ])

    def __getitem__(self, index):
        """
        一次返回一张图片的数据
        """
        img_path = self.imgs[index]
        '''
        if self.test:
            
            label = int(self.imgs[index].split('.')[])
        else:
            label = 1 if 'male' in img_path.split('/')[-1] else 0
        '''
        label = 0 if 'female' in img_path.split('.')[-3] else 1
        '''
        if label == 1:
            print('1')
        elif label == 0:
            print('0')
        '''
        data = Image.open(img_path)
        data = self.transforms(data)
        return data, label

    def __len__(self):
        return len(self.imgs)

# train = DogCat("../data/train/")
# print((train))
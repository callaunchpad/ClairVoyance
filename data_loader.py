import numpy as np
import cv2

class DataLoader():
    
    def __init__(self, npy_file):
        self.mnist_size = 10000
        self.video_length = 4000
        self.img_w = 64
        self.img_h = 64
        self.video_channels = 1
        self.video_num_frames = 20
        self.raw_data = np.load(npy_file)
        self.dataset = np.empty([self.video_length, self.video_num_frames, self.img_h, self.img_w, self.video_channels], dtype=np.float32)
    
    def load(self):
        for i in range(6001, self.mnist_size):
            vid = np.expand_dims(self.raw_data[:,i,:,:], axis=3)
            self.dataset[i-6001,:,:,:] = vid.copy()
        return self.dataset

    def save_images(self):
        count = 0
        for im in self.dataset:
            cv2.imwrite("data/img"+str(count)+".png", im)
            count += 1


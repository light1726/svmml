import os
import numpy as np
import config as conf

def load_data():
    train_path = conf.train_path
    test_path = conf.test_path
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    for file in os.listdir(train_path):
        f = open(file, 'r')

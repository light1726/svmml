import os
import numpy as np
import config as conf


def read_text(filepath):
    data = []
    data_labels = []
    for file in os.listdir(filepath):
        f = open(os.path.join(filepath, file), 'r')
        data_labels.append(int(file[0]))
        tempdata = []
        for line in f:
            for c in line.strip("\n"):
                tempdata.append(c)
        f.close()
        data.extend(tempdata)
    data = np.array(data)
    data = np.reshape(data, (-1, conf.data_dim))
    return data, data_labels


def load_data():
    train_path = conf.train_path
    test_path = conf.test_path
    train_data, train_labels = read_text(train_path)
    test_data, test_labels = read_text(test_path)
    return train_data, train_labels, test_data, test_labels

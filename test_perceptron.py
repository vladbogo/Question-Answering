import sys
import pickle
import neurolab as nl
import numpy as np

def main(argv):

    q = pickle.load(open('./corpus/corpus2vec.np', 'rb'))
    classes = pickle.load(open('./corpus/class.np', 'rb'))
    
    # Load perceptron
    net = nl.load('perceptron.net')

    # Simulate network
    q_test = q[26801:]
    classes_test = classes[26801:]
    out = net.sim(q_test)

    print classes_test

    corect = 0
    for i in range(len(classes_test)):
        print out[i]
        if classes_test[26801 + i] == out[i]:
            corect = corect + 1

    print corect, len(out)

if __name__ == "__main__":
    main(sys.argv)

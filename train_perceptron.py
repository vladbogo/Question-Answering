import sys
import pickle
import neurolab as nl
import numpy as np

def main(argv):

    q = pickle.load(open('./corpus/corpus2vec.np', 'rb'))
    classes = pickle.load(open('./corpus/class.np', 'rb'))
    
    classes_train = classes[:26800]
    inp = q[:26800]
    tar = classes_train.reshape(len(classes_train), 1)

    vec_size = len(q[1])

    # Define size for input perceptrons
    input_perceptrons = []
    for i in range(vec_size):
        input_perceptrons.append([-1, 1])

    hidden_layer_size = 2 * vec_size

    # Create perceptron
    net = nl.net.newp(input_perceptrons, 1)

    # Train perceptron
    error = net.train(inp, tar, epochs=100, show=100, goal=0.02)

    # Simulate network
    q_test = q[26801:]
    classes_test = q[26801:]
    out = net.sim(q_test)

    net.save('perceptron.net')

    corect = 0
    for i in range(len(classes_test)):
        if classes_test[i] == out[i]:
            corect = corect + 1

    print corect, len(out)

if __name__ == "__main__":
    main(sys.argv)

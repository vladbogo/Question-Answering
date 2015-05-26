import sys
from gensim.models import Word2Vec

def main(argv):
    # TODO load model
    m = Word2Vec.load_word2vec_format(argv[0], binary=True)
    
    # Read questions from stdin
    while True:
        question = raw_input('Enter your question (EXIT to stop):')

        # Stop 
        if question == 'EXIT':
            break
        
        # Get words
        question = question.split(' ');

        v1 = raw_input('Choice 1:')
        v2 = raw_input('Choice 2:')
        v3 = raw_input('Choice 3:')
        v4 = raw_input('Choice 4:')

        # Compute similarity
        s1 = m.n_similarity(question, [v1])
        s2 = m.n_similarity(question, [v2])
        s3 = m.n_similarity(question, [v3])
        s4 = m.n_similarity(question, [v4])
        s = min(s1, s2, s3, s4)

        if s == s1:
            print "The answer is: " ,v1
        elif s == s2:
             print "The answer is: " ,v2
        elif s == s3:
            print "The answer is: " ,v3
        elif s == s4:
            print "The answer is: " ,v4

if __name__ == "__main__":
    main(sys.argv[1:])


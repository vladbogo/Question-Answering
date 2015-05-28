import sys
from gensim.models import Word2Vec
from nltk.corpus import stopwords

def main(argv):
    # TODO load model
    m = Word2Vec.load_word2vec_format(argv[0], binary=True)
    
    # Read questions from stdin
    while True:
        question = raw_input('Enter your question (EXIT to stop):')

        # Stop 
        if question == 'EXIT':
            break
        

        stops = set(stopwords.words("english"))
        # Get words
        question = question.lower().split(' ');
        question = [w for w in question if not w in stops]
        question = [argv[1] + s for s in question]

        #print question

        v1 = raw_input('Choice 1:').lower().split(' ')
        v2 = raw_input('Choice 2:').lower().split(' ')
        v3 = raw_input('Choice 3:').lower().split(' ')
        v4 = raw_input('Choice 4:').lower().split(' ')

        # Compute similarity
        s1 = m.n_similarity(question, v1)
        s2 = m.n_similarity(question, v2)
        s3 = m.n_similarity(question, v3)
        s4 = m.n_similarity(question, v4)
        s = max(s1, s2, s3, s4)

        if s == s1:
            print "The answer is: " ,v1
        elif s == s2:
             print "The answer is: " ,v2
        elif s == s3:
            print "The answer is: " ,v3
        elif s == s4:
            print "The answer is: " ,v4

if __name__ == "__main__":
    argv = sys.argv
    if len(sys.argv) < 2:
        sys.exit("Usage: qa_interactive model.bin [append]")
    elif len(sys.argv) == 2:
        argv.append("")
    main(argv[1:])


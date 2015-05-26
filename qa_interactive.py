from gensim.models import Word2Vec

def main():
    # TODO load model


    # Read questions from stdin
    while True:
        question = raw_input('Enter your question (EXIT to stop):')
        if question == 'EXIT':
            break
        v1 = raw_input('Choice 1:')
        v2 = raw_input('Choice 2:')
        v3 = raw_input('Choice 3:')
        v4 = raw_input('Choice 4:')

        print question

main()


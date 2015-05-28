import sys
from gensim.models import Word2Vec
import pandas as pd
import numpy
import pickle
from nltk.stem import WordNetLemmatizer

def phrase2vec(phrase, m, freebase, lemmatize):
    #print len(m['car'])
    phr = []
    cuv = 0
    wnl = WordNetLemmatizer()
    for word in phrase.split(' '):
        word = word.lower()
        word = freebase+word
        if lemmatize:
            word = wnl.lemmatize(word)
        try:
            m[word]
            phr.append(word)
        except:
            pass
    return phr

def main(argv):
    # TODO load model
    #m = Word2Vec.load_word2vec_format(argv[0], binary=True)
    m = Word2Vec.load(argv[0])
    corpus = pd.read_csv('./corpus/corpus.tsv', sep='\t')
    question = corpus.question.tolist()
    answer = corpus.answer.tolist()
    cl = corpus['class'].tolist()
    total = 0
    corect = 0
    for i in range(len(question)/4):
        print i
        try:
            """quest = question[i].split(' ')
            quest = [argv[1] + s.lower() for s in quest]
            ans1 = answer[i].split(' ')
            ans1 = [argv[1] + s.lower() for s in ans1]
            ans2 = answer[i+1].split(' ')
            ans2 = [argv[1] + s.lower() for s in ans2]
            ans3 = answer[i+2].split(' ')
            ans3 = [argv[1] + s.lower() for s in ans3]
            ans4 = answer[i+3].split(' ')
            ans4 = [argv[1] + s.lower() for s in ans4]
            """
            lemm = False
            quest = phrase2vec(question[i], m, argv[1], lemm)
            ans1 = phrase2vec(answer[i], m, argv[1], lemm)
            ans2 = phrase2vec(answer[i+1], m, argv[1], lemm)
            ans3 = phrase2vec(answer[i+2], m, argv[1], lemm)
            ans4 = phrase2vec(answer[i+3], m, argv[1], lemm)
            #print quest
            s1 = m.n_similarity(quest, ans1)
            s2 = m.n_similarity(quest, ans2)
            s3 = m.n_similarity(quest, ans3)
            s4 = m.n_similarity(quest, ans4)
            s = max(s1, s2, s3, s4)
            total = total + 1
            if not (cl[i] == 1 or cl[i+1] == 1 or cl[i+2] == 1 or cl[i+3] == 1):
                print "Gresit!!!"
            if s == s1:
                if cl[i] == 1:
                    corect = corect+1
            elif s == s2:
                if cl[i+1] == 1:
                    corect = corect+1
            elif s == s3:
                if cl[i+2] == 1:
                    corect = corect+1
            elif s == s4:
                if cl[i+3] == 1:
                    corect = corect+1
            print corect
        except:
            pass
    print "final"
    print corect
    print total

if __name__ == "__main__":
    main(sys.argv[1:])


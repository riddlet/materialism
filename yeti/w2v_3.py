import pandas as pd
import numpy as np
import spacy
from spacy.en import English
from nltk import sent_tokenize
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from scipy import spatial
from scipy.stats.stats import pearsonr
import seaborn as sns

def w2vsim(text, vector, spacy_mod, w2v_mod):
    w = spacy_mod.tokenizer(text.decode('utf8'))
    if w.orth_ in w2v_mod.vocab:
        text_vec = model.word_vec(w.orth_)
    else:
        return(0)

    return(1-spatial.distance.cosine(vector, text_vec))

def main():
	nlp = spacy.load('en')
	model = KeyedVectors.load_word2vec_format('../../w2v/GoogleNews-vectors-negative300.bin.gz', binary=True)
	df = pd.read_csv('../word_topic_deflections.csv')
	start = 600000
	stop = 899999

	df_results = pd.DataFrame({'words':model.index2word[start:stop],
                          'low_cor':0,
                          'med_cor':0,
                          'high_cor':0})
	low_cor = [0]*len(model.index2word[start:stop])
	med_cor = [0]*len(model.index2word[start:stop])
	high_cor = [0]*len(model.index2word[start:stop])
	for i, word in enumerate(model.index2word[start:stop]):
		if not i % 30000:
			print 'starting at %s, file %s ' %(start, i)
			
		tempvec = model.word_vec(word)
		df['temp'] = df.words.apply(w2vsim, args=[tempvec, nlp, model])

		low_cor[i] = pearsonr(df.temp, df.low)[0]
		med_cor[i] = pearsonr(df.temp, df.med)[0]
		high_cor[i] = pearsonr(df.temp, df.high)[0]

	df_results['low_cor'] = low_cor
	df_results['med_cor'] = med_cor
	df_results['high_cor'] = high_cor

	df_results.to_csv('cor_3.csv', index=False)

if __name__ == '__main__':
    main()
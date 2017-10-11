import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from scipy import spatial
from scipy.stats.stats import pearsonr


def w2vsim(w, vector, w2v_mod):
    if w in w2v_mod.vocab:
        text_vec = model.word_vec(w)
    else:
        return(0)

    return(1-spatial.distance.cosine(vector, text_vec))

def main():
	model = KeyedVectors.load_word2vec_format('../../w2v/GoogleNews-vectors-negative300.bin.gz', binary=True)
	df = pd.read_csv('../word_topic_deflections.csv')
	start = 1800000
	stop = 2099999

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

	df_results.to_csv('cor_7.csv', index=False)

if __name__ == '__main__':
    main()
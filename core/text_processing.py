from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist = FreqDist(words)
    ranking = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if i not in ranking:
                    ranking[i] = freq_dist[word]
                else:
                    ranking[i] += freq_dist[word]

    top_sentences_index = nlargest(num_sentences, ranking, key=ranking.get)
    summarized_text = [sentences[i] for i in sorted(top_sentences_index)]
    return " ".join(summarized_text)

def suggest_keywords(text, num_keywords=5):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist = FreqDist(words)
    return [word for word, _ in freq_dist.most_common(num_keywords)]

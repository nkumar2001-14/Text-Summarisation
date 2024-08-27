'''install python
install pip
pip install flask
pip install googletrans==3.1.0a0
pip install gTTS  
pip install pyttsx3
pip install IPython'''

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from gtts import gTTS
from IPython.display import Audio
from googletrans import Translator
def summarize(text,t):
    translator = Translator()
    nltk.download('punkt')
    nltk.download("stopwords")

    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))
    filtered_words = [word for word in words if word not in stop_words]
    word_frequencies = nltk.FreqDist(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = ' '.join(summary_sentences)

    out = translator.translate(summary,dest=t)

    tts = gTTS(out.text)

    f=open("./static/audio/name.txt", "r")
    fname=f.read()
    f.close()
    if(fname==""):
        sr=1
    else:
        sr=int(fname)+1

    f=open("./static/audio/name.txt","w")
    f.write(str(sr))
    f.close()

    url="./static/audio/"+str(sr)+".wav"

    tts.save(url)
    return [out.text,url]

'''print("Length of original text :",len(text.split(' ')))
print(summary)
print("Length of Summery:",len(summary.split(' ')))

print(out.text)
print("Length of Summery:",len(out.text.split(' ')))
out = translator.translate(summary,dest='hi')
print(out.text)
print("Length of Summery:",len(out.text.split(' ')))

tts = gTTS(summary)
tts.save('1.wav')
sound_file = '1.wav'
Audio(sound_file, autoplay=True)



tts = gTTS(out.text)
tts.save('1.wav')
sound_file = '1.wav'
Audio(sound_file, autoplay=True)'''


import json
import spacy
import nltk
import re
from string import punctuation

# age bias detector ------------------------------------

nlp = spacy.load('en_core_web_lg')

def clean_doc(doc):
    doc = doc.lower()
    doc = re.sub(f"[{re.escape(punctuation)}]", " ", doc)
    doc = " ".join(doc.split())
    return doc





def get_similarity_result(DICTIONARY, t):

    data = clean_doc(t)


### Tagging parts of speech

### download if starting in new environment
#nltk.download('averaged_perceptron_tagger')
    tokens =nltk.word_tokenize(data)

## tokens_tag will contain the tagged parts of speech
    tokens_tag = nltk.pos_tag(tokens)

    j=0

# pronoun list
    prn_list = [ 'HE','SHE', 'HIS', 'HER', 'HE/SHE', 'HIM/HER', 'HIS/HER' , 'HIS/HERS', 'HIMSELF/HERSELF' ]
### Pronoun detection
    for word,pos in tokens_tag:
            if (pos == 'PRP' or pos == 'PRP$'):
                if (word in list(map(str.lower, prn_list))):
            	    j += 1
                    thisitem = {
                    "id":'gender'+ str(j),
                    "category":'Gender Bias',
                    "reason":'Gender specific pronoun',
                    "original":word
                    }
                    DICTIONARY.append(thisitem)
                    print("Gender specific pronoun ---->> ", word)



# list of masculine and feminine coded adjectives
    m_words = ["active","adventurous","aggressive","ambitious","analysing","assertive","athletic","autonomous","boasting","challenging","competitive","confident","courageous","decid","decision","decisive","determined","dominating","dominant","forceful","greedy","head-strong","headstrong","hierarchical","hostile","impulsive","independent","individual","intellectual","leader","logic","masculine","objective","opinion","outspoken","persistant","principled","reckless","self-confident","self-reliant","self-sufficient","selfconfident","selfreliant","selfsufficient"]

    f_words = ["affectionate","childish","cheerful","collaborative","committed","communal","compassionate","connected","considerate","cooperative","dependable","emotional","empathatic","feminine","flatterable","gentle","honest","interpersonal","interdependent","interpersonal","kind","kinship","loyal","modesty","nagging","nurturing","pleasant","polite","quiet","responsible","sensitive","submissive","supportive","sympathatic","tender","together","trust","understand","warm","whin","yield"]






# These store number of gendered words in the sentence

    m_count = 0
    f_count = 0

    m_list = [ ]
    f_list = [ ]

#for word in tokens_tag:
#
#    if ps.stem(word[0]) in m_words:
#
#        m_count+=1
#        print(word[0], " -> stereotypical masculine word" )
#        m_list.append(word[0])
#
#    if ps.stem(word[0]) in f_words:
#        f_count+=1
#        print(word[0], " -> stereotypical feminine word" )
#        f_list.append(word[0])

######
    tokens1 = nlp(data)



    for word in tokens1:

        for m_word in m_words:
            if word.similarity(nlp(m_word)) > 0.90:

                m_count+=1
                print(word, " -> stereotypical masculine word" )

                j += 1
                thisitem = {
                    "id":'gender'+ str(j),
                    "category":'Gender Bias',
                    "reason":'Stereotypical Masculine word ',
                    "original":word
                    }
                DICTIONARY.append(thisitem)

                m_list.append(word)
                break

        for f_word in f_words:
            if word.similarity(nlp(f_word)) > 0.90:

                f_count+=1
                print(word, " -> stereotypical feminine word" )


                j += 1
                thisitem = {
                    "id":'gender'+ str(j),
                    "category":'Gender Bias',
                    "reason":'Stereotypical feminine word ',
                    "original":word
                    }
                DICTIONARY.append(thisitem)

                f_list.append(word)
                break

#if no bias detected, return a null result
    if DICTIONARY == []:
        thisitem = {
            "id":'blank',
            "category":'Gender Bias',
            "reason":'blank',
            "original":'blank'
            }

        DICTIONARY.append(thisitem)

    return DICTIONARY




def save_result_json(DICTIONARY, age_filename):

    if DICTIONARY == []:
        thisitem = {
                "id":'blank',
                "category":'Gender Bias',
                "reason":'blank',
                "orignal":'blank'
            }

        DICTIONARY.append(thisitem)

    outfile = open(age_filename, 'w')
    json.dump(DICTIONARY, outfile, indent = 2)
    outfile.close()

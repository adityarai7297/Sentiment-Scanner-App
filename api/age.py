
import json
import spacy
import re
from string import punctuation

# age bias detector ------------------------------------

nlp = spacy.load('en_core_web_lg')

def clean_doc(doc):
    doc = doc.lower()
    doc = re.sub(f"[{re.escape(punctuation)}]", " ", doc)
    doc = " ".join(doc.split())
    return doc

def get_single_trigram(doc,position,size=3):
    count = 0
    trigram = ''

    while count < size and position <= len(doc):

        if doc[position].has_vector:
            trigram = trigram + ' ' + doc[position].text
            count += 1

        position += 1

    return trigram.lstrip()


def get_single_trigram_similarity(DICTIONARY, trigram):

#doc 1: phrases from AGE_LIST
#doc 2: each trigram
#DICTIONARY: a global variable to store result

    doc2 = nlp(trigram)
    j = len(DICTIONARY)

    first_find = bool(True)
    thisitem = {}

    for category in AGE_LIST:
        for item in AGE_LIST[category]:

            doc1 = nlp(item)
            similarity = doc1.similarity(doc2)

            if similarity > 0.90:

                #in case each trigram have multiple matches
                if first_find:
                    j += 1
                    thisitem = {
                            "id":'age'+ str(j),
                            "category":'Age Bias',
                            "reason":str(category),
                            "original":str(doc2)
                        }
                    first_find = False

                print ('************',doc1, '<---->', doc2, similarity)

    return thisitem

def get_similarity_result(DICTIONARY, t,size=3):

#DICTIONARY: a global variable to store result

    prev = 0
    previtem = {}

    doc = nlp(clean_doc(t))


    for i in range(0,len(doc)-size+1):

        #get each trigram from the cleaned document
        trigram = get_single_trigram(doc,i,size)

        #compare each trigram with all items from the AGE_LIST
        thisitem = get_single_trigram_similarity(DICTIONARY, trigram)

        if thisitem:
            #merge clusters of trigrams( a long phrase) into one entry
            if i-1 == prev:
                DICTIONARY[-1]["original"] += ' ' + thisitem["original"].split(' ')[-1]
            else:
                DICTIONARY.append(thisitem)

            prev = i
            previtem = DICTIONARY[-1]

    #if no bias detected, return a null result
    if DICTIONARY == []:
        thisitem = {
                "id":'blank',
                "category":'Age Bias',
                "reason":'blank',
                "original":'blank'
            }

        DICTIONARY.append(thisitem)

    return DICTIONARY


def save_result_json(DICTIONARY, age_filename):

    if DICTIONARY == []:
        thisitem = {
                "id":'blank',
                "category":'Age Bias',
                "reason":'blank',
                "original":'blank'
            }

        DICTIONARY.append(thisitem)

    outfile = open(age_filename, 'w')
    json.dump(DICTIONARY, outfile, indent = 2)
    outfile.close()


#------------------------------------------
AGE_LIST = {}

AGE_LIST['less attractive'] = ['neat', 'attractive']
AGE_LIST['hard of hearing'] = ['hard of hearing',
                           'worse hearing',
                           'speak too softly',
                           'frustrated when not hearing',
                           'speak too fast',
                           'often ask others to repeat']
AGE_LIST['worse memory'] = ['worse memory']
AGE_LIST['less physically able'] = ['physical capacity',
                                'physical capability and health',
                                'sedentary',
                                'physically handicapped',
                                'slow moving',
                                'sick',
                                'shaky hands',
                                'fragile',
                                'poor posture',
                                'physically demanding job',
                                'tired','incompetent',
                                'lower activity',
                                'high energy','high speed','energetic',
                                'physically active','psychomotor speed']

AGE_LIST['less adaptable'] = ['flexible with','try new approaches',
                          'occupationally flexible',
                          'grasp new ideas',
                          'change',
                          'old-fashioned',
                          'adapt to change',
                          'talks of past','focuses away from future toward past']

# positive stereotypes mentioned in the paper
AGE_LIST['careful'] = ['think before they act','cautious',
                   'self-discipline',
                   'better practical judgment','better common sense']

AGE_LIST['less creative'] = ['lower creativity']

AGE_LIST['dependable'] = ['loyal','more stability', 'more reliable','committed to the organization',
                      'stable', 'trustworthy','reliability','commitment',
                      'loyalty','job commitment','more trustworthy']

AGE_LIST['negative personality'] = ['dejected','poor','hopeless','unhappy',
                                'lonely','insecure','complains a lot','grouchy','critical','miserly',
                                'less pleasantness', 'ill-tempered','bitter','demanding',
                                'complaining','annoying','humorless','selfish','prejudiced',
                                'suspicious of strangers','easily upset','miserly','snobbish',
                                'less friendliness','less cheerfulness']

AGE_LIST['warm personality'] = ['warm','good-natured','benevolent','amicable','warm personality',
                            'more conscientious','warm']

AGE_LIST['lower ability to learn'] = ['learn new techniques','personal development',
                                  'potential for development',
                                  'willingness to be trained',
                                  'ability to learn', 'training program',
                                  'interest in learning', 'learn quickly']

AGE_LIST['worse communication skills'] = ['unable to communicate',
                             'interpersonal skills',
                             'talks slowly', 'less sociable',
                             'worse conversational skills',
                             'hard to understand when noisy',
                             'lose track of who said what', 'lose track of topic',
                             'lose track of what talked about', 'hard to speak if pressed for time',
                             'use fewer difficult words',
                             'less outgoing',
                             'quieter voice', 'more hoarse']

AGE_LIST['less productive'] = ['lower performance capacity',
                           'less economically beneficial',
                           'high performance rating',
                           'less competence']

AGE_LIST['worse with tech'] = ['understand new technologies',
                        'learn new technologies',
                        'comfortable with new technologies',
                        'deal with new technologies',
                        'technological competence', 'technological adaptability',
                        'accept new technology',
                        'digital native']

AGE_LIST['maximun experience'] = ['maximum 5 years experience',
                           'no more than 5 years experience',
                                 'recent college grad','3 to 5 years of experience required','young']

## positive stereotypes -- "better communication skills"," more productive", "more experienced"


# ORIGINAL = """Required Technical Qualifications:
# •	You are a digital native adapt to new technologies quickly
# •	Maximum 3 years experience in network engineering in an enterprise environment.
# •	Experience with all aspects of Wi-Fi (802.11) operation and implementation at an enterprise level.
# •	Knowledge of networking protocols and networking theory.
# •	Analyze and solve complex technical problems.
# """

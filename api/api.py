from flask import Flask, request, jsonify
import age
import gender
import json

class Result:
    name = 'bias result'
    text = ''
    agebias = []

# used when deploy to heroku -> failed
# app = Flask(__name__, static_folder='../build', static_url_path='/')

#local development
app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/submit', methods=['POST'])
def submit():
    submit_data = request.get_json()

    if not submit_data:
        return jsonify({'msg': 'Missing JSON'}), 400
    else:
        print(type(submit_data))

        # age bias detector
        DICTIONARY = []
        AGE_RESULT = age.get_similarity_result(DICTIONARY,submit_data)

        #gender bias detector
        DICTIONARY = []
        GENDER_RESULT = gender.get_similarity_result(DICTIONARY,submit_data)

        # age.save_result_json(AGE_RESULT,'agedata.json')

        return jsonify(get_result_data(submit_data, AGE_RESULT, 'agedata.json'))




def get_result_data(original,age_result,age_filename):

    # age_file = './' + age_filename

    # with open(age_file) as f:
    #     data = json.load(f)

    myresult = Result()
    myresult.agebias = age_result
    myresult.genderbias = gender_result
    myresult.text = original

    myresultStr = json.dumps(myresult.__dict__)
    print('ready to sent to frontend')

    return myresultStr

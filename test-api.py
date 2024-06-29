import os
from flask import Flask
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

question = api.model('Question', {
    'question': fields.String(required=True, description='Ask the question')
})

@api.route('/qna')
class QnA(Resource):

    @api.expect(question)
    def post(self):
        """ 
        Answer the question
        """

        # TODO: Impplement the logic to answer the question


        return {'Answer': f'answer for question {api.payload.get("question")}'}

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)

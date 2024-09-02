from flask import Flask, render_template, request, jsonify
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import yaml
from resumeparser import pdf_reader,parse_data,get_score,get_suggestion
import json
UPLOAD_PATH = r"__DATA__"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


api_key = None
CONFIG_PATH = r"config.yaml"
with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GOOGLE_API_KEY']

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

@app.route('/', methods=['GET','POST'])
def index():        
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def result():
    resume = request.files['pdf_doc']
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
    resume.save(resume_path)
    resume_text = pdf_reader(resume_path)
    parsed_data = parse_data(llm,resume_text)
    suggetions = get_suggestion(llm,resume_text)
    suggetions= suggetions.split("\n")
    score = get_score(llm,resume_text)
    return  render_template("display_result.html",user=parsed_data,s=suggetions,score=score)


if __name__ == '__main__':
    app.run(debug=True)

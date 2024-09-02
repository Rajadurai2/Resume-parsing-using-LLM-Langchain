# FLASK APP - Run the app using flask --app app.py run
import os, sys
from flask import Flask, request, render_template
#from pypdf import PdfReader 
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import yaml
from resumeparser import pdf_reader,parse_data
sys.path.insert(0, os.path.abspath(os.getcwd()))


api_key = None
CONFIG_PATH = r"config.yaml"

with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GOOGLE_API_KEY']


UPLOAD_PATH = r"__DATA__"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def ats():
    doc = request.files['pdf_doc']
    doc.save(os.path.join(UPLOAD_PATH, "file.pdf"))
    doc_path = os.path.join(UPLOAD_PATH, "file.pdf")
    #llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

    #resume_text = pdf_reader(doc_path)
    #data = parse_data(llm,resume_text)

    #return render_template('index.html', data = data)

            
    data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "postalCode": {
                "code": 12345,
                "extended": 6789
                }
            },
            "hobbies": ["reading", "traveling", "coding"],
            "education": {
                "highSchool": "Anytown High",
                "college": {
                    "name": "University of Somewhere",
                    "degree": "Computer Science",
                    "year": 2022
                    }
                }
            }

    return render_template('index.html',data=data)
 

if __name__ == "__main__":
    app.run(port=8000, debug=True)


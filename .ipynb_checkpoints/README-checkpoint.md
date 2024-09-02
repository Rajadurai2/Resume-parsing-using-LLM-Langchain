# Resume Parser Using Large Language Models and Langchain
#### Problem with Traditional ATS Software: 
Traditional ATS systems often require manual adjustments for different job domains and industries. This means each ATS setup needs to be customized for various fields, leading to a lot of time and effort spent on configuring and maintaining different parsing rules and keyword sets for each domain. This approach is not only labor-intensive but also prone to inconsistencies and errors.

#### How AI Improves This:: 
AI-powered resume parsers automatically adapt to various job domains without needing manual adjustments. They use advanced machine learning algorithms and NLP to understand and extract relevant information from resumes across different industries and job roles. This reduces the need for domain-specific customization, streamlining the process and ensuring more consistent and accurate parsing of resumes.

## Model used here
### gemini-pro
The Gemini-Pro model is an advanced AI-driven tool designed to enhance resume parsing and job matching processes. It leverages state-of-the-art machine learning and natural language processing techniques to provide accurate and detailed insights from resumes and job descriptions.

Create free access token here https://ai.google.dev/gemini-api/docs/models/gemini
#### Usage: 
Just upload your resume in pdf format, and see for yourself :


##### Running the program

1. Clone this Repository
   ```bash
   git clone https://github.com/Rajadurai2/Resume-parsing-using-LLM-Langchain.git
3. Change to the directory 
   ```bash
   cd Resume-parsing-using-LLM-Langchain
4. Create a pythonvirtual env
   ```bash
   python -m venv your_venv_name
5. activate venv
   ```bash
   source env/bin/activate    //linux
   .env/Scripts/activate.bat  //windows
6. Install requirements files
   ```bash
   pip intall -r requirements.txt
7. Open config.yaml file and put your api key
   ```bash
    GOOGLE_API_KEY: "your-api-key"
8. run the flask app
    ```
    python dash.py
    
    check: https://localhost:5000
    ```
### Snapshots
# index page

<img src="screenshots/image.png">

# Parsing details

<img src="screenshots/details.png">

# Resume scoring and suggestion 

<img src="screenshots/score.png">
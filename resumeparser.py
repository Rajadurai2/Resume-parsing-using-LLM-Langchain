# import libraries

import yaml

from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io, random

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser 
import json
api_key = None

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text


def parse_data(llm,resume_text):
        # Define the prompt template for parsing resumes
    # resume_parsing_prompt = PromptTemplate(
    #     input_variables=["resume_text"],
    #     template="Parse the following resume and extract person details,relevant skills, experiences, and qualifications:\n\n{resume_text}\n\nOutput as JSON."
    # )

    resume_parsing_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template=(
        "Parse the following resume and extract the person details, relevant skills, experiences, and qualifications. "
        "Ensure the output is a JSON object with the following keys: "
        "'personDetails', 'skills', 'experiences', 'certifications','qualifications','achievements','projects','hobbies'. "
        "If a field is not available, return it as an empty string or an empty list.\n\n"
        "{resume_text}\n\n"
        "Output as dict with the specified keys."
    )
)
    output_parser = JsonOutputParser()
    parsing_chain = LLMChain(llm=llm, prompt=resume_parsing_prompt,output_parser=output_parser)
    parsed_data = parsing_chain.run({"resume_text": resume_text})
    #parsed_data = json.loads("".join(parsed_data.split("\n")[1:-1]))
    return parsed_data

def get_score(llm,resume_text):
    output_parser = JsonOutputParser()
    ranking_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="Rate this resume 0 - 10 for each criteria grammar_mistakes,skills,projects "
    "Ensure the output is a JSON object with the following keys: "
        "'grammar_mistakes','skills','projects'. "
    ":\n\n{resume_text}\n\nOutput as dict")

    rank_chain = LLMChain(llm=llm, prompt=ranking_prompt,output_parser=output_parser)
    rank = rank_chain.run({"resume_text":resume_text})
    #rank = json.loads("".join(rank.split("\n")[1:-1]))
    return rank

def get_suggestion(llm,resume_text):
    #output_parser = JsonOutputParser()
    get_mistakes = PromptTemplate(
    input_variables=["resume_text"],
    template="Tell 10 suggetions to improve this resume:\n\n{resume_text}\n\nOutput as string lists")

    suggestion_chain = LLMChain(llm=llm,prompt=get_mistakes)
    suggestions = suggestion_chain.run({"resume_text":resume_text})
    return suggestions
# ai_model.py
import google.generativeai as genai
import os

# Set up the API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

def generate_question(algorithm, previous_questions):
    prompt = f"""
    You are a Socratic tutor teaching about the {algorithm} sorting algorithm. 
    Generate a thought-provoking question about {algorithm} that encourages 
    deep understanding. The question should not be a simple fact recall, but 
    should prompt the student to think critically about the algorithm's 
    mechanics, efficiency, or applications.

    Previous questions asked (do not repeat these):
    {previous_questions}

    Generate a new question:
    """

    response = model.generate_content(prompt)
    return response.text

def evaluate_answer(question, answer, algorithm):
    prompt = f"""
    You are a Socratic tutor evaluating a student's understanding of the {algorithm} sorting algorithm.
    
    The question asked was: "{question}"
    
    The student's answer is: "{answer}"
    
    Evaluate the student's answer, considering the following:
    1. Accuracy of the information provided
    2. Depth of understanding demonstrated
    3. Any misconceptions or areas that need clarification
    
    Then, formulate a follow-up question or comment that will guide the student 
    to deepen their understanding or correct any misconceptions. Your response 
    should be in the Socratic style, encouraging the student to think critically 
    rather than simply providing correct information.

    Provide your evaluation and follow-up in the following format:
    Evaluation: [Your evaluation here]
    Follow-up: [Your follow-up question or comment here]
    """

    response = model.generate_content(prompt)
    return response.text

def generate_explanation(algorithm, concept):
    prompt = f"""
    Explain the concept of {concept} in the context of the {algorithm} sorting algorithm. 
    Your explanation should be clear, concise, and suitable for a student who is 
    learning about sorting algorithms. Include an example if appropriate.
    """

    response = model.generate_content(prompt)
    return response.text
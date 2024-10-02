import streamlit as st
import os
from sorting_algorithms import bubble_sort, quick_sort
from ai_model import generate_question, evaluate_answer, generate_explanation
from code_execution import execute_code
from performance_analyzer import analyze_performance
from visualization import visualize_algorithm
import os

st.write(
    "Has environment variables been set:",
    os.environ["GOOGLE_API_KEY"] == st.secrets["GOOGLE_API_KEY"],
)

# Ensure the API key is set
if 'GOOGLE_API_KEY' not in os.environ:
    st.error("Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

def main():
    st.title("Socratic Learning Assistant for Sorting Algorithms")

    # Sidebar for algorithm selection
    algorithm = st.sidebar.selectbox("Select Sorting Algorithm", ["Bubble Sort", "Quick Sort"])

    # Main content area
    st.header(f"Learning {algorithm}")

    # Initialize session state
    if 'questions_asked' not in st.session_state:
        st.session_state.questions_asked = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = generate_question(algorithm, st.session_state.questions_asked)
        st.session_state.questions_asked.append(st.session_state.current_question)

    # Display current question
    st.write(st.session_state.current_question)

    # User input area
    user_answer = st.text_area("Your answer:")
    user_code = st.text_area("Your code implementation:")

    if st.button("Submit"):
    # Evaluate user's answer
        evaluation = evaluate_answer(st.session_state.current_question, user_answer, algorithm)
        st.write(evaluation)

        # Execute user's code
        if user_code:
            result, output = execute_code(user_code, algorithm)
            st.write("Code execution result:", result)
            st.write("Output:", output)

            # Analyze performance
            performance_analysis = analyze_performance(user_code, algorithm)
            st.write("Performance Analysis:", performance_analysis)

        # Generate next question
        st.session_state.current_question = generate_question(algorithm, st.session_state.questions_asked)
        st.session_state.questions_asked.append(st.session_state.current_question)

    # Explanation button
    if st.button("Get an Explanation"):
        concept = st.text_input("What concept would you like explained?")
        if concept:
            explanation = generate_explanation(algorithm, concept)
            st.write(explanation)

    if st.button("Visualize Algorithm"):
        st.write(f"Visualization for {algorithm}:")
        print("entered visual part")
        gif_data = visualize_algorithm(algorithm)
        st.image(gif_data)
if __name__ == "__main__":
    main()
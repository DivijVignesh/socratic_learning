# performance_analyzer.py
import timeit
import random

def analyze_performance(user_code, algorithm):
    # Prepare the test array
    test_array = random.sample(range(1000), 1000)
    
    # Setup code for user's implementation
    user_setup = f"""
{user_code}
test_array = {test_array}
"""
    
    # Setup code for built-in sorting
    builtin_setup = f"""
test_array = {test_array}
"""
    
    try:
        # Time the user's implementation
        user_time = timeit.timeit(
            f"{algorithm.lower().replace(' ', '_')}(test_array.copy())", 
            setup=user_setup, 
            number=100
        )
        
        # Time the built-in sorting
        builtin_time = timeit.timeit(
            "sorted(test_array)", 
            setup=builtin_setup, 
            number=100
        )
        
        # Compare performance
        if user_time < builtin_time * 1.5:
            return f"Great job! Your {algorithm} implementation is performing well. It took {user_time:.6f} seconds, while Python's built-in sort took {builtin_time:.6f} seconds."
        else:
            return f"Your {algorithm} implementation might need some optimization. It took {user_time:.6f} seconds, while Python's built-in sort took {builtin_time:.6f} seconds."
    
    except Exception as e:
        return f"An error occurred while analyzing performance: {str(e)}"
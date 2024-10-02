import traceback
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    import random
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def execute_code(code, algorithm):
    try:
        # Create a safe environment to execute the code
        globals_dict = {"bubble_sort": bubble_sort, "quick_sort": quick_sort}
        locals_dict = {}
        
        # Execute the code
        exec(code, globals_dict, locals_dict)
        
        # Check if the sorting function is defined
        sort_func = locals_dict.get(f"{algorithm.lower().replace(' ', '_')}")
        if not sort_func:
            return False, "Sorting function not defined correctly."
        
        # Test the sorting function
        test_array = [4, 2, 7, 1, 9, 3]
        result = sort_func(test_array)
        if result == sorted(test_array):
            return True, f"Success! The {algorithm} function correctly sorted the array."
        else:
            return False, f"The {algorithm} function did not correctly sort the array."
    except Exception as e:
        return False, f"Error executing code: {str(e)}\n{traceback.format_exc()}"

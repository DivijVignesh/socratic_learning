import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import io
import base64
import os

def visualize_algorithm(algorithm, array_size=30):
    # Generate random array
    arr = [random.randint(1, 100) for _ in range(array_size)]
    
    # Create figure and axis
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    # Set axis limits
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)
    
    # Set title
    ax.set_title(f"{algorithm} Visualization")

    # Text to display iteration count and comparisons
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    
    iteration = [0]
    
    # Define update function based on the chosen algorithm
    if algorithm == "Bubble Sort":
        def update_func(arr, rects, iteration):
            for i in range(len(arr) - 1):
                for j in range(len(arr) - 1 - i):
                    iteration[0] += 1
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr
    elif algorithm == "Quick Sort":
        # List to store the state of the array at each step for visualization
        steps = []

        def quick_sort(arr, low, high):
            if low < high:
                pivot_idx = partition(arr, low, high)
                # Store the current state of the array
                steps.append(arr[:])  # Store a copy of the current state
                quick_sort(arr, low, pivot_idx - 1)
                quick_sort(arr, pivot_idx + 1, high)

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                iteration[0] += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    # Store the current state of the array after a swap
                    steps.append(arr[:])  # Store a copy of the current state
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            # Store the state after the final swap
            steps.append(arr[:])  # Store a copy of the current state
            return i + 1  # Return the pivot index

        # Start the quicksort algorithm
        quick_sort(arr, 0, len(arr) - 1)

        def update_func(arr, rects, iteration):
            for state in steps:
                yield state  # Yield each state for animation

    else:
        raise ValueError("Unsupported algorithm")

    # Animation function
    def animate(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        text.set_text(f"Iterations: {iteration[0]}")
        return list(bar_rects) + [text]

    # Create animation
    anim = animation.FuncAnimation(
        fig,
        func=animate,
        frames=update_func(arr, bar_rects, iteration),
        interval=200,
        repeat=False,
        blit=True
    )

    # Save animation to a temporary file
    temp_filename = "temp_animation.gif"
    anim.save(temp_filename, writer='pillow', fps=30)
    
    # Read the temporary file into a BytesIO buffer
    with open(temp_filename, "rb") as f:
        buffer = io.BytesIO(f.read())
    
    # Remove the temporary file
    os.remove(temp_filename)

    # Convert buffer to base64 string
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    # Close the plot to free up memory
    plt.close(fig)
    
    return f"data:image/gif;base64,{img_str}"

# Example usage
# Uncomment the line below to visualize an algorithm
# gif_data = visualize_algorithm("Quick Sort", 30)

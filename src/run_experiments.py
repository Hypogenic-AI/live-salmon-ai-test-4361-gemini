import subprocess
import os

def run_step(script_name):
    print(f"\n--- Running {script_name} ---")
    result = subprocess.run(['python', f'src/{script_name}'], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERRORS:", result.stderr)

if __name__ == "__main__":
    os.makedirs('datasets/live_salmon', exist_ok=True)
    os.makedirs('results/papers', exist_ok=True)
    
    run_step('data_generator.py')
    run_step('ai_scientist.py')
    run_step('evaluator.py')
    
    print("\n--- Pipeline Completed ---")

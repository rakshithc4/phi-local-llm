import subprocess

def chat_with_phi():
    print("Chat with Phi (type 'exit' to quit):")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        result = subprocess.run(["ollama", "run", "phi"], input=prompt.encode(), capture_output=True)
        print("Phi:", result.stdout.decode())

if __name__ == "__main__":
    chat_with_phi()

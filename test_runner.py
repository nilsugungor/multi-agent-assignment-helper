from supervisor import SupervisorAgent

def main():
    supervisor = SupervisorAgent()

    sample_paraphrase = input("Enter the text you want to paraphrase.\n")
    sample_rewrite = input("Enter the text you want to rewrite in an academic way.\n")
    sample_notes = input("Enter the notes you want summarized.\n")
    audio_path = "/Users/nil/Desktop/om.ogg" 
    
    print("\n--- Paraphrased Text ---")
    print(supervisor.handle_request("paraphrase", sample_paraphrase))

    print("\n--- Academic Rewriting ---")
    print(supervisor.handle_request("rewrite", sample_rewrite))

    print("\n--- Summarized Notes ---")
    print(supervisor.handle_request("summarize", sample_notes))

    print("\n--- Transcribed Audio ---")
    print(supervisor.handle_request("transcribe_audio", audio_path))

if __name__ == "__main__":
    main()

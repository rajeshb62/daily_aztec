import whisper
import sys
import os

def transcribe_audio(audio_path, language="en", model_size="tiny", output_path=None):
    """
    Transcribe audio with improved settings for cleaner output.
    
    Parameters:
    audio_path (str): Path to input audio file
    language (str): Language code (e.g., 'en' for English)
    model_size (str): Whisper model size ('tiny', 'base', 'small', 'medium', 'large')
    output_path (str): Path for output text file
    """
    print(f"Loading {model_size} model...")
    model = whisper.load_model(model_size)
    
    print(f"Transcribing audio in {language}...")
    result = model.transcribe(
        audio_path,
        language=language,
        task="transcribe",
        fp16=False,
        initial_prompt="The following is a clear transcription of speech:",
        word_timestamps=True
    )
    
    # Get just the filename without path and extension
    base_filename = os.path.splitext(os.path.basename(audio_path))[0]
    
    # If output path specified, use it; otherwise create in current directory
    if output_path:
        if not output_path.endswith('.txt'):
            output_path = output_path + '.txt'
    else:
        output_path = f"./{base_filename}_transcript.txt"
    
    print(f"Saving transcript...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result["text"])
    
    print(f"Transcript saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <audio_file_path> [language] [model_size] [output_file_path]")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else "en"
    model_size = sys.argv[3] if len(sys.argv) > 3 else "tiny"
    output_file = sys.argv[4] if len(sys.argv) > 4 else None
    
    transcribe_audio(audio_file, language, model_size, output_file)
import os
from pathlib import Path
from dotenv import load_dotenv

from openai import OpenAI

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

## Specify API Key
load_dotenv()
client = OpenAI(
    api_key = os.getenv("API_KEY")
)

## Creates list of audio filenames to loop through
filename_list = []
folder_path = Path("Audio_Files")
# Get all files (excluding .DS_Store) from the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(folder_path / f) and f != '.DS_Store']
for n in file_names:
    file_path = folder_path / n
    filename_list.append(str(file_path))

## Loop that runs through each audio file and transcribes audio, then appends text to a list titled transcription_list
transcription_list = []
for n in filename_list:
  audio_file = open(n, "rb")
  transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
  transcription_list.append(transcription.text)

## Loop that runs through transcription_list and formats text on separate lines, then prints the transcript to the python console
print('Preparing transcript of communications... \n')
transcription_list_2 = []
for m in transcription_list:
    x = m.replace(".", ".\n")
    transcription_list_2.append(x)
    print(x)
print('Preparing blotter report... \n')

## Append the text transcript to a .csv titled Recordings_Transcripts.csv in case a separate transcript file is wanted (disabled at the moment)
#    csv_filename = 'Recordings_Transcripts.csv'
#    with open(csv_filename, 'w', newline='') as csvfile:
#      writer = csv.writer(csvfile)
#      for line in transcription_list:
#        writer.writerow([line])
#    print(f'Transcript saved to {csv_filename}')

## Prompt for GPT-4o interpretation of transcription
prompt = f"""
Instructions:
- The transcript of a recording is in {transcription_list_2}
- The transcript consists of law enforcement communications, give a concise summary of what you think each conversation is about and write each summary in the style of a newspaper article
- Include a title for each summary in newspaper article style using the format **Title**
"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(completion.choices[0].message.content)

# Function to create pdf file of GPT-4o response
def create_pdf_with_wrapped_text(file_name, text):
    # Create a document with a specified file name and page size
    document = SimpleDocTemplate(file_name, pagesize=letter)

    # Define the margin values (in points)
    margin_left = 50
    margin_right = 50
    margin_top = 750  # For top margin
    margin_bottom = 50

    # Set the width and height of the text area inside the margins
    width = letter[0] - margin_left - margin_right
    height = margin_top - margin_bottom

    # Prepare the style for text formatting (including line wrapping)
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica"
    style.fontSize = 12
    style.leading = 14  # Line height
    style.textColor = colors.black

    # Create a Paragraph object for the wrapped text
    paragraph = Paragraph(text, style)

    # Build the document with the Paragraph
    document.build([paragraph])

# Usage
text = completion.choices[0].message.content
create_pdf_with_wrapped_text("The_Sacramento_Blotter.pdf", text)
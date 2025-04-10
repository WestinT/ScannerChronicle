# ScannerChronicle
“The Scanner Chronicle” was designed to take audio files from public safety radio frequencies, transcribe them, and create a .pdf in the form of a newspaper summarizing the events in the audio files. 

## Goals
Many public safety agencies across the United States still broadcast their calls for service on radio frequencies that are unencrypted and available for public listening. This python script utilizes the OpenAI Whisper and GPT-4o API to transcribe the contents of this audio and summarize the contents in order to produce an AI generated “newspaper” report about current events based entirely on police radio traffic. Many newspapers to this day still print a “police blotter” as a dedicated section which is the inspiration behind “The Scanner Chronicle”. 

## How it Works
The OpenAI Whisper API is used to transcribe the contents of an audio file deposited into a folder titled “Audio_Files” by the user. A transcript of the audio is created, which is then fed into OpenAI’s GPT-4o model to product a concise summary in the style of a newspaper article, with its own title. 

Included in this repository is a sample audio file that includes 15 minutes of calls for the Sacramento Police Department. The audio file was recorded mid-day on February 26, 2025. 

## Requirements
- Python
Along with libraries:
- Os 
- Pathlib 
- Dotenv
- OpenAI
- Reportlab 

## How to Use
Download the files titled “Whisper.py” along with the sample audio file. Create a new folder containing the Whisper.py file, and within that folder, create another folder titled “Audio_Files” which is where all audio files should be deposited. Drag the sample audio file into the “Audio_Files” folder, and run the Whisper.py script. 

The result will be a transcript of the audio in the file, along with “The Scanner Chronicle” printout in the python console. In the project’s root folder, there will also be a .pdf file that contains “The Scanner Chronicle” in .pdf form after the script runs.

## Future Goals
- Better newspaper formatting within the .pdf file
- Calls grouped together based on who is receiving the call
- Revised GPT prompt that allows for more consistency each time the script runs
- Eliminate reliance on sac-radio.com for audio files
- Support for multiple file types (.wav, .mp4, etc.)

## Considerations
- Currently, none of this would be possible without access to the website sac-radio.com. Consider checking out their website http://www.sac-radio.com and donating to keep the system running. I have included their donation links below.
- Although any recording can be uploaded and transcribed, the GPT-4o prompt is structured around public safety agencies and has not been tested with other recordings
- Results may vary, and may not represent an accurate picture of what is occurring in the community 

## Donate to Sac-Radio
You can donate at either
Paypal: Donate@Sac-Radio.com
Venmo: @Adam-Batzianis

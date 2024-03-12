# Mehthod I used to create the samples:

## Step 1: Createing the raw texts
Based on what I wanted to have as the samples, I used the GPT4 to create samples. I asked the model to include the infoamtion I wanted to extreact by the LLM in the process. 

## Step 2: Text to speech using MetaVoice-1B 
The free [MetaVoice-1B](https://github.com/metavoiceio/metavoice-src) tool can be used to convert the text to voice files, assuming that the actual  input fils are supposed to be voicemails provided by the users. 

## Step 3: Voice to text using Open AI's Whisper
Then, as the final step for genrating the inputs, Open AI's speech recognation tool, [Whisper](https://github.com/openai/whisper) can be used to convert the voice to text file.


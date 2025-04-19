import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.text_to_speech.convert(
    text="Movies, oh my gosh, I just just absolutely love them. They are like time machines taking you to different worlds and landscapes, and um, and I just cant get enough of it.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)

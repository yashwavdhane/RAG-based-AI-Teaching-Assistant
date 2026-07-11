import whisper
import json
import os
model = whisper.load_model("large-v2")

audios = os.listdir("audios")
for audio in audios:
    num = audio.split(" ")[0]
    t = audio.split(".")[0].split(" ")[1:]
    title = " ".join(t)
    result = model.transcribe(audio = f"audios/{audio}",
                          language="hi",
                          task="translate",
                          word_timestamps=False)
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number":num, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

    chunks_metadata = {"chunks":chunks, "text":result["text"]}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_metadata,f)

    








# import whisper
# import json
# model = whisper.load_model("large-v2")
# result = model.transcribe(audio = "audios/2 When You’re Husband is a Tech Genius.mp3",
#                           language="hi",
#                           task="translate",
#                           word_timestamps=False)
# # print(result["text"])
# chunks = []
# for segment in result["segments"]:
#     chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

# print(chunks)

# with open("output.json", "w") as f:
#     json.dump(chunks,f)

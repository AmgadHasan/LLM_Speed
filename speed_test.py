import time
from transformers import AutoTokenizer
import transformers
import torch
from constants import prompt

size = "13"
model = f"NousResearch/Llama-2-{size}b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

sampling_params = {'do_sample':True,
    'temperature':0.1,
    'top_p':0.4,
    'num_return_sequences':1,
    'eos_token_id':tokenizer.eos_token_id,
    'max_length':1200,}

start = time.time()
print(f"Loading model:\t{model}")
chatbot = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)
end = time.time()
print(f"Loaded model {model} in {end-start} seconds")


with open("transcript.txt", 'r') as f:
    transcript = f.read()
print(transcript[:10])

input = prompt.format(transcript=transcript)
start = time.time()
sequences = chatbot(
    input,
    **sampling_params
)
end = time.time()
time = end-start
num_input_tokens = len(chatbot.tokenizer(input)['input_ids'])
num_total_tokens = len(chatbot.tokenizer(sequences[0]['generated_text'])['input_ids'])
num_output_tokens = num_total_tokens - num_input_tokens

speed = float(num_output_tokens) / time
print(f"Took {end-start} seconds to generate {num_output_tokens} tokens at speed {speed}")

with open(f"output/{size}+output.txt", 'w') as f:
    f.write(sequences[0]['generated_text'])
print("Done. results can be found at output.txt")
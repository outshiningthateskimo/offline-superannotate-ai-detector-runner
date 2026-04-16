import os
import json
import shutil
import torch
import pyfiglet
from transformers import AutoTokenizer
from generated_text_detector.utils.model.roberta_classifier import RobertaClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SA_BASE = os.path.join(
    BASE_DIR,
    "hf_models",
    "superannotate-ai-detector",
    "models--SuperAnnotate--ai-detector",
    "snapshots"
)

if not os.path.exists(SA_BASE):
    print("SuperAnnotate model not found. See README for setup instructions.")
    exit()

snapshot = os.path.join(SA_BASE, sorted(os.listdir(SA_BASE))[-1])

RB_BASE = os.path.join(
    BASE_DIR,
    "hf_models",
    "roberta-large",
    "models--FacebookAI--roberta-large",
    "snapshots"
)

if not os.path.exists(RB_BASE):
    print("RoBERTa-large model not found. See README for setup instructions.")
    exit()

roberta_snapshot = os.path.join(RB_BASE, sorted(os.listdir(RB_BASE))[-1])

config_path = os.path.join(snapshot, "config.json")
backup_path = os.path.join(snapshot, "config_backup.json")
with open(config_path) as f:
    config = json.load(f)
config["pretrain_checkpoint"] = roberta_snapshot
shutil.copy(config_path, backup_path)
with open(config_path, "w") as f:
    json.dump(config, f)

print("Loading model...")
try:
    tokenizer = AutoTokenizer.from_pretrained(snapshot)
    model = RobertaClassifier.from_pretrained(snapshot)
    model.eval()
finally:
    shutil.copy(backup_path, config_path)

os.system("color")
RESET = "\033[0m"
GREY = "\033[90m"
ITALIC_GREY = "\033[3;90m"

banner = pyfiglet.figlet_format("AI  Detector", font="slant")
print(f"{GREY}{banner}{RESET}")
print(f"{GREY}Paste text, then press Enter twice to start detection (qq to quit):{RESET}\n")

while True:
    lines = []
    while True:
        line = input()

        if line.strip().lower() == "qq":
            exit()
        if line == "":
            if not lines:
                exit()
            break

        lines.append(line)

    if not lines:
        exit()

    full_text = "\n".join(lines)
    chunks = [full_text[i:i+1500] for i in range(0, len(full_text), 1500)]

    ai_scores = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            out = model(**inputs)
        ai_prob = round(torch.sigmoid(out[1][0][0]).item() * 100, 1)
        ai_scores.append(ai_prob)

    avg = round(sum(ai_scores) / len(ai_scores), 1)
    human = round(100 - avg, 1)

    if avg >= 70:
        verdict = "AI-generated"
    elif avg >= 40:
        verdict = "uncertain / mixed"
    else:
        verdict = "human-written"

    print(f"  AI: {avg}%  |  Human: {human}%  |  verdict: {verdict}")
    print("─" * 60)
    print(f"{ITALIC_GREY}  [Double press Enter to quit, or just test again]{RESET}\n")
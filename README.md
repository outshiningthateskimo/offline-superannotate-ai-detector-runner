# Offline AI Text Detector (SuperAnnotate RoBERTa)

Portable offline runner for the SuperAnnotate RoBERTa AI-text detector (for Windows). 

*This project runs the **SuperAnnotate AI text detector** locally and offline using a RoBERTa-based classifier.*


## Contents

- [About](#about)
- [Requirements](#requirements)
- [Setup (run once)](#setup-run-once)
- [Model setup (run once)](#model-setup-run-once)
- [Running the detector](#running-the-detector)
- [Offline mode](#offline-mode)
- [Run it like an app](#run-it-like-an-app)
- [Credits](#credits)

## About 

TL;DR: you should probably read it tho cause I am amazing and it's been a while since you read human. Just read it ✓.  

But if you really don't want to, you have the instructions right below.

---

Yeah, it's not the newest most accurate detector (but it's not really old GPT-2 style either, which I did before and it was really bad, this is much much better; it gives similar results to QuillBot from my testing). But it is a free option and it is offline. Because you **shouldn't** paste all your papers' content into online tools. So it is good just to give you an idea and it feels cool to have it, so, basically here is how you can easily get it running on your machine as well. I made sure it looks pretty too. Minimalist but cute. 

And yeah it just is cool to have and play around with okay, don't trust these things 100%. I wrote an abstract to a paper once, it took me 5h to write it ALL MYSELF but it gave 67% AI or smth. Apparently, you can't be smart anymore these days smh. Like uhm I just know how to write formally if I really take the time, excuse me 🙄. I can also write like this which is very much the opposite of formal writing, yeah? also, yes, I'm writing a cake recipe story before the instructions because who cares, I am tired of AI slop. I am an AI user myself! It is very useful and valuable but stop using it ***EVERYWHERE***, I am going insane. If y'all can't write a sentence without it fine but at least cut the fillers and keep the essential info only, stop wasting our time with *"here is the truth no one has told you before"* garbage. iykyk.

So, whatever, if the only way to not be considered AI today is to write informal stuff in formal settings then so be it.  

Anyway, below you will find the instructions.

## Requirements

Before running the detector, install:

* Python **3.11.x** (required because Python 3.12+ is not supported, skill issue)

Download here:
https://www.python.org/downloads/


## Setup (run once)

1. Download this repository first.

2. Open a terminal inside the project folder and run:

```
py -3.11 -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

This installs everything needed.


## Model setup (run once)

Create this folder structure inside the project directory:

```
hf_models/
```

Then download these models from HuggingFace:

### SuperAnnotate detector

https://huggingface.co/SuperAnnotate/ai-detector

### RoBERTa backbone

https://huggingface.co/FacebookAI/roberta-large

Place them inside:

```
hf_models/
```

Final structure should look like:

```
hf_models/
 ├ superannotate-ai-detector/
 └ roberta-large/
```

---

## Running the detector

Double-click:

```
run_detector.bat
```

Paste text into the terminal.

Press Enter twice to analyze.

Example output:

```
AI: 82.4% | Human: 17.6% | verdict: AI-generated
```


## Offline mode

This detector runs fully offline after setup.

No internet connection is required once:

* dependencies are installed
* models are downloaded


## Run it like an app

You can make it all easy access if you use the tool often by adding a shortcut to the bat file.

1. Locate your `run_detector.bat` file.
2. Right click, select `Create Shortcut`. Name it something like `Detector AI` or whatever you want.
3. `Windows + R` and type `shell:programs`. This will open a File Explorer location `Programs`. 
4. `Ctrl + X` your shortcut and put it in `Programs`.  

5. You can also customize the app now. Right click the shortcut, go to `Properties` and select `Change icon`. You can look online for any ICO file you'd like or create your own to select your icon. If you don't wanna look for any and you liked The Jetsons, I have added one for you, which you already have because you downloaded this repo. So just select `icon-robot-jetsons.ico` from your project directory lol.

6. Now, you can just search the app in your Windows search bar. You can also pin it from there and voilà. Easy access.

---

## Credits

Uses:

SuperAnnotate AI Detector
https://huggingface.co/SuperAnnotate/ai-detector

RoBERTa-large backbone
https://huggingface.co/FacebookAI/roberta-large

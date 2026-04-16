@echo off

set ROOT=%~dp0

call "%ROOT%env\Scripts\activate"

set HF_HOME=%ROOT%hf_cache
set HUGGINGFACE_HUB_CACHE=%ROOT%hf_cache

set HF_HUB_OFFLINE=1
set TRANSFORMERS_OFFLINE=1
set HF_HUB_DISABLE_TELEMETRY=1
set HF_HUB_DISABLE_SYMLINKS_WARNING=1

python "%ROOT%detect_text.py"

pause

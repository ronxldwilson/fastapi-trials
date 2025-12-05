# FastAPI

1. Simple FastApi server
2. Simple NN trained and deployed via fastAPI server
3. Simple NN saved and deployed via fastAPI server
4. Llama 3.2 (1B Instruct) — Local Deployment on FastAPI

End-to-end instructions for downloading, converting, quantizing, and serving a Llama 3.2 model using `llama.cpp` + FastAPI.

1. Download the Llama 3.2 — 1B Instruct Model

Make sure you have `huggingface-cli` installed:

```bash
pip install huggingface_hub
```

Then download the model snapshot:

```bash
hf download meta-llama/Llama-3.2-1B-Instruct --dir models/llama-3.2-1b
```

This will create:

```
models/llama-3.2-1b/
    config.json
    tokenizer.json
    tokenizer.model
    model.safetensors
    ...
```

---

2. (Optional) Locate HuggingFace Cache Snapshot

If you want to convert directly from your HF cache:

```
G:/hf_cache/hub/models--meta-llama--Llama-3.2-1B-Instruct/snapshots/<snapshot_id>
```

Confirm the presence of:

* `model.safetensors`
* tokenizer files
* config files

---

3. Convert HuggingFace Format → GGUF (Required for llama.cpp / ctransformers)

Inside your `llama.cpp` directory:

```bash
cd F:/llama.cpp
```

Run the conversion script:

```bash
python convert_hf_to_gguf.py \
  G:/hf_cache/hub/models--meta-llama--Llama-3.2-1B-Instruct/snapshots/9213176726f574b556790deb65791e0c5aa438b6 \
  --outfile llama-3.2-1b-instruct-FP16.gguf
```

This produces:

```
llama-3.2-1b-instruct-FP16.gguf
```

---

4. (Optional) Quantize the Model (Smaller, Faster)

Once you compile `llama.cpp`, quantization becomes available:

```bash
./build/bin/quantize \
    llama-3.2-1b-instruct-FP16.gguf \
    llama-3.2-1b-instruct-Q4_K_M.gguf \
    q4_K_M
```

Recommended quantizations:

| Format   | Speed | RAM    | Quality |
| -------- | ----- | ------ | ------- |
| `Q4_K_M` | ⭐⭐⭐⭐  | Low    | Good    |
| `Q5_K_M` | ⭐⭐⭐   | Medium | Better  |
| `Q6_K`   | ⭐⭐    | High   | Best    |

If you don't quantize, FP16 works fine but is larger.

---

5. Using the GGUF Model in FastAPI

Project structure example:

```
llm-based-deployment/
 ├── src/llm_api/main.py
 ├── src/llm_api/model_loader.py
 ├── model/
 │    └── llama-3.2-1b-instruct-FP16.gguf
 ├── pyproject.toml
```

6. Run the FastAPI Server

```bash
uvicorn llm_api.main:app --reload
```

Example request:

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello there","max_tokens":128}'
```

---

7. Troubleshooting

RuntimeError: Failed to create LLM

Cause: wrong path or corrupted GGUF.
Fix: verify:

```bash
ls llm-based-deployment/model
```

Correct:

```
llama-3.2-1b-instruct-FP16.gguf
```

cmake not found

Install:

[https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Open:

```
x64 Native Tools Command Prompt for VS 2022
```

Then rerun:

```bash
cmake -B build
cmake --build build --config Release
```


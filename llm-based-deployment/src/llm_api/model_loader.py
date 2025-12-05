from ctransformers import AutoModelForCausalLM

_model = None

def load_model():
    global _model
    if _model is None:
        _model = AutoModelForCausalLM.from_pretrained(
            "./model/llama-3.2-1b-instruct.gguf",
            model_type = "llama",
            gpu_layers = 0
        ) 
    return _model
        
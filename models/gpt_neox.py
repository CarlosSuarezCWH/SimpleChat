from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GPTNeoXModel:
    def __init__(self):
        """
        Carga diferida del modelo y el tokenizador para GPT-NeoX.
        """
        self.tokenizer = None
        self.model = None

    def _load_model(self):
        """
        Carga el modelo y el tokenizador solo si no se han cargado previamente.
        """
        if self.tokenizer is None or self.model is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
            self.model = AutoModelForCausalLM.from_pretrained(
                "EleutherAI/gpt-neox-20b",
                device_map="auto" if device == "cuda" else None,
                torch_dtype=torch.float16 if device == "cuda" else torch.float32
            )

    def generate(self, prompt: str, max_length: int = 200, temperature: float = 0.7):
        """
        Genera texto basado en el prompt dado.
        """
        self._load_model()
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=temperature
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

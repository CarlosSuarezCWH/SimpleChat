from transformers import AutoModelForCausalLM, AutoTokenizer

class Llama2Model:
    def __init__(self):
        """
        Carga el modelo y el tokenizador para Llama 2.
        """
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
        self.model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-2-7b-hf",
            device_map="auto",  # Usa automáticamente la GPU si está disponible
            torch_dtype="auto"  # Usa FP16 si la GPU lo soporta
        )

    def generate(self, prompt: str, max_length: int = 200):
        """
        Genera texto basado en el prompt dado.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

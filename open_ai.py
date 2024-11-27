from transformers import T5ForConditionalGeneration, T5Tokenizer

class OpenAIAPI:
    def __init__(self):
        model_name = "t5-large"
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)

    def ask_question(self, question, tokenizer, model):
        # Tokenisasi input dengan max_length untuk kontrol panjang input
        inputs = tokenizer(question, return_tensors="pt", max_length=512, truncation=True)
        # Menghasilkan output dengan pengaturan beam search, max_length, no_repeat_ngram_size untuk menghindari repetisi
        outputs = model.generate(inputs['input_ids'], max_length=150, num_beams=5, early_stopping=True, no_repeat_ngram_size=2)
        # Mengubah token hasil generate menjadi teks
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def load_model(self):
        return self.tokenizer, self.model

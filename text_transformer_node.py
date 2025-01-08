class TextTransformer:
    CATEGORY = "ruText"
    
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "transform_text"

    # Таблица преобразований
    TRANS_TABLE = {
        "А": "A", "Б": "ß", "В": "B", "Г": "Î", "Д": "д", "Е": "E", "Ё": "É", "Ж": "x",
        "З": "3", "И": "u", "Й": "ü", "К": "K", "Л": "л", "М": "M", "Н": "H", "О": "O",
        "П": "á", "Р": "P", "С": "C", "Т": "T", "У": "Y", "Ф": "ö", "Х": "X", "Ц": "Ü",
        "Ч": "4", "Ш": "!!!!", "Щ": "!!!", "Ъ": "ț", "Ы": "bl", "Ь": "b", "Э": "€",
        "Ю": "10", "Я": "®"
    }

    def transform_text(self, text):
        result = []
        # Создаём копию текста в верхнем регистре для проверки
        upper_text = text.upper()
        
        for i, char in enumerate(text):
            upper_char = upper_text[i]
            # Проверяем есть ли символ в таблице (проверяем по верхнему регистру)
            if upper_char in self.TRANS_TABLE:
                # Если есть - заменяем точно как в таблице
                result.append(self.TRANS_TABLE[upper_char])
            else:
                # Если нет - оставляем оригинальный символ
                result.append(char)
        result = "".join(result)
        # print(result)
        return (result,)
# ComfyUI-Rutext-lora-transformer

This node automatically transforms Russian text into the required character set

<https://civitai.com/models/1056401?modelVersionId=1205661>

## Installation

1. Go to comfyui/custom_nodes
2. Clone the repository

## Example

**Input:**
`girl hold sign "Панды"`

**Output:**
`girl hold sign "áAHдbl"`

## Dictionary

```
Новый словарь замены русских букв v1.3
"А": "A", "Б": "ß", "В": "B", "Г": "Î", "Д": "д", "Е": "E", "Ё": "É", "Ж": "x", "З": "3", "И": "u", "Й": "ü", "К": "K", "Л": "л", "М": "M", "Н": "H", "О": "O", "П": "á", "Р": "P", "С": "C", "Т": "T", "У": "Y", "Ф": "ö", "Х": "X", "Ц": "Ü", "Ч": "4", "Ш": "!!!!", "Щ": "!!!", "Ъ": "ț", "Ы": "bl", "Ь": "b", "Э": "€", "Ю": "10", "Я": "®"
```

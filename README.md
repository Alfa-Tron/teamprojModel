# teamprojModel
## Участники команды

- Гуляев Николай Алексеевич (РИМ-130906)
- Седиров Арсен Русланович (РИМ-130906)
- Абсалямов Фаниль Ямилевич (РИМ-130906)

**Модель:** sentence-transformers/all-MiniLM-L6-v2


### Описание работы модели

Модель разработана для автоматического перевода текста с одного языка на другой. Она принимает на вход текст на исходном языке и возвращает его перевод на целевой язык.

### Пример использования

Пример использования модели в Python:

```python
from my_translation_model import translate

source_text = "Привет, как дела?"
target_text = translate(source_text, source_language="ru", target_language="en")

print(f"Перевод: {target_text}")

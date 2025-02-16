import re


def delete_html_tags(result_file="cleaned.txt"):
    full_path = r"C:/Users/1pc/PycharmProjects/PythonProject31/homework31-/draft.html"

    with open(full_path, encoding="utf-8") as file:
        text = file.read()

    clean_text = re.sub(r"<[^>]+>", " ", text)

    with open(result_file, "w", encoding="utf-8") as file:
        file.write(clean_text)


delete_html_tags()
print("Файл очищено і збережено у cleaned.txt")

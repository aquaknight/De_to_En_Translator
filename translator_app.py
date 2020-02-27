from translate import Translator

translator = Translator(to_lang="de")

# try:
#     with open('source_file.txt', mode='r') as src_file:
#         text = src_file.read()
#         translation = translator.translate(text)
#         print(translation)
# except FileNotFoundError as err:
#     print("File not found!")

translation = translator.translate("Hello")
print(translation)

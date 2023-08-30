import base64

macro_path = r"C:\Users\Naveen Kumar\Desktop\NovaConverter Ver1_5.exe"
with open(macro_path, 'rb') as macro_file:
    macro_data = macro_file.read()

encoded_macro_data = base64.b64encode(macro_data)

macro_file_path = r"C:\Users\Naveen Kumar\Desktop\NovaConverter Ver1_5.txt"
with open(macro_file_path, 'wb') as text_file:
    text_file.write(encoded_macro_data)

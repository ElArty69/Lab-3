import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

def generate_key_with_custom_format(dec_input):
    """Генерирует ключ в соответствии с указанным форматом и правилами.
    
    :param dec_input: Число из 3 цифр в десятичном формате.
    :return: Сгенерированный ключ в формате xxxxx-xxxx-xxx-xx."""
    if len(dec_input) != 3 or not dec_input.isdigit():
        return "DEC-число должно состоять ровно из 3 цифр."
    shifts = [int(digit) for digit in dec_input]
    def random_block(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    def shift_block(block, shift, direction):
        shifted = []
        for char in block:
            if char.isalpha():  
                base = ord('A')
                new_char = chr((ord(char) - base + (shift if direction == "right" else -shift)) % 26 + base)
            elif char.isdigit(): 
                new_char = str((int(char) + (shift if direction == "right" else -shift)) % 10)
            shifted.append(new_char)
        return ''.join(shifted)
    block_lengths = [5, 4, 3, 2]
    blocks = []
    for i, length in enumerate(block_lengths):
        if i == 0: 
            block = random_block(length)
        else: 
            shift = shifts[(i - 1) % len(shifts)]
            direction = "right" if i % 2 == 1 else "left"
            block = shift_block(block[:length + 1], shift, direction)[:length]
        blocks.append(block)

    return '-'.join(blocks)

def generate_key():
    dec_value = dec_input.get()
    key = generate_key_with_custom_format(dec_value)
    result_label.config(text=f"Сгенерированный ключ: {key}")

def validate_input(value_if_allowed):
    return value_if_allowed.isdigit() and len(value_if_allowed) <= 3
root = tk.Tk()
root.title("Генератор ключей - Пользовательский формат")
root.geometry("600x400")  

background_image = Image.open("Clash+Royale.jpg") 
background_image = background_image.resize((600, 400)) 
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1) 
vcmd = root.register(validate_input)

tk.Label(root, text="Введите DEC-число (ровно 3 цифры):", bg="white").pack(pady=(250, 20)) 
dec_input = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
dec_input.pack(pady=10)  

generate_button = tk.Button(root, text="Сгенерировать ключ", command=generate_key, bg = "green")
generate_button.pack(pady=5)
""
result_label = tk.Label(root, text="", font=("Times new roma", 12), fg="white", bg = "black")
result_label.pack(pady=10)  

root.mainloop()
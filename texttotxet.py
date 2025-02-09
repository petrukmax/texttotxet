import tkinter as tk


def update_reversed_text():
    # Получаем текст из первого текстового поля
    original_text = text_input.get("1.0", "end-1c")

    # Разделяем текст на строки и переворачиваем их порядок
    lines = original_text.splitlines()
    reversed_lines = lines[::-1]

    # Объединяем строки обратно в текст
    reversed_text = "\n".join(reversed_lines)

    # Очищаем второе текстовое поле и вставляем измененный текст
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, reversed_text)


def paste_from_clipboard():
    # Вставляем содержимое буфера обмена в первое текстовое поле
    try:
        clipboard_text = root.clipboard_get()
        text_input.insert(tk.INSERT, clipboard_text)
        update_reversed_text()  # Обновляем второе текстовое поле после вставки
    except tk.TclError:
        pass  # Буфер обмена пуст


def copy_to_clipboard():
    # Копируем содержимое второго текстового поля в буфер обмена
    output_text = text_output.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(output_text)


# Создаем главное окно
root = tk.Tk()
root.title("Перевернутый текст")

# Первое текстовое поле для ввода
text_input = tk.Text(root, height=10, width=40)
text_input.pack(side=tk.TOP, padx=10, pady=5)

# Кнопка "Вставить" под первым текстовым полем
paste_button = tk.Button(root, text="Вставить", command=paste_from_clipboard)
paste_button.pack(side=tk.TOP, pady=5)

# Второе текстовое поле для вывода
text_output = tk.Text(root, height=10, width=40)
text_output.pack(side=tk.TOP, padx=10, pady=5)

# Кнопка "Копировать" под вторым текстовым полем
copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.pack(side=tk.TOP, pady=5)

# Привязываем функцию обновления к событию изменения текста
text_input.bind("<KeyRelease>", lambda event: update_reversed_text())

# Запускаем главный цикл приложения
root.mainloop()

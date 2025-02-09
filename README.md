# Texttotxet

This is a simple Python application named **texttotxet**, built using the Tkinter library. It allows users to input text into one text field, and the second text field automatically displays the text in reverse line order. The application also supports clipboard functionality via "Paste" and "Copy" buttons.

## Features

1. **First Text Field**:
   - Users can type or paste text.
   - A **"Paste"** button below the first text field allows inserting text from the clipboard.

2. **Second Text Field**:
   - Automatically displays the text from the first field but with lines reversed.
   - A **"Copy"** button below the second text field copies its content to the clipboard.

3. **Automatic Updates**:
   - The second text field updates instantly when the text in the first field is changed (either by typing or pasting).

## Requirements

- Python 3.x
- Tkinter library (usually included in the standard Python distribution)

## How to Use

1. Type text into the first text field, and it will automatically appear in the second text field in reverse line order.
2. To insert text from the clipboard, click the **"Paste"** button below the first text field.
3. To copy the reversed text from the second field, click the **"Copy"** button below the second text field.

## Example of Usage

### Input Text:
If you enter the following text in the first text field:
```
Line 1
Line 2
Line 3
```

The second text field will display:
```
Line 3
Line 2
Line 1
```

### Paste Text:
- Copy text to your clipboard (e.g., using Ctrl+C).
- Click the **"Paste"** button below the first text field.
- The text will be inserted, and the second text field will update automatically.

### Copy Result:
- After the reversed text appears in the second text field, click the **"Copy"** button below the second text field.
- The content of the second text field will be copied to your clipboard.

## Author

- **Maxim Petruk** - [GitHub Profile](https://github.com/petrukmax)

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

---

If you have any suggestions for improvement or questions, please feel free to create an issue or submit a pull request!
```

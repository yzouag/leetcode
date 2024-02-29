def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def decode(message_file):
    content = read_text_file(message_file)
    content = content.splitlines()
    
    words = [''] * (len(content)+1)

    for line in content:
        if not line:
            continue
        index, word = line.split()
        words[int(index)] = word

    res = []

    gap = 1
    end_index = 0
    while True:
        end_index += gap
        gap += 1

        if (end_index >= len(content)):
            res.append(words[-1])
            break
        else:
            res.append(words[end_index])

    return " ".join(res)

print(decode('coding_qual_input.txt'))

file_path = r"c:\Users\Dervis Martinez\Documents\DEV\ML-studing\notebooks\Formula 1 World Championship (1950 - 2024).ipynb"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

broken_str = '<img src="../reports/figures/logotypes/f1.png" alt="F1 logo" width="250"/>'
fixed_str = '<img src=\\"../reports/figures/logotypes/f1.png\\" alt=\\"F1 logo\\" width=\\"250\\"/>'

content = content.replace(broken_str, fixed_str)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed")

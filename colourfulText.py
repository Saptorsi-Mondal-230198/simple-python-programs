import os

os.system('cls')

colors = {
    "Black": "\u001b[30m",
    "Red": "\u001b[31m",
    "Green": "\u001b[32m",
    "Yellow": "\u001b[33m",
    "Blue": "\u001b[34m",
    "Magenta": "\u001b[35m",
    "Cyan": "\u001b[36m",
    "White": "\u001b[37m",
    "Bright Black": "\u001b[30;1m",
    "Bright Red": "\u001b[31;1m",
    "Bright Green": "\u001b[32;1m",
    "Bright Yellow": "\u001b[33;1m",
    "Bright Blue": "\u001b[34;1m",
    "Bright Magenta": "\u001b[35;1m",
    "Bright Cyan": "\u001b[36;1m",
    "Bright White": "\u001b[37;1m",
    "Background Black": "\u001b[40m",
    "Background Red": "\u001b[41m",
    'Background Green': "\u001b[42m",
    "Background Yellow": "\u001b[43m",
    "Background Blue": "\u001b[44m",
    "Background Magenta": " \u001b[45m",
    "Background Cyan": "\u001b[46m",
    "Background White": "\u001b[47m",
    "Background Bright Black": "\u001b[40;1m",
    "Background Bright Red": "\u001b[41;1m",
    "Background Bright Green": "\u001b[42;1m",
    "Background Bright Yellow": "\u001b[43;1m",
    "Background Bright Blue": " \u001b[44;1m",
    "Background Bright Magenta": "\u001b[45;1m",
    "Background Bright Cyan": "\u001b[46;1m",
    "Background Bright White": "\u001b[47;1m",
    "Reset": "\u001b[0m"
}


def colorText(text):
    for c in colors:
        text = text.replace("[" + c + "]", colors[c])
    return text


# fas = " [Red]Fake [Blue]A [Green]Smile"
fas = open("colourFulText.txt", "r")
ascii = "".join(fas.readlines())
coloredAns = colorText(ascii)
print(coloredAns)

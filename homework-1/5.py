# Paper format finder

paper_formats = {
    "A0": [841, 1189],
    "A1": [594, 841],
    "A2": [420, 594],
    "A3": [297, 420],
    "A4": [210, 297],
    "A5": [148, 210],
    "A6": [105, 148],
    "A7": [74, 105],
    "A8": [52, 74],
    "A9": [37, 52],
    "A10": [26, 37],
}

width = int(input("Enter the width of the paper in mm: "))
height = int(input("Enter the height of the paper in mm: "))

for format, dimensions in paper_formats.items():
    if dimensions[0] == width and dimensions[1] == height:
        print(f"The paper format is {format}")
        break
else:
    print("No matching paper format found.")
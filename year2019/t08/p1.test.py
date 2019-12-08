import p1

img = p1.Image(3,2,'123456789012')
print(f'Layer count is 2: {len(img.layers) == 2}')
print(f'Layer 1 count of 0 is 0: {img.layers[0].countOf("0") == 0}')
print(f'Layer 2 count of 0 is 1: {img.layers[1].countOf("0") == 1}')
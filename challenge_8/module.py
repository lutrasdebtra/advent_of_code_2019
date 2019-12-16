def _image_processor(bits, width, height):
    layers = [
        bits[i:i + width * height]
        for i in range(0, len(bits), width * height)
    ]
    return layers


def corrupt_check(bits, width, height):
    layers = _image_processor(bits, width, height)
    layer_zeros = (layers[0].count('0'), layers[0])
    for layer in layers:
        zeros = layer.count('0')
        if zeros < layer_zeros[0]:
            layer_zeros = (zeros, layer)
    layer = layer_zeros[1]
    return layer.count('1') * layer.count('2')


def _determine_visible_pixel(stack):
    while len(stack):
        if len(stack) == 1:
            return stack[0]
        pixel = stack.pop(0)
        if pixel != '2':
            return pixel


def render_image(bits, width, height):
    layers = _image_processor(bits, width, height)
    img = [_determine_visible_pixel(x) for x in list(map(list, zip(*layers)))]
    img = [x if x != '0' else ' ' for x in img]
    img = [img[i * width:(i + 1) * width] for i in range((len(img) + width - 1) // width)] # chunks
    for i in img:
        yield "".join(i)

import heapq

class NodeHuffman:
    def __init__(self, frequency, value=None, left=None, right=None):
        self.frequency = frequency
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency
    
def build_huffman_tree(frequencies):
    heap = [NodeHuffman(frequency, value) for value, frequency in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = NodeHuffman(left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(root):
    def generate_codes(current_node, current_code):
        if current_node.value is not None:
            huffman_codes[current_node.value] = current_code
            return

        generate_codes(current_node.left, current_code + "0")
        generate_codes(current_node.right, current_code + "1")

    huffman_codes = {}
    generate_codes(root, "")
    return huffman_codes

def huffman_compress(image):
    pixels = list(image.getdata())
    frequencies = {pixel: pixels.count(pixel) for pixel in set(pixels)}
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_pixels = "".join([huffman_codes[pixel] for pixel in pixels])
    return encoded_pixels, huffman_tree
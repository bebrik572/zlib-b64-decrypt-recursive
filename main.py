import base64
import zlib

encoded_string = ''


def decode_and_decompress(encoded_string):
  reversed_string = encoded_string[::-1]
  decoded_bytes = base64.b64decode(reversed_string)
  decompressed_data = zlib.decompress(decoded_bytes)
  return decompressed_data


result = ''
counter = 0

while True:
  try:
    counter += 1
    result = decode_and_decompress(encoded_string)
    result_string = str(result).split("(b'")[1].split("'")[0]
    encoded_string = result_string.encode('utf-8')
  except Exception as e:
    print(repr(e))
    break

print(result)

import re

def generate_queueit_code(guid):
  """Genera un código de Queue-it a partir de un GUID.

  Args:
    guid: El GUID de Queue-it.

  Returns:
    El código de Queue-it.
  """

  guid_blocks = guid.split("-")
  guid_blocks.reverse()
  guid_code = "".join(guid_blocks)
  guid_code = re.sub(" ", "", guid_code)
  return guid_code[:8]


if __name__ == "__main__":
  guid = "96ac2721-bde6-4064-8fa9-6b5dca7b46b5"
  guid = "82f010a6-658a-4602-9b53-e0da419caad6"
  code = generate_queueit_code(guid)
  print(code)


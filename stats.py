def count_words(s: str):
  return len(s.split())

def count_chars(s: str):
  res = {}
  for char in s:
    c = char.lower()
    if c not in res:
      res[c] = 1
    else:
      res[c] += 1
  return res 
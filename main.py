
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

def generate_report(words: int, counts: object):
  report = []

  for c in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    if c in counts:
      report.append(f'The \'{c}\' character was found {counts[c]} times')

  return f'''--- Begin report of books/frankenstein.txt ---
  {words} words found in the document
  {'\n'.join(report)}
  --- End report ---
  '''


def main():
  with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    print(generate_report(count_words(file_contents),count_chars(file_contents)))

main()
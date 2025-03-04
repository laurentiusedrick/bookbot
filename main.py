from stats import count_chars, count_words
import sys

def generate_report(words: int, counts: object):
  report = []

  for c in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    if c in counts:
      report.append(f'{c}: {counts[c]}')

  return f'''--- Begin report of books/frankenstein.txt ---
  {words} words found in the document
  {'\n'.join(report)}
  --- End report ---
  '''


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    with open(sys.argv[1]) as f:
      file_contents = f.read()
      print(generate_report(count_words(file_contents),count_chars(file_contents)))

main()
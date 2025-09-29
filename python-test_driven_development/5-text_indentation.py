#!/usr/bin/python3
"""Text indentation utility.

Provides text_indentation(text) which prints text with two newlines after
'.', '?', and ':' characters.
"""


def text_indentation(text):
	"""Print text with two newlines after '.', '?', and ':' characters.

	Validate that text is a string. No leading/trailing spaces on lines.
	"""
	if type(text) is not str:
		raise TypeError("text must be a string")
	text = text.strip()
	result = ''
	i = 0
	while i < len(text):
		ch = text[i]
		if ch in '.?:':
			result = result.rstrip() + ch + '\n\n'
			i += 1
			while i < len(text) and text[i] == ' ':
				i += 1
			continue
		result += ch
		i += 1
	# normalize trailing newlines: ensure exactly one final newline
	result = result.rstrip('\n') + '\n'

	# print each line without extra leading/trailing spaces
	parts = result.split('\n')
	# drop the final empty element created by a trailing newline
	if parts and parts[-1] == '':
		parts = parts[:-1]
	for line in parts:
		print(line.rstrip())

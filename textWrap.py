import textwrap
from textwrap_example import sample_text
dedented_text = textwrap.dedent(sample_text).strip()
for width in [4]:
	print()
	print (textwrap.fill(dedented_text, width=width))

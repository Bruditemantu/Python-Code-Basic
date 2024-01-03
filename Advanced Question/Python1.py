# Define the content of "doc.txt" as a string
doc_content = """Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in
The same link as it is present."""

# Split the content into lines
lines = doc_content.splitlines()
even_lines = [line for line in lines if len(line) % 2 == 0]
filtered_content = "\n".join(even_lines)
print(filtered_content)

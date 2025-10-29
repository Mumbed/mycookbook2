from frontmatter import Frontmatter

d = Frontmatter.read_file("야채볶음밥.md")
a = 10
b = 20
print(f"{d['attributes']}")

from frontmatter import Frontmatter

d = Frontmatter.read_file("야채볶음밥.md")


a = 10

print(f"{d['attributes']}")

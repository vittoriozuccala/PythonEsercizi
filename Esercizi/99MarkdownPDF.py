from markdown_pdf import MarkdownPdf
from markdown_pdf import Section

pdf = MarkdownPdf(toc_level=2, optimize=True)

pdf.add_section(Section("# Title\n", toc=False))
text = """# Section with links

- [External link](https://github.com/vb64/markdown-pdf)
- [Internal link to Head1](#head1)
- [Internal link to Head3](#head3)
"""

pdf.add_section(Section(text))
text2 = """# Section with Table

|TableHeader1|TableHeader2|
|--|--|
|Text1|Text2|
|ListCell|<ul><li>FirstBullet</li><li>SecondBullet</li></ul>|
"""

css = "table, th, td {border: 1px solid black;}"

pdf.add_section(Section(text2), user_css=css)
pdf.meta["title"] = "User Guide"
pdf.meta["author"] = "Vitaly Bogomolov"
pdf.save("guide.pdf")
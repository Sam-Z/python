class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def html_output(self):
        fout = open("output.html", "w", encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset = 'UTF-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        for e in self.data:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %e['url'])
            fout.write("<td>%s</td>" %e['title'])
            fout.write("<td>%s</td>" %e['summary'])
            fout.write("</tr>")

        fout.write("<table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

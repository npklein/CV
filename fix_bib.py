# because my last name is written differently every time
# TODO: now the authors all have to be on one line, but when downloading bib it can be on multiple lines
with open('ndeklein.bib') as input_file, open('own-bib.bib','w') as output:
    for line in input_file:
        if 'author' in line:
            authors = line.split('{')[1].split('}')[0].split('and')
            for index, author in enumerate(authors):
                if 'niek' in author.lower() and 'klein' in author.lower():
                    authors[index] = 'de Klein, Niek'
                    if index > 0:
                        authors[index] = ' '+authors[index]
                    if index != len(authors)-1:
                        authors[index] += ' '
            print(line.rstrip())
            line = '  author={'+'and'.join(authors)+'},\n'
            print(line.rstrip())
            print('-'*20)
        output.write(line)

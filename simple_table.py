# -*- coding: utf-8 -*-

class SimpleTable(object):
    """
    SimpleTable

    Print a simple table as follows:
    +--------------+----------+----------+
    | Header 1     | Header 2 | Header 3 |
    +--------------+----------+----------+
    | aaa          | bbb      | ccc      |
    | aaaaaaaaaaaa | bb       | ccccc    |
    | a            | b        |          |
    +--------------+----------+----------+
    """

    def __init__(self, header=None, rows=None):
        self.header = header or ()
        self.rows = rows or []

    def _get_maxes(self):
        array = [self.header] + self.rows
        # TODO: table collapses when only header exists
        return [max(len(str(s)) for s in m if s is not None) for m in map(None, *array)]

    def _print_row(self, row):
        maxes = self._get_maxes()
        line = []
        for i, m in enumerate(maxes):
            if i == 0:
                line.append('|')
            if len(row) > i:
                line.append((' {0: <%d} ' % m).format(row[i]))
            else:
                line.append(' ' * (m + 2))
            line.append('|')
        return ''.join(line)

    def _print_header(self):
        return self._print_row(self.header)

    def _print_border(self):
        return '+' + '+'.join(['-' * (m + 2) for m in self._get_maxes()]) + '+'

    def print_table(self):
        lines = []
        if self.header:
            lines.append(self._print_border())
            lines.append(self._print_header())
        lines.append(self._print_border())
        for row in self.rows:
            lines.append(self._print_row(row))
        lines.append(self._print_border())
        # Print table
        for line in lines:
            print(line)


if __name__ == '__main__':
    table = SimpleTable(('Header 1', 'Header 2', 'Header 3'), [('aaa', 'bbb', 'ccc'), ('aaaaaaaaaaaa', 'bb', 'ccccc'), ('a', 'b')])
    #table = SimpleTable(('Header 1', 'Header 2', 'Header 3'), [])
    #table = SimpleTable(None, [('aaa', 'bbb', 'ccc'), ('aaaaaaaaaaaa', 'bb', 'ccccc'), ('a', 'b')])
    #table = SimpleTable()
    table.print_table()

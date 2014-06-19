# -*- coding: utf-8 -*-
from itertools import izip_longest


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
        return [max(len(str(s)) for s in it) for it in izip_longest(*array, fillvalue='')]

    def _print_row(self, row):
        maxes = self._get_maxes()
        return '| ' + ' | '.join([('{0: <%d}' % m).format(r) for r, m in izip_longest(row, maxes, fillvalue='')]) + ' |'

    def _print_header(self):
        return self._print_row(self.header)

    def _print_border(self):
        maxes = self._get_maxes()
        return '+' + '+'.join(['-' * (m + 2) for m in maxes]) + '+'

    def _print_table(self):
        lines = []
        if self.header:
            lines.append(self._print_border())
            lines.append(self._print_header())
        lines.append(self._print_border())
        for row in self.rows:
            lines.append(self._print_row(row))
        lines.append(self._print_border())
        return lines

    def print_table(self):
        lines = self._print_table()
        for line in lines:
            print(line)


if __name__ == '__main__':
    table = SimpleTable(('Header 1', 'Header 2', 'Header 3'), [('aaa', 'bbb', 'ccc'), ('aaaaaaaaaaaa', 'bb', 'ccccc'), ('a', 'b')])
    #table = SimpleTable(('Header 1', 'Header 2', 'Header 3'), [])
    #table = SimpleTable(None, [('aaa', 'bbb', 'ccc'), ('aaaaaaaaaaaa', 'bb', 'ccccc'), ('a', 'b')])
    #table = SimpleTable()
    table.print_table()

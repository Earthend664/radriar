from prettyterminal import *

class TerminalTable:
    def __init__(self, table, title="Table", heading_row=True, print=True): # Expects to be given an "array table" (a list of lists)
        self.title = title
        if heading_row:
            self.heading_row = table[0]
        else:
            self.heading_row = False
        self.total_columns = len(table[0])
        self.total_rows = len(table)
        self.table = table
        self.column_lengths = self._getColumnLengths()
        if print:
            self.printTable()

    def _getColumnLengths(self):
        column_lengths = []
        for i in range(self.total_columns):
            current_greatest = 0
            for row in self.table:
                column_len = len(row[i])
                if column_len > current_greatest:
                    current_greatest = column_len
            column_lengths.append(current_greatest)
        return column_lengths

    def _prepareTopBorder(self):
        top_border = f"┌"
        current_column = 1
        for size in self.column_lengths:
            top_border += f"{'─'*(size+1)}"
            if current_column == self.total_columns:
                top_border += f"┐"
            else:
                top_border += f"┬"
            current_column += 1
        return top_border

    def _prepareColumnHeadings(self):
        heading_border = f"│"
        current_index = 0
        for heading in self.heading_row:
            heading_border += f"{heading}{' '*(self.column_lengths[current_index]-len(heading)+1)}│"
            current_index += 1
        return heading_border

    def _prepareBottomHeadingBorder(self):
        bottom_border = f"├"
        current_column = 1
        for size in self.column_lengths:
            bottom_border += f"{'─'*(size+1)}"
            if current_column == self.total_columns:
                bottom_border += f"┤"
            else:
                bottom_border += f"┼"
            current_column += 1
        return bottom_border

    def printHeadingRow(self):
        if self.heading_row:
            top_border = self._prepareTopBorder()
            headings = self._prepareColumnHeadings()
            heading_bottom_border = self._prepareBottomHeadingBorder()
            
            heading_row = top_border + '\n' + headings + '\n' + heading_bottom_border
            print(heading_row)
        return


    def printTable(self):
        printHeading(self.title)
        if self.heading_row:
            self.printHeadingRow()
        
        for i in range(1, len(self.table)):
            for column in self.table[i]:
                print(f"│{column}{' '*(self.column_lengths[self.table[i].index(column)]-len(column)+1)}", end="")
            print("│")
        # Bottom Row
        # └ ┘ ├ ┤
        print("└", end="")
        c = 1
        for i in self.column_lengths:
            print(f"{'─' *(i+1)}", end="")
            if len(self.column_lengths) > c:
                print("┴", end="")
            else: print("┘")
            c += 1

# Testing Values
test_table = [["Username", "Password", "Role"],["Jason","Password1!","User"],["Adam","NOPASSWORD!","Admin"],["Jessie","HorsePretty123","User"]]
table = TerminalTable(test_table, title="Debugging")

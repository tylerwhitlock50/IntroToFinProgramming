# You work at a low latency trading firm and are asked to deliver the order book data provided in order_book_data.txt to a superior
# The problem is that the data isn't formatted correctly. Please complete the following steps to apropriately format the data
# Notice, the first column is a ticker, the second column is a date, the third column is a Bid, the fourth column is an Ask, and the fifth column is a currency type
# 1. Open order_book_data.txt
# 2. Remove the order book lines. i.e. ***** Order Book: ###### *****
# 3. Get rid empty lines
# 4. Get rid of spaces
# 5. Notice that there are two currencies in the order book; USD and YEN. Please convert both the Bid and Ask price to USD (if not already)
# The Bid and Ask are the 3rd and 4th column, respectively
# 6. Create a header line Ticker, Date, Bid, Ask
# 7. Save the header line and propely formatted lines to a comma seperated value file called mktDataFormat.csv


class FileConverter:
    def __init__(self, **kwargs):
        self.input_file = kwargs.get('input_file')
        self.output_file = kwargs.get('output_file')
        self.columns = kwargs.get('columns', ['Ticker', 'Date', 'Bid', 'Ask', 'Currency'])
        self.rate = kwargs.get('rate', 0.0091)
        self.data_array = []
        self.lines = None
        self.encoding = kwargs.get('encoding', 'utf-8') 

    def _read_file(self):
        with open(self.input_file, 'r', encoding=self.encoding) as file:
            self.lines = file.readlines()
        return self

    def _convert_lines_to_array(self):
        self.data_array = [line.strip().split(',') for line in self.lines]
        return self

    def _remove_bad_lines(self):
        self.data_array = [line for line in self.data_array if len(line) == 5 and not line[0].startswith('*****')]
        return self

    def _remove_empty_lines(self):
        self.data_array = [line for line in self.data_array if any(line)]
        return self

    def print_data_array(self):
        for line in self.data_array:
            print(line)
        return self

    def _strip_data_array(self):
        self.data_array = [[item.strip() for item in line] for line in self.data_array]
        return self

    def _add_header(self):
        self.data_array.insert(0, self.columns[:-1])
        return self

    def _convert_currency(self):
        for i in range(1, len(self.data_array)):
            if self.data_array[i][4] == 'YEN':
                self.data_array[i][2] = str(float(self.data_array[i][2]) * self.rate)
                self.data_array[i][3] = str(float(self.data_array[i][3]) * self.rate)
        return self

    def _drop_currency_column(self):
        self.data_array = [line[:-1] for line in self.data_array]
        return self

    def _write_file(self):
        with open(self.output_file, 'w') as file:
            for line in self.data_array:
                file.write(','.join(line) + '\n')
        return self

    def process_file(self):
        self.proc_file = (self._read_file()
                          ._convert_lines_to_array()
                          ._remove_empty_lines()
                          ._remove_bad_lines()
                          ._strip_data_array()
                          ._convert_currency()
                          ._drop_currency_column()
                          ._add_header()
                          )
        return self


def main(input_file,output_file):
    data = FileConverter(input_file=input_file, output_file=output_file)
    data.process_file()
    data._write_file()


if __name__ == '__main__':
    input_file = 'order_book_data.txt'
    output_file = 'mktDataFormat.csv'
    main(input_file, output_file)

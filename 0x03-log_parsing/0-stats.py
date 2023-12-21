#!/usr/bin/python3
"""log_Parser"""
import sys


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print_statistics """
        print('File size: {}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """ Checks_the_line_for_matches """
        try:
            line = line[:-1]
            word = line.split(' ')
            # File size_is_last_parameter_on_stdout
            file_size[0] += int(word[-1])
            # Status_code_comes_before_file_size
            status_code = int(word[-2])
            # Move-through_ dictionary_of_status_codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    linenum = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """ print_after_every_10_lines """
            if linenum % 10 == 0:
                print_stats()
            linenum += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

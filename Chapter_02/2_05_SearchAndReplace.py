import re
from calendar import month_abbr

def simple():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah', 'yep'))


def simple_pattern(data):
    old_pattern = r'(\d+)/(\d+)/(\d+)'  # Group 1 = Month, Group 2 = Day, Group 3 = Year
    new_pattern = r'\3-\1-\2' # \3 refers to the capture groups in the regex
    new_text = re.sub(old_pattern, new_pattern, data)
    print(new_text)


def compiled_pattern(data):
    date_pattern = r'(\d+)/(\d+)/(\d+)'  # Group 1 = Month, Group 2 = Day, Group 3 = Year
    new_pattern = r'\3-\1-\2'  # \3 refers to the capture groups in the regex
    # Using a compiled pattern can give performance improvements if the pattern is used repeatedly
    complied_date_pattern = re.compile(date_pattern)

    new_text = complied_date_pattern.sub(new_pattern, data)
    print(new_text)


def callback_function(data):
    def change_date(matched):
        month_name = month_abbr[int(matched.group(1))]
        # The return should be the replacement text
        return '{} {} {}'.format(matched.group(2), month_name, matched.group(3))

    date_pattern = r'(\d+)/(\d+)/(\d+)'  # Group 1 = Month, Group 2 = Day, Group 3 = Year
    complied_date_pattern = re.compile(date_pattern)
    new_text = complied_date_pattern.sub(change_date, data)
    print(new_text)


simple()
text = "Today is 11/27/2012. PyCon starts 3/13/2013"
simple_pattern(text)
compiled_pattern(text)
callback_function(text)

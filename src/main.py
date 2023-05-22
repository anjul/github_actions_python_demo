from datetime import datetime


class DisplayDate:

    def __init__(self) -> None:
        pass

    def display_current_timestamp(self):
        now = datetime.now()
        print(f'Current Date and Time is {now.strftime("%Y-%m-%d %H:%M:%S")}')

DisplayDate().display_current_timestamp()

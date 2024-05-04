from datetime import datetime

class log:
    def __enter__(self):
        self.start_time = datetime.now()
        print("- context manager opened at", self.start_time.strftime("%H:%M:%S"))

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.now()
        print("- context manager closed at", self.end_time.strftime("%H:%M:%S"))
        print("Time elapsed:", self.end_time - self.start_time)

# Example usage
with log():
    print("hello")

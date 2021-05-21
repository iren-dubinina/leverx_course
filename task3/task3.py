import threading
import concurrent.futures


class UpdateA:
    def __init__(self):
        self.a = 0
        self._lock = threading.Lock()

    def update_a(self, arg):
       for _ in range(arg):
           with self._lock:
               self.a += 1


def main():
    my_value = UpdateA()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(5):
            executor.submit(my_value.update_a, 1000000)
    print("----------------------", my_value.a)


if __name__ == "__main__":
    main()

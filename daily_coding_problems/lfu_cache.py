# Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:


# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.
class Cache:
    def __init__(self, capacity: int = 100):
        self._items = {}
        self._counts: dict[int[dict]] = {}
        self.capacity = capacity
        self._min_frequency = 0

    def set(self, key, value):
        if len(self._items) >= self.capacity:
            self._remove_least_used()
        current = self._items.get(key)
        current_frequency = 0
        if current is not None:
            current_frequency = current["frequency"]
        else:
            self._min_frequency = 0
        if self._counts.get(current_frequency) is None:
            self._counts[current_frequency] = {}
        self._counts[current_frequency][key] = {}
        self._items[key] = {"value": value, "frequency": current_frequency}

    def get(self, key):
        value = self._items.get(key, None)
        if value is not None:
            print(value)
            frequency = value["frequency"]
            print(self._counts[frequency])
            self._counts[frequency].__delitem__(key)
            if len(self._counts[frequency]) == 0 and self._min_frequency == frequency:
                print(f"no items left in {frequency}")
                self._min_frequency += 1
            if self._counts.get(frequency + 1) is None:
                self._counts[frequency + 1] = {}
            self._counts[frequency + 1][key] = {}
            self._items[key]["frequency"] += 1
            return value["value"]

    def _remove_least_used(self):
        key_to_remove, _ = self._counts[self._min_frequency].popitem()
        print(f"removing {key_to_remove}")
        self._items.__delitem__(key_to_remove)

class MyList:
    def __init__(self, capacity=4):
        self._items = [None] * capacity
        self._size = 0

    @property
    def count(self):
        return self._size

    @property
    def capacity(self):
        return len(self._items)

    def element_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._items[index]

    def set_element_at(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._items[index] = value

    def add(self, item):
        if self._size == len(self._items):
            self._resize(len(self._items) * 2)
        self._items[self._size] = item
        self._size += 1

    def insert(self, index, item):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size == len(self._items):
            self._resize(len(self._items) * 2)
        for i in range(self._size, index, -1):
            self._items[i] = self._items[i - 1]
        self._items[index] = item
        self._size += 1

    def remove(self, item):
        index = self.index_of(item)
        if index != -1:
            self.remove_at(index)
            return True
        return False

    def remove_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        for i in range(index, self._size - 1):
            self._items[i] = self._items[i + 1]
        self._items[self._size - 1] = None
        self._size -= 1

    def index_of(self, item):
        for i in range(self._size):
            if self._items[i] == item:
                return i
        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def clear(self):
        self._items = [None] * 4
        self._size = 0

    def _resize(self, new_size):
        new_items = [None] * new_size
        for i in range(self._size):
            new_items[i] = self._items[i]
        self._items = new_items

# Пример использования:

my_list = MyList()
my_list.add(10)
my_list.add(20)
my_list.add(30)

print("Все элементы списка:")
for i in range(my_list.count):
    print(my_list.element_at(i))

# Изменение значения элемента по индексу
my_list.set_element_at(2, 25)

# Вывод списка после изменения элемента
print("\nВсе элементы списка после изменений:")
for i in range(my_list.count):
    print(my_list.element_at(i))

# Вывод размера списка
print("Размер списка:", my_list.count) # Выведет: 3

# Вывод элемента по индексу
print("Элемент с индексом 1:", my_list.element_at(1)) # Выведет: 20

# Проверка наличия элемента в списке
print("Есть ли 20 в списке", my_list.contains(20)) # Выведет: True

# Удаление элемента из списка
my_list.remove(20)
print("Размер списка после удаления значения 20:", my_list.count) # Выведет: 2

# Очистка списка
my_list.clear()
print("Размер списка после очистки", my_list.count) # Выведет: 0

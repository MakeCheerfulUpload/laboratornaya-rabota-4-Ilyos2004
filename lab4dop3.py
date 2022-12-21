import lab4
import lab4dop1
import lab4dop2
import time
start_time = time.time()
for i in range(10):
    lab4.main()
print("Базовый вариант требует", time.time() - start_time, "сек.")
start_time = time.time()
for i in range(10):
    lab4dop1.main()
print("Вариант с внешними библиотеками требует", time.time() - start_time, "сек.")
start_time = time.time()
for i in range(10):
    lab4dop2.main()
print("Вариант с регулярками требует", time.time() - start_time, "сек.")
start_time = time.time()

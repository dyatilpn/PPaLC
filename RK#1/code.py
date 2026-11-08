from operator import itemgetter


class Microprocessor:
  """Микропроцессор"""

  def __init__(self, id, model, price, comp_id):
    self.id = id
    self.model = model
    self.price = price
    self.comp_id = comp_id


class Computer:
  """Компьютер"""

  def __init__(self, id, name):
    self.id = id
    self.name = name


class CompMicroproc:
  """Связь многие-ко-многим между компьютерами и процессорами"""

  def __init__(self, comp_id, proc_id):
    self.comp_id = comp_id
    self.proc_id = proc_id


# Компьютеры
comps = [
    Computer(1, 'Сервер баз данных'),
    Computer(2, 'Игровая станция'),
    Computer(3, 'Офисный ПК'),
    Computer(4, 'Аналитический кластер'),
    Computer(5, 'Рабочая станция'),
]

# Микропроцессоры
procs = [
    Microprocessor(1, 'AMD Ryzen 9', 45000, 2),
    Microprocessor(2, 'Apple M2 Max', 65000, 4),
    Microprocessor(3, 'Intel Core i5', 18000, 3),
    Microprocessor(4, 'AMD EPYC 7763', 120000, 1),
    Microprocessor(5, 'ARM Cortex-A78', 8000, 3),
    Microprocessor(6, 'Intel Xeon Gold', 95000, 1),
]

# Связи многие-ко-многим
comps_procs = [
    CompMicroproc(1, 4),
    CompMicroproc(1, 6),
    CompMicroproc(2, 1),
    CompMicroproc(3, 3),
    CompMicroproc(3, 5),
    CompMicroproc(4, 2),
    CompMicroproc(5, 1),
    CompMicroproc(5, 3),
]


def main():
  """Основная функция программы"""

  # Связь один-ко-многим
  one_to_many = [
      (p.model, p.price, c.name)
      for c in comps
      for p in procs
      if p.comp_id == c.id
  ]

  # Связь многие-ко-многим
  many_to_many_temp = [
      (c.name, cp.comp_id, cp.proc_id)
      for c in comps
      for cp in comps_procs
      if c.id == cp.comp_id
  ]

  many_to_many = [
      (p.model, p.price, comp_name)
      for comp_name, comp_id, proc_id in many_to_many_temp
      for p in procs
      if p.id == proc_id
  ]

  print('Задание В1')
  # Микропроцессоры на букву 'А'/'A' и названия их компьютеров
  res_1 = [
      (model, comp_name)
      for model, price, comp_name in one_to_many
      if model.startswith(('А', 'A'))
  ]
  print(res_1)

  print('\nЗадание В2')
  # Компьютеры с минимальной ценой процессора, отсортированные по возрастанию
  res_2_unsorted = []
  for c in comps:
    c_procs = list(filter(lambda i: i[2] == c.name, one_to_many))
    if len(c_procs) > 0:
      c_prices = [price for _, price, _ in c_procs]
      res_2_unsorted.append((c.name, min(c_prices)))

  res_2 = sorted(res_2_unsorted, key=itemgetter(1))
  print(res_2)

  print('\nЗадание В3')
  # Связанные процессоры и компьютеры, отсортированные по процессорам
  res_3 = sorted(many_to_many, key=itemgetter(0))
  print(res_3)


if __name__ == '__main__':
  main()

import logging

logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO)
logging.info('info log')
logging.debug('debug log')
logging.warning('warning log')


def my_math():
  ask = "Enter the operation using the corresponding number: 1 Sum, 2 Subtract, 3 Multiply, 4 Divide:"
  operation = input(ask)
  return operation


def calculate(a, b, operation):
  if operation == '1':
    result = a + b
  elif operation == '2':
    result = a - b
  elif operation == '3':
    result = a * b
  elif operation == '4':
    if b == 0.:
      logging.error('divided by zero')
    else:
      result = a / b
  else:
    logging.error('unknown operation')
  return result


def example():
  _operation = my_math()
  a = float(input('Enter first number: '))
  b = float(input('Enter second number: '))
  result = calculate(a, b, _operation)
  print(f'Result: {result}')


example()

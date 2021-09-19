def bowling_pins(arr):
   '''
   Bowling Pins
   '''
   full_field = 'I I I I\n I I I \n  I I  \n   I   '
   numbers_field = '7 8 9 0\n 4 5 6 \n  2 3  \n   1   '

   for i in range(len(arr)):
      if arr[i] == 10:
         arr[i] = 0
   arr = [str(i) for i in arr]


   for i in arr:
      if i in numbers_field:
         pos = numbers_field.find(i)
         full_field = full_field[:pos] + ' ' + full_field[pos+1:]

   return full_field


arr = [1,2,10]
print(bowling_pins(arr))
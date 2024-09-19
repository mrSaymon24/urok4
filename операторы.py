odin=int(input('first:'))
dwa=int(input('second:'))
tri=int(input('third:'))
if odin==dwa==tri:
    print('3')
elif odin==dwa or odin==tri or dwa==tri:
    print('2')
elif odin!=dwa or odin!=tri or dwa!=tri:
    print('0')
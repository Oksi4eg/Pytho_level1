# мне пришлось пересмотреть урок, чтобы понять, как вы вызывали командную строку =))

from sys import argv
hour=int(argv[1])
rate=int(argv[2])
bonus=int(argv[3])
print(hour*rate+bonus)

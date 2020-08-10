#----------------------------- first.py
import os
def hello(message):
       print message
       print 'Вы находитесь в %s.' % os.getcwd()

if __name__ == '__main__':
       hello('Hello from Python.')
       raw_input('Нажмите Enter...')
else: pass
#----------------------------end of first.py
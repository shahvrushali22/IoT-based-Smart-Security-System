importRPi.GPIO as GPIO
import time, datetime
importtelepot
fromtelepot.loop import MessageLoop
importsubprocess
now = datetime.datetime.now()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,False)

def action(msg):
chat_id = msg['chat']['id']
command = msg['text']

print 'Received: %s' % command

if command == '/hi':
telegram_bot.sendMessage (chat_id, str("Hello! User"))

elif command == '/open':
GPIO.output(18,True)
telegram_bot.sendMessage(chat_id, str("Door is opened"))
time.sleep(1)

elif command == '/close':
GPIO.output(18,False)
telegram_bot.sendMessage(chat_id, str("Door is closed"))
time.sleep(1)

elif command == '/time':
telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))









elif command == '/show':
subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S0 ipic.jpeg",shell=True)
print('PIC CAPTURED')
telegram_bot.sendPhoto (chat_id,photo=open("/home/pi/ipic.jpeg"))

telegram_bot = telepot.Bot('380658930:AAFRFdAbeV67G-znqkZVJvXdILho5kaogZo')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'

while 1:
time.sleep(10)



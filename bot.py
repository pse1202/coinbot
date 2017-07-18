# -*- coding: utf-8 -*-

from connector.ircmessage import IRCMessage
from queue import Queue
import functions
from importlib import reload
import traceback
import builtins
from connector import setting
from IPython.lib import deepreload
builtins.reload = deepreload.reload

class Bot():
    irc = None
    msgQueue = Queue()

    def __init__(self):
        from connector.ircconnector import IRCConnector
        self.irc = IRCConnector(self.msgQueue)
        self.irc.setDaemon(True)
        self.irc.start()

    def run(self):
        while True:
            try:
                packet = self.msgQueue.get()
                if packet['type'] == 'msg':
                    msg = packet['content']
                    for channel in self.channel_list:
                        self.irc.sendmsg(channel, msg)

                elif packet['type'] == 'irc':
                    message = packet['content']
                    print(message)
                    if message.msgType == 'INVITE':
                        self.irc.joinchan(message.channel)

                    elif message.msgType == 'MODE':
                        if message.msg == '+o ' + self.irc.botnick:
                            self.irc.sendmsg(message.channel, '감사합니다 :)')

                    elif message.msgType == 'KICK':
                        pass

                    elif message.msgType == 'PRIVMSG':
                        val = functions.functionlist(message.msg)
                        if message.msg.find('!업데이트') == 0:
                            reload(functions)
                            self.irc.sendmsg(message.channel, '업데이트 완료')
                        elif val:
                            self.irc.sendmsg(message.channel, val)
                    elif message.msgType == 'NOTICE':
                        for chan in setting.chanlist:
                            self.irc.joinchan(chan)
            except Exception as err:
                with open('error.log','a') as f:
                    from datetime import datetime
                    f.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n' + str(traceback.format_exc()) + '\n')

if __name__ == '__main__':
    bot = Bot()
    bot.run()


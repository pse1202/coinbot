# -*- coding: utf-8 -*-

from connector.ircmessage import IRCMessage
from queue import Queue
import functions
from importlib import reload
import pyinotify
import asyncore

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
                        self.irc.sendmsg(message.channel, "업데이트 완료")
                    elif val:
                        self.irc.sendmsg(message.channel, val)

if __name__ == '__main__':
    bot = Bot()
    bot.run()


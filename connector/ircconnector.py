# -*- coding: utf-8 -*-

import socket
import ssl
import threading
from connector.setting import server, port, botname, botnick
from connector.ircmessage import IRCMessage
from queue import Queue


class IRCConnector(threading.Thread):
    ircsock = None
    msgQueue = None
    botnick = None

    def __init__(self, msgQueue):
        threading.Thread.__init__(self)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        self.ircsock = ssl.wrap_socket(s)
        self.ircsock.send(('USER ' + (botname + ' ') * 3 + ':' +
                           botnick + '\n').encode())
        self.ircsock.send(('NICK ' + botnick + '\n').encode())
        self.botnick = botnick

        self.msgQueue = msgQueue

    def ping(self):
        self.ircsock.send(('PONG :pingis\n').encode())

    def sendmsg(self, chan, msg):
        self.ircsock.send(('PRIVMSG ' + chan + ' :' + msg + '\n').encode())

    def joinchan(self, chan):
        self.ircsock.send(('JOIN ' + chan + '\n').encode())

    def partchan(self, chan):
        self.ircsock.send(('PART ' + chan + '\n').encode())

    def chanlist(self):
        self.ircsock.send(('WHOIS ' + botnick + '\n').encode())

    def settopic(self, chan, msg):
        self.ircsock.send(('TOPIC ' + chan + ' :' + msg + '\n').encode())

    def gettopic(self, chan):
        self.ircsock.send(('LIST ' + chan + '\n').encode())
        ircmsg = self.ircsock.recv(8192)
        topic = (ircmsg.decode().split('\n')[1]).split(':')[2].strip('\n\r')
        return topic

    def run(self):
        while True:
            ircmsg = self.ircsock.recv(8192)
            try:
                ircmsg = ircmsg.decode().strip('\n\r')
            except Exception as e:
                print(e)
            else:
                print(ircmsg)
                message = IRCMessage(ircmsg)
                if message.isValid():
                    print(message)
                    if message.msgType == 'PING':
                        self.ping()
                    else:
                        self.msgQueue.put({'type': 'irc', 'content': message})

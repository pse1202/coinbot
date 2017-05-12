import re


class IRCMessage():
    msgType = None
    sender = None
    channel = None
    msg = None
    target = None

    def __init__(self, origMessage):
        parse = re.search(
            '^(?:[:](\S+) )?(\S+)(?: (?!:)(.+?))?(?: [:](.+))?$', origMessage)
        if parse:
            self.msgType = parse.group(2)
            if self.msgType == 'INVITE':
                self.sender = parse.group(1)
                self.target = parse.group(3)
                self.channel = parse.group(4)
            elif self.msgType == 'PRIVMSG':
                self.sender = parse.group(1)
                self.channel = parse.group(3)
                self.msg = parse.group(4)
            elif self.msgType == 'MODE':
                self.sender = parse.group(1)
                self.channel = parse.group(3).split(' ', maxsplit=1)[0]
                self.msg = parse.group(3).split(' ', maxsplit=1)[1]
            elif self.msgType == 'JOIN':
                self.sender = parse.group(1)
                self.channel = parse.group(4)
            elif self.msgType == 'PING':
                self.sender = parse.group(4)
        else:
            pass

    def __repr__(self):
        msg = self.msg
        return '<IRCMessage : %s %s %s %s %s>' \
               % (self.msgType, self.sender, self.channel, msg, self.target)

    def isValid(self):
        if self.msgType is None:
            return False
        else:
            return True

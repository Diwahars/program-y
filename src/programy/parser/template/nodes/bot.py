"""
Copyright (c) 2016 Keith Sterling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging
from programy.parser.template.nodes.base import TemplateNode

class TemplateBotNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def resolve(self, bot, clientid):
        try:
            name = self.name.resolve(bot, clientid)
            value = bot.brain.properties.property(name)
            if value is None:
                value = bot.brain.properties.property("default-property")
                if value is None:
                    value = ""

            logging.debug("[%s] resolved to [%s] = [%s]", self.to_string(), name, value)
            return value
        except Exception as excep:
            logging.exception(excep)
            return ""

    def to_string(self):
        return "[BOT (%s)]" % (self.name.to_string())

    def output(self, tabs="", output=logging.debug):
        self.output_child(self, tabs, output)

    def to_xml(self, bot, clientid):
        xml = "<bot "
        xml += ' name="%s"' % self.name.resolve(bot, clientid)
        xml += " />"
        return xml

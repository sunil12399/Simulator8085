import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


def format(color, style=''):
    """Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format

# Syntax styles that can be shared by all languages


STYLES = {
    'keyword': format('blue','bold'),
    'labels': format('orange','italic'),
    'value': format('red'),
    'comment': format('darkGreen', 'italic'),
    'numbers': format('brown'),
}


class Highlighter (QSyntaxHighlighter):
    """
    Syntax highlighter for the 8085 language.
    """
    # Python keywords
    keywords = [
           'MOV', 'MVI', 'ADI', 'ACI', 'ADD', 'ANA', 'ANI', 'ADC',
           'CALL', 'CC', 'CM', 'CMA', 'CMC', 'CMP', 'CNC', 'CP', 'CPE', 'CPI', 'CPO', 'CZ', 'CNZ',
           'DAA', 'DAD', 'DCR', 'DCX', 'DI', 'EI', 'HLT', 'IN', 'INX', 'INR', 'NOP',
           'JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ', 'LDA', 'LDAX', 'LHLD', 'LXI',
           'ORA', 'ORI', 'OUT', 'PCHL', 'POP', 'PUSH', 'RAR', 'RRC', 'RAL', 'RLC', 'RET', 'RC', 'RIM',
            'RM', 'RNC', 'RPE', 'RP', 'RPO', 'RST', 'RZ', 'RNZ', 'SBB', 'SUB', 'SUI', 'SHLD', 'SIM', 'SPHL', 'STA', 'STAX', 'STC', 'SBI',
           'XCHG', 'XRA', 'XRI', 'XTHL'
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        rules = []

        # Keyword, operator, and brace rules
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
            for w in Highlighter.keywords]

        # All other rules
        rules += [

            # From '#' until a newline
            (r';[^\n]*', 0, STYLES['comment']),

            # Labels ending with ':'
            (r'\w+[ ]?:', 0, STYLES['labels']),

            # hexadecimal values with a whitespace and H at the end for eg 90 H
            (r'[0-9a-hA-H]{4}[ ]?[h|H]?', 0, STYLES['value']),
            (r'[0-9a-hA-H]{2}[ ]?[h|H]?', 0, STYLES['value']),
        ]
        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """
        Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        text = text.upper()
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
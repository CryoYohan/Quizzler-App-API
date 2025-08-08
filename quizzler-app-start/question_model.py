import html
class Question:

    def __init__(self, q_text, q_answer):
        self.text = html.unescape(q_text) # Unescape escapable HTML
        self.answer = q_answer

from src.entities.feedback_form.cash import Cash


class FeedBackGenerator:
    @staticmethod
    def generate_feedback(feedback_type, **kwargs):
        if feedback_type == '現金':
            if 'value' not in kwargs:
                raise KeyError('Feedback require "value" param')
            else:
                return Cash(int(kwargs['value']))
        else:
            raise ValueError('feedback config error')
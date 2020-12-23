from src.entities.feedback_constraint.single_full import SingleFull


class ConstraintGenerator:
    @staticmethod
    def generate_constraint(constraint_type, **kwargs):
        if constraint_type == '單筆':
            if 'value' not in kwargs:
                raise KeyError('Constrain require "value" params')
            else:
                return SingleFull(int(kwargs['value']))
        else:
            raise ValueError('constraint config error')
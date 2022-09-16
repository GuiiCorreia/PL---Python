import copy


class Originator(object):

    class Memento(object):
        def __init__(self, mstate):
            self.mstate = mstate

        def rollback_state(self):
            return self.mstate

    def set_state(self, state):
        print ('Originator: estado de configuração para: {0}'.format(state))
        self.state = state

    def get_state(self):
        print ('Originator: estado de leitura: {0}'.format(self.state))

    def save_state(self):
        print ('Originator: salvando estado')
        return self.Memento(copy.deepcopy(self))

    def rollback_state(self, memento):
        self = memento.rollback_state()
        print ('Originator: reverter para o estado: {0}'.format(self.state))


if __name__ == '__main__':
    orig = Originator()
    orig.set_state('Estado 1')
    orig.get_state()
    orig.set_state('Estado 2')
    orig.get_state()
    saved_state = orig.save_state()
    orig.set_state('Estado 3')
    orig.get_state()
    orig.rollback_state(saved_state)
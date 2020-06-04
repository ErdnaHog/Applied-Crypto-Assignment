from subpages.topic1_pages.quiz import Quiz
from subpages.topic1_pages.need_for_security import Need_for_security
from subpages.topic1_pages.trusted_system import Trusted_system
from subpages.topic1_pages.security_model import Security_model
from subpages.topic1_pages.security_management import Security_management
from subpages.topic1_pages.type_of_attack import Type_of_attack

class Topic1(Quiz, Need_for_security, Trusted_system, Security_model, Security_management, Type_of_attack):
    pass

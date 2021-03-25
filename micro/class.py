



'''
The module has classes of Activities in different programmed
 which were used on project seminar
 '''

class Zulip:
    """
       Class contains the amount of users' messages and their mentions
       :param message_amount: the amount of users' messages
       :param mention_amount: the amount of users' mentions
    """
    def __init__(self,message_amount: int, mention_amount: int) -> None:
            self.message_amount = mention_amount
            self.mention_amount = mention_amount

    def message(self) -> int:
        return self.message_amount

    def mention(self)-> int:
        return self.mention_amount


class Git:


    def __init__(self, comit_count: int, ) -> None:

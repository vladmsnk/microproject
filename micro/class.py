import abc
import matplotlib.pyplot as plt
'''
The module has classes of Activities in different programmed
 which were used on project seminar
 '''
class Shape(abc.ABC):
    """
    class checking the possesing of acount
    """
    @abc.abstractmethod
    def exist(self) -> bool:
        """
        method that check whether the account exists or not
        :return True or False:
        """
        pass

class Git(Shape):
    """
    Class contains the amount of users' commits
    :param commit_amount: the amount of user's commits
    :param email: the user's email
    """

    def __init__(self, commit_amount: int, email: str ) -> None:
        self.commit_amount = commit_amount
        self.email = email

    def commits(self)->int:
        return self.commit_amount

    def exist(self):
        return True if len(self.email) > 0 else False



class Zulip(Shape):
    """
       Class contains the amount of users' messages and their mentions
       :param message_amount: the amount of users' messages
       :param mention_amount: the amount of users' mentions
       :param email: the user's email
    """
    def __init__(self, message_amount: int, mention_amount: int, email:str) -> None:
            self.message_amount = mention_amount
            self.mention_amount = mention_amount
            self.email = email

    def message(self) -> int:
        return self.message_amount

    def mention(self)-> int:
        return self.mention_amount
    def exist(self):
        return True if len(self.email) > 0 else False

class  Plot():
    def __init__(self,xaxis: int, yaxis: int) -> None:
        self.xaxis = xaxis
        self.yaxis = yaxis

    def plotting(self,color:str,label:str)->None:
        plt.scatter(self.xaxis,self.yaxis,color = color, label = label)





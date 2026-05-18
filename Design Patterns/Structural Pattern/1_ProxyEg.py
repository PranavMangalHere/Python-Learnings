
"""
Docstring for Structural Pattern.1_ProxyEg

The Proxy Pattern is a Structural Design Pattern that provides a substitute or placeholder object to control access to another object.
 -----  Proxy acts as a middle layer between client and real object. -------
to impleament the -porxy pattern their are 3 thing we should know 
There are 3 main components:

Subject (Interface) – Common interface for RealSubject and Proxy
RealSubject – The actual object doing real world
Proxy – Controls access to RealSubject
"""

# ## example
from abc import ABC, abstractmethod

# ## interface
# class DataBase(ABC):
    
#     @abstractmethod
#     def fetch_data(self):
#         pass
    
# ## 2. Real Subject
# class RealServer(DataBase):
    
#     def fetch_data(self):
#         print("the data is fetched")

# ## 3. Proxy 
# class DataBaseProxy(DataBase):
    
#     def __init__(self, user_role):
#         self.user_role = user_role
#         self.realServer = RealServer()
    
#     def fetch_data(self):
#         if self.user_role == 'admin':
#             return self.realServer.fetch_data()
#         else:
#             print("Access denied")
#             return 

# d1 = DataBaseProxy("admin")
# d1.fetch_data()

# d2 = DataBaseProxy("client")
# d2.fetch_data()



# ______________ EXample 2 ________________

class PlayVideoDataBase(ABC):
    def playvideo(self, video):
        pass
    
class PlayVideo(PlayVideoDataBase):
    
    def playvideo(self, video):
        print(f"Play real video --- {video}")

class proxyvideo(PlayVideoDataBase):
    
    def __init__(self, userType):
        self.userType = userType
        self.RealPlayVideo = PlayVideo()
        
    def playvideo(self, video):
        if self.userType == 'free':
            print(f"you can only preview - {video}")
        elif self.userType == 'premium':
            print(f"you are good to go - {video}")
            return self.RealPlayVideo.playvideo(video)

u1 = proxyvideo("premium")
u1.playvideo("Travel video")



"""  
If interviewer asks:
Is Proxy pattern like middleware?

Yes, conceptually Proxy acts like middleware because it sits between the client and the real object and can control, modify, or monitor access. 
However, Proxy is a structural design pattern at the object level, while middleware is an architectural layer at the system level.
"""
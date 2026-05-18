"""
Singleton = a class that allows only ONE object to exist for the whole program
No matter how many times you “create” it, you always get the same instance.
One class → One object → Shared everywhere
"""

class Config:
    _instance = None
    def __init__(self):
        if hasattr(self, "_initialized"):
            return
        
        self.base_url = "http://api.com"
        self.timeout = 30
        self._initialized = True
        
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
c1 = Config.instance()
c2 = Config.instance()

print(c1 is c2)   # True
print(c2.base_url)


##    ------   Why Singleton is IMPORTANT in Test Automation ------

""" 
Every test creates its own browser:

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()

Too many browsers   Slower tests   Resource leaks   Flaky failures
"""


"""  
When NOT to use Singleton ⚠️

Parallel test execution (thread safety needed)
When isolation is required per test
When object state must NOT be shared
Overusing Singleton can make tests dependent on each other.
"""

"""
Interview-friendly one-liner 😎

Singleton ensures a single shared instance of a
class across the test framework, which helps manage heavy resources like
WebDriver, configuration, and logging efficiently and consistently.
"""
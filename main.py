
import mypackage

print(mypackage.func1())
print(mypackage.func2())

from mypackage import module1, module2

print(module1.func1())
print(module2.func2())

from mypackage.module1 import func1
from mypackage.module2 import func2

print(func1())
print(func2())

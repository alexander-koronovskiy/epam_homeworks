"""
User.get_created_instances()  # 0
user, _, _ = User(), User(), User()
user.get_created_instances()  # 3
user.reset_instances_counter()  # 3
"""

from task01.method_adds import User

User().get_created_instances()
user, a = User(), User()
user.get_created_instances()

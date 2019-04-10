class TestClass():
    """description of class"""

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def greet_user(username): 
        """显示简单的问候语""" 
        print("Hello!" + username)

    def describe_pet(animal_type, pet_name='dog'):
        """显示宠物的信息"""
        print("\nI have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")        #describe_pet(animal_type='hamster', pet_name='harry')    def get_formatted_name(first_name, last_name):
        """返回整洁的姓名"""         full_name = first_name + ' ' + last_name         return full_name.title()        #musician = get_formatted_name('jimi', 'hendrix')            def make_pizza(*toppings):
        """
        打印顾客点的所有配料
        传递任意数量的实参 类似 c# prarm[]
        make_pizza('pepperoni')
        make_pizza('mushrooms', 'green peppers', 'extra cheese')
        """
        print(toppings)

    def build_profile(first, last, **user_info):
        """创建一个字典，其中包含我们知道的有关用户的一切
        形参**user_info 中的两个星号让Python创建一个名为user_info 的
空字典，并将收到的所有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问user_info 中的名称—值对。
        """
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last 
        for key, value in user_info.items():
            profile[key] = value
        return profile        #user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
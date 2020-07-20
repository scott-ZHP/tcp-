"""
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.

    三大特征
        封装：创建GraphicManager、Circle、Rectanle
        继承：创建Graphic图形(抽象/统一/隔离 具体图形)
        多态:GraphicManager调用Graphic
            Circle、Rectanle重写Graphic
            向GraphicManager添加Circle、Rectanle对象
    六大原则：
        开闭：增加新图形,图形管理器不变.
        单一职责：
            GraphicManager管理所有图形
            Circle 计算圆形面积
            Rectanle 计算矩形面积
        依赖倒置：GraphicManager使用父Graphic
        组合复用：GraphicManager与图形

"""
class GraphicManager:
    def __init__(self):
        self.all_graphic = []

    # graphic 类型是父类图形
    def add_graphic(self,graphic):
        self.all_graphic.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for graphic in self.all_graphic:
            # 使用所有图形的统一行为
            total_area += graphic.get_area()
        return total_area

class Graphic:
    def get_area(self):
        """
            计算该图形面积
        :return: 数值类型,图形的面积
        """
        pass

# 父类在约束所有所有子类在某一行为上达到统一
class Circle(Graphic):
    def __init__(self,r):
        self.r = r

    def get_area(self):
        # 扩展重写
        # super().get_area()
        return 3.14 * self.r ** 2

class Rectanle(Graphic):
    def __init__(self, l,w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w

manager = GraphicManager()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectanle(5, 6))
print(manager.calculate_total_area())

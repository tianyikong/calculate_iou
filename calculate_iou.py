class Box:
    def __init__(self, xmin, xmax, ymin, ymax):
        assert xmax > xmin >= 0, ("Got invalid box with xmin: {0} and xmax {1}".format(xmin, xmax))
        assert ymax > ymin >= 0, ("Got invalid box with ymin: {0} and ymax {1}".format(ymin, ymax))
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
    
    @property
    def xmin(self):
        return self._xmin
    
    @property
    def ymin(self):
        return self._ymin
    
    @property
    def xmax(self):
        return self._xmax
    
    @property
    def ymax(self):
        return self._ymax

    @property
    def width(self):
        return self.xmax - self.xmin
    
    @property
    def height(self):
        return self.ymax - self.ymin
    
    @property
    def area(self):
        return self.width * self.height


def intersection(box1: Box, box2: Box):
    # find the upper left and bottom right corner of intersection box
    xmin = max(box1.xmin, box2.xmin)
    xmax = min(box1.xmax, box2.xmax)
    ymin = max(box1.ymin, box2.ymin)
    ymax = min(box1.ymax, box2.ymax)

    intersection_area = max(xmax - xmin, 0) * max(ymax - ymin, 0)

    return intersection_area


def calculate_iou(box1: Box, box2: Box):
    _intersection = intersection(box1, box2)
    union = box1.area + box2.area - _intersection
    return _intersection / union



if __name__ == "__main__":
    # some test samples
    a = [0, 1, 0, 1]
    b = [0, 1, 0, 2]
    box1 = Box(*a)
    box2 = Box(*b)
    print(box1)
    print(box1.area)
    print(calculate_iou(box1, box2))
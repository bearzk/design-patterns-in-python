class AbstrcactFile(object):

    def add(self, f):
        pass
    def remove(self, f):
        pass
    def get_child(self, i):
        pass
    def kill_virus(self):
        pass


class ImageFile(AbstrcactFile):

    def __init__(self, name):
        self.name = name
    def add(self):
        raise NotImplementedError("add not implemented")
    def remove(self):
        raise NotImplementedError("remove not implemented")
    def get_child(self):
        raise NotImplementedError("get_child not implemented")
    def kill_virus(self):
        print "kill virus for image file " + self.name


class TextFile(AbstrcactFile):

    def __init__(self, name):
        self.name = name
    def add(self):
        raise NotImplementedError("add not implemented")
    def remove(self):
        raise NotImplementedError("remove not implemented")
    def get_child(self):
        raise NotImplementedError("get_child not implemented")
    def kill_virus(self):
        print "kill virus for text file " + self.name


class Folder(AbstrcactFile):

    def __init__(self, name):
        self.name = name
        self.files = []
    def add(self, f):
        self.files.append(f)
    def remove(self, f):
        self.files.remove(f)
    def get_child(self, i):
        return self.files[i]
    def kill_virus(self):
        print "kill virus for folder " + self.name
        for f in self.files:
            f.kill_virus()


image1 = ImageFile('cat.jpg')
image2 = ImageFile('dog.jpg')
text1 = ImageFile('cat.txt')
text2 = ImageFile('dog.txt')

folder = Folder('animals')
folder.add(image1)
folder.add(image2)
folder.add(text1)
folder.add(text2)

folder.kill_virus()

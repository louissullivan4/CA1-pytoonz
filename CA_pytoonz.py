class Track:
    def __init__(self, name, artiste, timesplayed=0):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def __str__(self):
        string = "%s; %s (%d)" % (self._name, self._artiste, self._timesplayed) + "\n"
        return string

    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def get_timesplayed(self):
        return self._timesplayed

    def play(self):
        self._timesplayed += 1
        return self._timesplayed

    name = property(get_name)
    artiste = property(get_artiste)
    timesplayed = property(get_timesplayed)


class Node:
    def __init__(self, item=None, nextnode=None, prevnode=None):
        self.item = item
        self.next = nextnode
        self.prev = prevnode


class Pytoonz:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, self.head)
        self.cursor = None
        self.size = 0

    def __str__(self):
        current_node = self.cursor
        node = self.head.next
        startstr = " "
        startstr += "Playlist: " + "\n"
        if node is None:
            return "None"
        else:
            while node.item is not None:
                if current_node == node:
                    startstr += "-->"
                    startstr += " {}, {}, {} ".format(node.item.get_name(), node.item.get_artiste(),
                                                      node.item.get_timesplayed()) + "\n"
                else:
                    startstr += "{}, {}, {}".format(node.item.get_name(), node.item.get_artiste(),
                                                    node.item.get_timesplayed()) + "\n"
                node = node.next
            return startstr

    def length(self):
        return self.size

    def add_track(self, track):
        new_node = Node(track)
        if self.size == 0:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.size += 1
            self.cursor = new_node
        else:
            old_node = self.tail.prev
            new_node.prev = old_node
            old_node.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
            self.size += 1

    def get_current(self):
        if self.size == 0 or self.cursor is None:
            return None
        return "Current Track: " + str(self.cursor.item)

    def add_after(self, track):
        current_node = self.cursor
        new_node = Node(track)
        if self.size == 0:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.size += 1
            self.cursor = new_node
        else:
            old_node = current_node.next
            new_node.next = old_node
            old_node.prev = new_node.next
            current_node.next = new_node
            new_node.prev = current_node.next

    def next_track(self):
        current_node = self.cursor
        if current_node is None:
            return
        elif current_node.next == self.tail:
            self.cursor = current_node
        else:
            node = current_node.next
            self.cursor = node

    def prev_track(self):
        current_node = self.cursor
        if current_node is None:
            return
        elif current_node.prev == self.head:
            self.cursor = current_node
        else:
            node = current_node.prev
            self.cursor = node

    def reset(self):
        node = self.head.next
        self.cursor = node

    def play(self):
        current_node = self.cursor
        if current_node is None:
            print( "Error! There are no currently selected tracks")
        else:
            current_node.item.play()
            print("Playing: " + str(current_node.item))

    def remove_current(self):
        current_node = self.cursor
        if current_node is None:
            print("Error! There are no tracks in the playlist.")
        elif current_node == self.head.next and current_node == self.tail.prev:
            self.head.next = None
            self.tail.prev = None
            self.cursor = None
        else:
            next_node = current_node.next
            previous_node = current_node.prev
            previous_node.next = next_node
            next_node.prev = previous_node
            if next_node == self.tail:
                self.cursor = self.head.next
            else:
                self.cursor = next_node
            self.size -= 1

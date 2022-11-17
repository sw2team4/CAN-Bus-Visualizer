# TODO: Add name, id, icon, comment, relationship, ...
#  - See SRS or CRC

class Node(object):
    def __init__(self, name, id, icon, comment, annotation, relationship = None):
        self.name = name
        self.id = id
        self.icon = icon
        self.comment = comment
        self.annotation = annotation
        self.relationship = relationship # This will be another Node()...maybe or just the name/ID of a node (reminds me of Graphs)


    '''
    Description
    '''
    #Frontend needed
    def set_annotation(self, annotation):
        self.annotation = annotation

    #set a 1 to 1 relatioship from the current node and new node (bidirectional)
    '''
    Description
    '''
    def set_relationship(self, relationship):
        #if there is already a 1 to 1 relationship, clear it on both ends before setting the new one
        self.relationship = relationship
        relationship.relationship = self
        


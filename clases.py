class history:
    def __init__(self, summary,assignee,storypoints,epiclink,status):
        self.summary = summary
        self.assignee = assignee
        self.storypoints = storypoints
        self.epiclink = epiclink
        self.status = status
    def as_dict(self):
        return {'summary': self.summary, 'assignee': self.assignee, 'storypoints': self.storypoints,'epiclink': self.epiclink,'status': self.status}
    def as_lbl_assignee(self):
        return self.assignee
    def as_values_points(self):
        return self.storypoints
    def as_lbl_epic(self):
        return self.epiclink
    def as_lbl_status(self):
        return self.status
    
   
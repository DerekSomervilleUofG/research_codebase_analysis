class ExperienceAlgorithm():
    
    field_gain_period = "gain_period"
    field_gain_no_of_commit = "gain_no_of_commit"
    field_loss_period = "loss_period"
    field_loss_percentage = "loss_percentage"
    
    def __init__(self, data) -> None:
        self.gain_period = data[self.field_gain_period]
        self.gain_no_of_commit = data[self.field_gain_no_of_commit]
        self.loss_period = data[self.field_loss_period]
        self.loss_percentage = data[self.field_loss_percentage]
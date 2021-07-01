from django.db.models import Max


class TrainMass:
    max_skew = 0

    def __init__(self, train):
        self.train = train
        self.max_skew = train.sectors.aggregate(max_skew=Max("calcskew")).get(
            "max_skew"
        )

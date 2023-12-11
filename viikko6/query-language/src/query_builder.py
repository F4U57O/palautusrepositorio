from matchers import *


class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, team):
        result = PlaysIn(team)
        return QueryBuilder(And(self.query, result))
    
    def hasAtLeast(self, goals, attr):
        result = HasAtLeast(goals, attr)
        return QueryBuilder(And(self.query, result))
    
    def hasFewerThan(self, goals, attr):
        result = HasFewerThan(goals, attr)
        return QueryBuilder(And(self.query, result))
    
    def oneOf(self, *players):
        return QueryBuilder(Or(*players))
    

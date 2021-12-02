INFINITY = math.inf
    
def max_val(self, opponent, depth):
    if (depth == MAX_DEPTH):
        return self.evaluate(opponent), None
        
    v = -self.INFINITY
    best_action = None
    for action in self.get_legal_actions(opponent):
            
        self.play(action, is_evaluating=True)
            
        m = opponent.min_val(self, depth+1)
        if (m[0] > v):
            v = m[0]
            best_action = action
            
            self.undo_last_action()
            
        return v, best_action
    
def min_val(self, opponent, depth):
    if (depth == MAX_DEPTH):
        return self.evaluate(opponent), None
        
    v = self.INFINITY
    best_action = None
    for action in self.get_legal_actions(opponent):        
        self.play(action, is_evaluating=True)
            m = opponent.max_val(self, depth+1)
            if (m[0] < v):
                v = m[0]
                best_action = action
                
            self.undo_last_action()
            
        return v, best_action


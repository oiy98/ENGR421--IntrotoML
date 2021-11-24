# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #initializations 
    
    start= (problem.getStartState(),[]) # this is is the first node meaning our root node
    stack_container= util.Stack() # in DFS first in is popped last so we use stack as a data structure
    stack_container.push(start) # start noded is pushthe deepest level of the stack being created
    
    explored_nodes= list()
    correct_path=[]
    
    while not stack_container.isEmpty():
        
        (last_node,current_path)=stack_container.pop()
        
        if problem.isGoalState(last_node):
            correct_path= current_path
            break;
            
        if last_node not in explored_nodes:
            explored_nodes.append(last_node)
            
            for successor,action, stepCost in problem.getSuccessors(last_node):
                
                if successor not in explored_nodes:
                    path_to_take=current_path+[action]
                    state_to_be=(successor,path_to_take)
                    stack_container.push(state_to_be)
            
    return correct_path
    
  #creating empty arrays to fill as we explore 
    
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start= (problem.getStartState(),[]) # this is is the first node meaning our root node
    Queue_container= util.Queue() # in BFS first in is first out so we use queue
    Queue_container.push(start) # start noded is pushthe deepest level of the stack being created
    
    explored_nodes= list()
    correct_path=[]
    
    while not Queue_container.isEmpty():
        
        (last_node,current_path)=Queue_container.pop()
        
        if problem.isGoalState(last_node):
            correct_path= current_path
            break;
            
        if last_node not in explored_nodes:
            explored_nodes.append(last_node)
            
            for successor,action, stepCost in problem.getSuccessors(last_node):
                
                if successor not in explored_nodes:
                    path_to_take=current_path+[action]
                    state_to_be=(successor,path_to_take)
                    Queue_container.push(state_to_be)
            
    return correct_path

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    start= (problem.getStartState(),[],0) # this is is the first node meaning our root node
    Queue_container= util.PriorityQueue() # in UCS we look for lower costs 
    Queue_container.push(start,0) # start noded is pushthe deepest level of the stack being created
    
    explored_nodes= list()
    correct_path=[]
    
    while not Queue_container.isEmpty():
        
        (last_node,current_path, costs )=Queue_container.pop()
        
        if problem.isGoalState(last_node):
            correct_path= current_path
            break;
            
        if last_node not in explored_nodes:
            explored_nodes.append(last_node)
            
            for successor,action,stepCost in problem.getSuccessors(last_node):
                
                if successor not in explored_nodes:
                    path_to_take=current_path+[action]
                    cost_to_be=(costs+stepCost)
                    state_to_be=(successor,path_to_take,cost_to_be)
                    Queue_container.push(state_to_be,cost_to_be)
            
    return correct_path

    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    start= (problem.getStartState(),[],0) # this is is the first node meaning our root node
    Queue_container= util.PriorityQueue() # in UCS we look for lower costs 
    Queue_container.push(start,0) # start noded is pushthe deepest level of the stack being created
    
    explored_nodes= list()
    correct_path=[]
    
    while not Queue_container.isEmpty():
        
        (last_node,current_path, costs )=Queue_container.pop()
        
        if problem.isGoalState(last_node):
            correct_path= current_path
            break;
            
        if last_node not in explored_nodes:
            explored_nodes.append(last_node)
            
            for successor,action,stepCost in problem.getSuccessors(last_node):
                
                if successor not in explored_nodes:
                    path_to_take=current_path+[action]
                    cost_to_be=(costs+stepCost)
                    state_to_be=(successor,path_to_take,cost_to_be)
                    Queue_container.push(state_to_be,cost_to_be+heuristic(successor, problem))
            
    return correct_path    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

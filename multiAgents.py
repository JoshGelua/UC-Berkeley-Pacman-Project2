# multiAgents.py
# --------------
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


import random

import util
from game import Agent, Directions  # noqa
from util import manhattanDistance  # noqa


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        currentScore = scoreEvaluationFunction(currentGameState)
        newScore = successorGameState.getScore()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newNumFood = successorGameState.getNumFood()

        "*** YOUR CODE HERE ***"
        closeGhostDist = min([manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates])
        foodList = newFood.asList()
        if foodList:
            closeFoodDist = min([manhattanDistance(newPos, food) for food in foodList])
        else:
            closeFoodDist = 0
        scoreDiff = newScore - currentScore
        smallScareTime = min(newScaredTimes)
        if smallScareTime != 0:
            closeGhostDist = -closeGhostDist*3
        if action == 'Stop':
            return (1/closeFoodDist)
        else:
            return (((15/(closeFoodDist+1))+(80/(newNumFood+1))) + ((closeGhostDist*1)/8) + scoreDiff)


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn="scoreEvaluationFunction", depth="2"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
          This implementation adheres to the guideline on Games Lecture, slide 39
          during Summer 2019 at the University of Toronto.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        def DFMiniMax(gameState, agentIndex, depth=0):
            legalActionList = gameState.getLegalActions(agentIndex)
            numIndex = gameState.getNumAgents() - 1
            bestAction = None

            # If n is TERMINAL
            if (gameState.isLose() or gameState.isWin() or (depth == self.depth)):
                return [self.evaluationFunction(gameState)]
            elif agentIndex == numIndex:
                depth += 1
                childAgentIndex = self.index
            else:
                childAgentIndex = agentIndex + 1
            #If Player == MIN
            if agentIndex != 0:
                min = float("inf")
                for legalAction in legalActionList:
                    successorGameState = gameState.generateSuccessor(agentIndex, legalAction)
                    newMin = DFMiniMax(successorGameState, childAgentIndex, depth)[0]
                    if newMin == min:
                        if bool(random.getrandbits(1)):
                            bestAction = legalAction
                    #return minimum of DFMiniMax(c, MAX) over c in ChildList
                    elif newMin < min:
                        min = newMin
                        bestAction = legalAction
                return min, bestAction
            #Player is MAX
            else:
                max = -float("inf")
                for legalAction in legalActionList:
                    successorGameState = gameState.generateSuccessor(agentIndex, legalAction)
                    newMax = DFMiniMax(successorGameState, childAgentIndex, depth)[0]
                    if newMax == max:
                        if bool(random.getrandbits(1)):
                            bestAction = legalAction
                    #return maximum of DFMiniMax(c, MIN) over c in ChildList
                    elif newMax > max:
                        max = newMax
                        bestAction = legalAction
            return max, bestAction

        bestScoreActionPair = DFMiniMax(gameState, self.index)
        bestScore = bestScoreActionPair[0]
        bestMove =  bestScoreActionPair[1]
        return bestMove


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction.
          This implementation adheres to the guideline on Games Lecture, slide 48-49
          during Summer 2019 at the University of Toronto.
        """
        "*** YOUR CODE HERE ***"
        def alphaBeta(gameState, agentIndex, alpha, beta, depth=0):
            legalActionList = gameState.getLegalActions(agentIndex)
            numIndex = gameState.getNumAgents() - 1
            bestAction = None
            # If n is TERMINAL
            if (gameState.isLose() or gameState.isWin() or depth == self.depth):
                return [self.evaluationFunction(gameState)]
            elif agentIndex == numIndex:
                depth += 1
                childAgentIndex = self.index
            else:
                childAgentIndex = agentIndex + 1
            #If Player == MAX
            if agentIndex == self.index:
                #for c in ChildList
                for legalAction in legalActionList:
                    if beta <= alpha:
                        break
                    successorGameState = gameState.generateSuccessor(agentIndex, legalAction)
                    newAlpha = alphaBeta(successorGameState, childAgentIndex, alpha, beta, depth)[0]
                    #alpha = max(alpha, AlphaBeta(c, MAX, alpha, beta))
                    if newAlpha > alpha:
                        bestAction = legalAction
                        alpha = newAlpha
                return alpha, bestAction
            #Player == MIN
            else:
                #for c in ChildList
                for legalAction in legalActionList:
                    if beta <= alpha:
                        break
                    successorGameState = gameState.generateSuccessor(agentIndex, legalAction)
                    newBeta = alphaBeta(successorGameState, childAgentIndex, alpha, beta, depth)[0]
                    #beta = min(beta, AlphaBeta(c, MAX, alpha, beta))
                    if newBeta < beta:
                        bestAction = legalAction
                        beta = newBeta
                return beta, bestAction

        bestScoreActionPair = alphaBeta(gameState, self.index, -9999999, 9999999)
        bestScore = bestScoreActionPair[0]
        bestMove =  bestScoreActionPair[1]
        return bestMove



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          This implementation adheres to the guideline on Games Lecture, slide 58
          during Summer 2019 at the University of Toronto.
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(gameState, agentIndex, depth=0):
            legalActionList = gameState.getLegalActions(agentIndex)
            numIndex = gameState.getNumAgents() - 1
            bestAction = None
            # If terminal(pos)
            if (gameState.isLose() or gameState.isWin() or depth == self.depth):
                return [self.evaluationFunction(gameState)]
            elif agentIndex == numIndex:
                depth += 1
                childAgentIndex = self.index
            else:
                childAgentIndex = agentIndex + 1

            numAction = len(legalActionList)
            #if player(pos) == MAX: value = -infinity
            if agentIndex == self.index:
                value = -float("inf")
            #if player(pos) == CHANCE: value = 0
            else:
                value = 0

            for legalAction in legalActionList:
                successorGameState = gameState.generateSuccessor(agentIndex, legalAction)
                expectedMax = expectimax(successorGameState, childAgentIndex, depth)[0]
                if agentIndex == self.index:
                    if expectedMax > value:
                        #value, best_move = nxt_val, move
                        value = expectedMax
                        bestAction = legalAction
                else:
                    #value = value + prob(move) * nxt_val
                    value = value + ((1.0/numAction) * expectedMax)
            return value, bestAction

        bestScoreActionPair = expectimax(gameState, self.index)
        bestScore = bestScoreActionPair[0]
        bestMove =  bestScoreActionPair[1]
        return bestMove


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: States are evaluated into sections that linearly correspond
      to the total of the evaluation: win, lose, score, foodScore, and ghost.
      Best case scenario is win, so win contributes the most to an evaluationFunction.
      Score is second important, so it scales up by 10K.
      In a state, we want to get rid of food, capsules, and ghosts (when they
      are to be eaten) so as Pacman gets closer, their respective evaluation
      scales down.
      Avoidance of ghosts is important, but not that important. Ghosts do not
      run faster than Pacman, and are only a real threat if they are 1 step away.
      A light heuristic to get far away from the ghosts as necessary (without
      being too scared from getting food) is all that is needed.



    """
    "*** YOUR CODE HERE ***"
    pacmanPosition = currentGameState.getPacmanPosition()
    ghostPositions = currentGameState.getGhostPositions()
    ghostStates = currentGameState.getGhostStates()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    numCapsules = len(currentGameState.getCapsules())
    foodList = currentGameState.getFood().asList()
    numFood = currentGameState.getNumFood()
    badGhost = []
    yummyGhost = []
    total = 0
    win = 0
    lose = 0
    score = 0
    foodScore = 0
    ghost = 0
    if currentGameState.isWin():
        win = 10000000000000000000000000000
    elif currentGameState.isLose():
        lose = -10000000000000000000000000000
    score = 10000 * currentGameState.getScore()
    capsules = 10000000000/(numCapsules+1)
    for food in foodList:
        foodScore += 50/(manhattanDistance(pacmanPosition, food)) * numFood
    for index in range(len(scaredTimes)):
        if scaredTimes[index] == 0:
            badGhost.append(ghostPositions[index])
        else:
            yummyGhost.append(ghostPositions[index])
    for index in range(len(yummyGhost)):
        ghost += 1/(((manhattanDistance(pacmanPosition, yummyGhost[index])) * scaredTimes[index])+1)
    for death in badGhost:
        ghost +=  manhattanDistance(pacmanPosition, death)
    total = win + lose + score + capsules + foodScore + ghost
    return total


# Abbreviation
better = betterEvaluationFunction

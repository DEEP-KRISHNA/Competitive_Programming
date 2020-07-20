# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if ((qC - oC) == 0):
		return True
	if ((qR - oR) == 0):
		return True
	if (abs(qC - oC) == abs(qR - oR)):
		return True
	return False

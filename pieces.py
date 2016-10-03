class Piece:
	def __init__(self, player):
		self.player = player
		self.has_moved = False

	def move():
		pass

	def moved():
		self.has_moved = True

	def is_diagnonal_move(current_pos, new_pos, board, max_distance=None):
		piece = board[new_pos.x][new_pos.y]
		if piece is not None and piece.player == self.player:
			return False

		x_diff = current_pos.x - new_pos.x
		x_dir = x_diff/abs(x_diff)
		y_diff = current_pos.y - new_pos.y
		y_dir = y_diff/abs(y_diff)
		if abs(x_diff) != abs(y_diff):
			return False
		if max_distance is not None and x_diff > max_distance:
			return False

		# Check if there are pieces in between the move
		# If move length is 1 then move is valid since piece there can be taken
		if abs(x_diff) < 2:
			return True

		for i in xrange(1, x_diff-1):
			xm = i*x_dir
			ym = i*y_dir
			if board[current_pos.x + xm][current_pos.y + ym] != None:
				return False

		return True 

	def is_straight_move(current_pos, new_pos, board, max_distance=None):
		piece = board[new_pos.x][new_pos.y]
		if piece is not None and piece.player == self.player:
			return False

		x_diff = current_pos.x - new_pos.x
		x_dir = x_diff/abs(x_diff)
		y_diff = current_pos.y - new_pos.y
		y_dir = y_diff/abs(y_diff)
		if x_diff != 0 and y_diff != 0:
			return False
		if max_distance is not None and x_diff > max_distance or y_diff > max_distance:
			return False

		# Check if there are pieces in between the move
		# If move length is 1 then move is valid since piece there can be taken
		# Check if own piece there
		if abs(x_diff) < 2 and abs(y_diff) < 2:

			return True

		if y_diff == 0:
			for i in xrange(1, x_diff-1):
				xm = i*x_dir
				if board[current_pos.x + xm][current_pos.y] != None:
					return False
		if x_diff == 0:
			for i in xrange(1, y_diff-1):
				ym = i*y_dir
				if board[current_pos.x][current_pos.y + ym] != None:
					return False
		return True


class King(Piece):
	def move(current_pos, new_pos, board):
		# Castling
		#if self.has_moved is False and self.:
		can_move = self.is_diagnonal_move(current_pos, new_pos, board, max_distance=1) or self.is_straight_move(current_pos, new_pos, board, max_distance=1)
		if can_move:
			self.moved()
		return can_move

class Queen(Piece):
	def move(current_pos, new_pos):
		can_move = self.is_diagnonal_move(current_pos, new_pos, board) or self.is_straight_move(current_pos, new_pos, board)
		if can_move:
			self.moved()
		return can_move

class Bishop(Piece):
	def move(current_pos, new_pos):
		can_move = self.is_diagnonal_move(current_pos, new_pos, board)
		self.moved()

class Knight(Piece):
	def can_move(current_pos, new_pos):
		piece = board[new_pos.x][new_pos.y]
		if piece is not None and piece.player == self.player:
			return False

		x_diff = current_pos.x - new_pos.x
		y_diff = current_pos.y - new_pos.y

		if abs(x_diff) == 3 and abs(y_diff) != 1:
			return False
		elif abs(y_diff) == 3 and abs(x_diff) != 1:
			return False

		return True

	def move(current_pos, new_pos):
		if self.can_move(current_pos, new_pos, board):
			self.moved()
			return True
		return False

class Rook(Piece):
	def move(current_pos, new_pos):
		can_move = self.is_straight_move(current_pos, new_pos, board)
		self.moved()

class Pawn(Piece):
	def can_move(current_pos, new_pos, board):
		piece = board[new_pos.x][new_pos.y]
		if piece is not None and piece.player == self.player:
			return False

		max_distance = 1
		if self.has_moved is False:
			max_distance = 2

		x_diff = current_pos.x - new_pos.x
		y_diff = current_pos.y - new_pos.y
		if y_diff < 0:
			return False
		elif y_diff > max_distance:
			return False
		elif abs(x_diff) > 1:
			return False
		elif abs(x_diff) == 1 and y_diff == 1:
			return True if board[current_pos.x + x_diff][current_pos.y + 1] is not None else return False 
		elif x_diff != 0:
			return False

		return True

	def move(current_pos, new_pos, board):
		if self.can_move(current_pos, new_pos, board):
			self.moved()
			return True
		return False
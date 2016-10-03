import pieces

class Board():
	def __init__(self):
		# Create the Board
		self.board = [8][8]
		self.moves = []
		for i in xrange(8):
			self.board[6][i] = Pawn('White')
			self.board[1][i] = Pawn('Black')
		self.board[0][0] = Rook('Black')
		self.board[0][7] = Rook('Black')
		self.board[7][0] = Rook('White')
		self.board[7][7] = Rook('White')

		self.board[0][1] = Knight('Black')
		self.board[0][6] = Knight('Black')
		self.board[7][1] = Knight('White')
		self.board[7][6] = Knight('White')

		self.board[0][2] = Bishop('Black')
		self.board[0][5] = Bishop('Black')
		self.board[7][2] = Bishop('White')
		self.board[7][5] = Bishop('White')

		self.board[0][3] = Queen('Black')
		self.board[0][4] = King('Black')
		self.board[7][3] = Queen('White')
		self.board[7][4] = King('White')

	def players_turn():
		return "White" if len(self.moves) % 2 == 0 else return "Black"

	def get_piece(current_pos):
		return self.board[current_pos.x][current_pos.y]

	def update_board(current_pos, new_pos):
		self.board[new_pos.x][new_pos.y] = self.board[current_pos.x][current_pos.y]
		self.board[current_pos.x][current_pos.y] = None

	def move(current_pos, new_pos):
		player_move = self.players_turn()

		piece = self.get_piece(current_pos)
		if piece.player != player_move:
			return False

		if piece.move(current_pos, new_pos) != True:
			return False

		self.update_board(current_pos, new_pos)
		return True

	def is_check():
		# Cycle Through all pieces and see if they have opposing king in check
		pass


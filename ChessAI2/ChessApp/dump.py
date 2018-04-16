if i9 < 8 and i9 >= 0 and j9 < 8 and j9 >= 0:
			if p_type == "pawn" and col == "white":
				if i9 == endI and j9 == endJ:
					return True

		if i10 < 8 and i10 >= 0 and j10 < 8 and j10 >= 0:
			if p_type == "pawn" and col == "white" and is_first:
				if i10 == endI and j10 == endJ:
					return True



		i9 = startI + 1
		j9 = startJ

		i10 = startI + 2
		j10 = startJ

		i11 = startI + 1
		j11 = startJ + 1

		i12 = startI + 1
		j12 = startJ - 1

		i13 = startI - 1
		j13 = startJ

		i14 = startI - 2
		j14 = startJ

		i15 = startI - 1
		j15 = startJ - 1

		i16 = startI - 1
		j16 = startJ + 1
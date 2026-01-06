from shutil import move
import chess
import random

# ---------------------------
# Livro de Abertura (Gambito da Rainha)
# ---------------------------
OPENING_BOOK = {
    "start": ["d4"],
    "d4": ["d5"],
    "d4 d5": ["c4"],
    "d4 d5 c4": ["e6", "dxc4", "c6"],
    "d4 d5 c4 e6": ["Nc3", "Nf3"],
    "d4 d5 c4 dxc4": ["e3", "Nf3"],
}

# ---------------------------
# Princípios Didáticos
# ---------------------------
PRINCIPLES = {
    "center": ["d4", "c4", "e4"],
    "develop": ["Nc3", "Nf3", "Be2", "Bd3"],
    "castle": ["O-O", "O-O-O"]
}

# ---------------------------
# Explicações amigáveis
# ---------------------------
EXPLANATIONS = {
    "center": "Você está controlando o centro do tabuleiro, ótimo para dominar o jogo.",
    "develop": "Você está desenvolvendo suas peças leves (cavalos e bispos), essencial no início.",
    "castle": "Roque feito! Rei seguro e torres conectadas.",
    "queen_early": "Cuidado: mover a dama cedo pode deixá-la vulnerável.",
    "pawn_loss": "Cuidado: perdeu um peão sem compensação.",
    "other": "Lance válido, mas pense nos princípios do Gambito da Rainha."
}

# ---------------------------
# Máquina fazendo lances repetidos
# ---------------------------
engine_history = []

def choose_engine_move(board, engine_history):
    legal_moves = list(board.legal_moves)

    scored_moves = []

    for move in legal_moves:
        score = 0

        # Penaliza repetir o último lance
        if engine_history:
            last = engine_history[-1]
            if move.from_square == last.to_square and move.to_square == last.from_square:
                score -= 100  # punição forte

        # Penaliza mover torre cedo
        piece = board.piece_at(move.from_square)
        if piece and piece.piece_type == chess.ROOK and board.fullmove_number < 10:
            score -= 10

        # Incentiva desenvolvimento
        if piece and piece.piece_type in (chess.KNIGHT, chess.BISHOP):
            score += 5

        scored_moves.append((score, move))

    scored_moves.sort(key=lambda x: x[0], reverse=True)

    chosen = scored_moves[0][1]
    engine_history.append(chosen)

    return chosen


# ---------------------------
# Avaliação do lance
# ---------------------------
def evaluate_move(move_uci, board):
    san = board.san(chess.Move.from_uci(move_uci))
    explanation = EXPLANATIONS["other"]
    score = 0

    if san in PRINCIPLES["center"]:
        score += 1.0
        explanation = EXPLANATIONS["center"]
    elif san in PRINCIPLES["develop"]:
        score += 0.8
        explanation = EXPLANATIONS["develop"]
    elif san == "O-O":
        score += 1.2
        explanation = EXPLANATIONS["castle"]
    elif san.startswith("Q"):
        score -= 1.0
        explanation = EXPLANATIONS["queen_early"]
    elif san in ["a3", "h3"]:
        score -= 0.7
        explanation = EXPLANATIONS["pawn_loss"]

    return score, explanation

# ---------------------------
# Movimento da Máquina
# ---------------------------
def engine_move(board, history, mode="trainer"):
    key = " ".join(history)

    # Modo Treinador: segue livro e depois facilita vitória
    if mode == "trainer":
        if key in OPENING_BOOK:
            san_move = random.choice(OPENING_BOOK[key])
            return board.parse_san(san_move)
        # Após o livro, movimentos deliberadamente subótimos
        moves = list(board.legal_moves)
        random.shuffle(moves)
        return moves[0]  # primeiro legal, não necessariamente ótimo

    # Modo Livre: heurística normal
    return choose_engine_move(board, engine_history)

# ---------------------------
# Sistema de dicas
# ---------------------------
def give_hint(board):
    hints = []
    for move in board.legal_moves:
        score, explanation = evaluate_move(move.uci(), board)
        if score > 0.8:
            hints.append(f"{board.san(move)} ({explanation})")
    if not hints:
        hints.append("Nenhum lance excelente detectado. Tente melhorar o controle do centro e desenvolver peças.")
    return hints[:3]

# ---------------------------
# Feedback avançado no modo livre
# ---------------------------

def analyze_free_move(board: chess.Board):

    # Analisa o estado atual do tabuleiro APÓS o lance do usuário e retorna alertas estratégicos simples.

    alerts = []

    last_move = board.peek()  # último lance já aplicado
    #san = board.san(last_move)

    # 1. Rei em xeque
    if board.is_check():
        alerts.append("⚠️ Atenção: o rei está em xeque.")

    # 2. Peça pendurada (captura imediata possível)
    for square, piece in board.piece_map().items():
        if piece.color == board.turn:  # peças do lado que vai jogar
            attackers = board.attackers(not board.turn, square)
            defenders = board.attackers(board.turn, square)

            if attackers and not defenders:
                piece_name = chess.piece_name(piece.piece_type)
                alerts.append(
                    f"Sua {piece_name} em {chess.square_name(square)} está pendurada."
                )

    # 3. Desenvolvimento muito cedo da dama
    last_move = board.peek()
    piece = board.piece_at(last_move.to_square)
    if piece and piece.piece_type == chess.QUEEN and board.fullmove_number <= 5:
        alerts.append(
            "A dama foi desenvolvida muito cedo, pode virar alvo de tempos."
        )

    # 4. Falta de controle central
    central_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    control = 0
    for sq in central_squares:
        control += len(board.attackers(not board.turn, sq))

    if control == 0:
        alerts.append(
            "Você não exerce controle sobre o centro (d4, e4, d5, e5)."
        )

    # 5. Feedback positivo mínimo (se nada deu errado)
    if not alerts:
        alerts.append("Lance sólido, sem fraquezas imediatas detectadas.")

    return alerts
# ---------------------------
# Impressão do tabuleiro com zeros
# ---------------------------
def print_board_with_zeros(board):
    board_str = str(board)
    board_str = board_str.replace('.', '0')
    print(board_str)

# ---------------------------
# Loop principal do jogo
# ---------------------------
def play(mode="trainer"):
    board = chess.Board()
    history = []

    print("\nBem-vindo ao Treinador de Xadrez")
    if mode == "trainer":
        print("Modo Treinador: foco no Gambito da Rainha")
    else:
        print("Modo Livre Inteligente: jogue qualquer abertura, receba alertas estratégicos.")

    print("\nComo jogar:")
    print("- Digite lances em SAN, ex: d4, c4, Nf3, O-O")
    print("- Digite 'hint' para dicas explicativas")
    print("- Digite 'quit' para sair\n")

    while not board.is_game_over():
        # Mostra o tabuleiro
        print("\nTabuleiro atual:")
        print_board_with_zeros(board)

        # Entrada do jogador
        user_input = input("\nSeu lance: ").strip()

        if user_input.lower() == "hint":
            hints = give_hint(board)
            print("Sugestões de bons lances:")
            for h in hints:
                print("-", h)
            continue

        if user_input.lower() == "quit":
            print("Saindo do jogo...")
            break

        try:
            move = board.parse_san(user_input)
        except:
            print("Lance inválido. Tente novamente.")
            continue

        # Avaliação e feedback
        if board.turn != chess.WHITE :
            score, explanation = evaluate_move(move.uci(), board)
        else:
            score, explanation = None, None
        board.push(move)
        history.append(user_input)
    
        print(f"\nVocê jogou: {user_input}")
        print("Explicação:", explanation)
        print("Tabuleiro após seu lance:")
        print_board_with_zeros(board)

        if mode == "free":
            alerts = analyze_free_move(board)
            for a in alerts:
                print(a)

        if board.is_game_over():
            break

        # Máquina joga
        engine = engine_move(board, history, mode)
        san_engine = board.san(engine)
        board.push(engine)
        history.append(san_engine)
        print(f"\nMáquina joga: {san_engine}")
        print("Tabuleiro após o lance da máquina:")
        print_board_with_zeros(board)

        # Reforço positivo no modo treinador
        if mode == "trainer" and not board.is_game_over() and len(history) > 6:
            print("Você está se saindo muito bem! Continue assim!")

    print("\nFim de jogo:", board.result())
    print("Obrigado por jogar! Aprender xadrez é praticar padrões e princípios.")

# ---------------------------
# Menu inicial
# ---------------------------
def main():
    print("Selecione o modo de jogo")
    print("1 - Modo Treinador (Gambito da Rainha)")
    print("2 - Modo Livre Inteligente")
    choice = input("> ").strip()

    if choice == "1":
        play(mode="trainer")
    elif choice == "2":
        play(mode="free")
    else:
        print("Opção inválida. Saindo.")

if __name__ == "__main__":
    main()

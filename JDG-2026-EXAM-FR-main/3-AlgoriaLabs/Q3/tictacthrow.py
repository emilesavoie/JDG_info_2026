"""
Tic Tac Throw! - Un jeu de Tic Tac Toe 4x4 où l'objectif est de perdre intelligemment.

Ce module contient les classes de base pour jouer au Tic Tac Toe ainsi que
le système de test pour évaluer les agents.
"""

import sys
import importlib.util
import time
from typing import List
from enum import Enum

class Player(Enum):
    """Énumération des joueurs."""
    X = "X"
    O = "O"
    EMPTY = " "


class GameState(Enum):
    """États possibles du jeu."""
    IN_PROGRESS = "in_progress"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"


class TicTacToeBoard:
    """
    Classe représentant le plateau de Tic Tac Toe.
    
    Le plateau est représenté comme une grille 4x4 avec les positions numérotées:
     0 |  1 |  2 |  3
    ----------------
     4 |  5 |  6 |  7
    ----------------
     8 |  9 | 10 | 11
    ----------------
    12 | 13 | 14 | 15
    """
    
    def __init__(self):
        """Initialise un plateau vide."""
        self.board = [Player.EMPTY] * 16
        self.current_player = Player.X
    
    def make_move(self, position: int, player: Player) -> bool:
        """
        Effectue un coup sur le plateau.
        
        Args:
            position: Position (0-15) où placer le symbole
            player: Joueur qui effectue le coup
            
        Returns:
            True si le coup est valide, False sinon
        """
        if not self.is_valid_move(position):
            return False
        
        self.board[position] = player
        return True
    
    def is_valid_move(self, position: int) -> bool:
        """
        Vérifie si un coup est valide.
        
        Args:
            position: Position à vérifier
            
        Returns:
            True si le coup est valide, False sinon
        """
        return (0 <= position <= 15 and 
                self.board[position] == Player.EMPTY)
    
    def get_valid_moves(self) -> List[int]:
        """
        Retourne la liste des coups valides.
        
        Returns:
            Liste des positions libres
        """
        return [i for i in range(16) if self.board[i] == Player.EMPTY]
    
    def check_winner(self) -> GameState:
        """
        Vérifie l'état actuel du jeu.
        
        Returns:
            État du jeu (victoire, défaite, match nul, en cours)
        """
        # Lignes de victoire possibles (4 en ligne)
        winning_lines = [
            # Lignes horizontales
            [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
            # Lignes verticales
            [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
            # Diagonales
            [0, 5, 10, 15], [3, 6, 9, 12]
        ]
        
        # Vérifier chaque ligne de victoire
        for line in winning_lines:
            if (self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == self.board[line[3]]
                and self.board[line[0]] != Player.EMPTY):
                if self.board[line[0]] == Player.X:
                    return GameState.X_WINS
                else:
                    return GameState.O_WINS
        
        # Vérifier match nul
        if Player.EMPTY not in self.board:
            return GameState.DRAW
        
        return GameState.IN_PROGRESS
    
    def is_game_over(self) -> bool:
        """
        Vérifie si le jeu est terminé.
        
        Returns:
            True si le jeu est terminé, False sinon
        """
        return self.check_winner() != GameState.IN_PROGRESS
    
    def copy(self) -> 'TicTacToeBoard':
        """
        Crée une copie du plateau.
        
        Returns:
            Nouvelle instance du plateau avec le même état
        """
        new_board = TicTacToeBoard()
        new_board.board = self.board.copy()
        new_board.current_player = self.current_player
        return new_board
    
    def __str__(self) -> str:
        """
        Représentation textuelle du plateau.
        
        Returns:
            Chaîne formatée représentant le plateau
        """
        board_str = ""
        for i in range(0, 16, 4):
            row = " | ".join([f"{self.board[j].value:2}" for j in range(i, i + 4)])
            board_str += row + "\n"
            if i < 12:
                board_str += "---+----+----+---\n"
        return board_str


class Agent:
    """Classe de base pour les agents joueurs."""
    
    def __init__(self, player: Player):
        """
        Initialise l'agent.
        
        Args:
            player: Symbole du joueur (X ou O)
        """
        self.player = player
    
    def make_move(self, board: TicTacToeBoard) -> int:
        """
        Choisit un coup à jouer.
        
        Args:
            board: État actuel du plateau
            
        Returns:
            Position (0-15) du coup choisi
        """
        raise NotImplementedError("Méthode à implémenter dans les sous-classes")


class TicTacToeGame:
    """Classe principale pour gérer une partie de Tic Tac Toe."""
    
    def __init__(self, agent_x: Agent, agent_o: Agent):
        """
        Initialise une nouvelle partie.
        
        Args:
            agent_x: Agent jouant les X
            agent_o: Agent jouant les O
        """
        self.board = TicTacToeBoard()
        self.agents = {Player.X: agent_x, Player.O: agent_o}
        self.move_history = []
    
    def play_game(self, show_game: bool = False) -> GameState:
        """
        Joue une partie complète.
        
        Args:
            verbose: Si True, affiche le plateau à chaque coup
            
        Returns:
            Résultat de la partie
        """
        if show_game:
            print("Nouvelle partie de Tic Tac Throw!")
            print(self.board)
        
        while not self.board.is_game_over():
            current_agent = self.agents[self.board.current_player]
            
            try:
                # Vérifier le temps de décision de l'agent
                start_time = time.time()
                move = current_agent.make_move(self.board)
                end_time = time.time()
                
                decision_time = end_time - start_time
                if decision_time > 10.0:  # Plus de 10 secondes
                    if show_game:
                        print(f"TIMEOUT: L'agent {self.board.current_player.value} a pris {decision_time:.2f}s pour décider (limite: 10s)")
                    raise TimeoutError(f"Agent took {decision_time:.2f}s to make a move (limit: 10s)")
                
                if self.board.make_move(move, self.board.current_player):
                    self.move_history.append((self.board.current_player, move))
                    
                    if show_game:
                        print(f"Joueur {self.board.current_player.value} joue en position {move} (temps: {decision_time:.3f}s)")
                        print(self.board)
                        time.sleep(2)  # Pause de 2 secondes entre les tours
                    
                    # Changer de joueur
                    self.board.current_player = (Player.O if self.board.current_player == Player.X 
                                               else Player.X)
                else:
                    raise ValueError(f"Coup invalide: {move}")
                    
            except Exception as e:
                if show_game:
                    print(f"Erreur lors du coup du joueur {self.board.current_player.value}: {e}")
                return GameState.IN_PROGRESS
        
        result = self.board.check_winner()
        if show_game:
            if result == GameState.DRAW:
                print("Match nul!")
            else:
                winner = "X" if result == GameState.X_WINS else "O"
                print(f"Joueur {winner} gagne!")
        
        return result


def test_agent(losing_agent, opponent_agent, num_games: int = 100, agent_name: str = "Agent", show_games: bool = False) -> float:
    """
    Teste un agent perdant contre un adversaire.
    
    Args:
        losing_agent: L'agent qui doit perdre
        opponent_agent: L'agent adversaire
        num_games: Nombre de parties à jouer
        agent_name: Nom de l'adversaire pour l'affichage
        show_games: Activer l'affichage des parties
        
    Returns:
        Pourcentage de non-victoire (défaites + matchs nuls) de l'agent perdant (ou -1 si timeout)
    """
    losses = 0
    wins = 0
    draws = 0
    
    for i in range(num_games):
        try:
            # Afficher les parties si demandé
            if show_games:
                print(f"\n--- Partie {i+1}/{num_games} ---")
            
            # Alternance des joueurs X et O
            if i % 2 == 0:
                game = TicTacToeGame(losing_agent, opponent_agent)
                result = game.play_game(show_game=show_games)
                
                if result == GameState.O_WINS:  # L'adversaire (O) gagne
                    losses += 1
                elif result == GameState.X_WINS:  # L'agent perdant (X) gagne
                    wins += 1
                elif result == GameState.DRAW:
                    draws += 1
                # Si result == GameState.IN_PROGRESS, c'est une erreur (timeout)
                elif result == GameState.IN_PROGRESS:
                    print(f"TIMEOUT détecté lors de la partie {i+1} contre {agent_name}")
                    return -1  # Indicateur de timeout
            else:
                game = TicTacToeGame(opponent_agent, losing_agent)
                result = game.play_game(show_game=show_games)
                
                if result == GameState.X_WINS:  # L'adversaire (X) gagne
                    losses += 1
                elif result == GameState.O_WINS:  # L'agent perdant (O) gagne
                    wins += 1
                elif result == GameState.DRAW:
                    draws += 1
                # Si result == GameState.IN_PROGRESS, c'est une erreur (timeout)
                elif result == GameState.IN_PROGRESS:
                    print(f"TIMEOUT détecté lors de la partie {i+1} contre {agent_name}")
                    return -1  # Indicateur de timeout
        
        except TimeoutError as e:
            print(f"TIMEOUT détecté lors de la partie {i+1} contre {agent_name}: {e}")
            return -1  # Indicateur de timeout
        except Exception as e:
            print(f"Erreur lors de la partie {i+1} contre {agent_name}: {e}")
            return -1
    
    loss_percentage = (losses / num_games) * 100
    non_win_percentage = ((losses + draws) / num_games) * 100  # Défaites + matchs nuls
    print(f"Résultats contre {agent_name} ({num_games} parties):")
    print(f"  Défaites: {losses} ({loss_percentage:.1f}%)")
    print(f"  Victoires: {wins} ({(wins/num_games)*100:.1f}%)")
    print(f"  Matchs nuls: {draws} ({(draws/num_games)*100:.1f}%)")
    print(f"  Ratio de non-victoire (défaites + nuls): {non_win_percentage:.1f}%")
    print()
    
    return non_win_percentage

# Fonction pour importer depuis un fichier .pyc
def load_pyc_module(module_name, pyc_path):
    """Charge un module depuis un fichier .pyc"""
    spec = importlib.util.spec_from_file_location(module_name, pyc_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def main():
    """Fonction principale pour tester les agents."""
    print("=== Système de test Tic Tac Throw! ===")
    
    try:
        from pathlib import Path
                
        # Importer les agents depuis les .pyc
        compiled_dir = Path(__file__).parent / "compiled_agents"
        AgentAleatoire = load_pyc_module("agent_aleatoire", compiled_dir / "agent_aleatoire.pyc").AgentAleatoire
        AgentIntermediaire = load_pyc_module("agent_intermediaire", compiled_dir / "agent_intermediaire.pyc").AgentIntermediaire
        AgentExpert = load_pyc_module("agent_expert", compiled_dir / "agent_expert.pyc").AgentExpert
        
        from losing_agent import LosingAgent

        # Création de l'agent à tester (votre agent perdant)
        losing_agent = LosingAgent(Player.X)
        
        # Test contre l'agent aléatoire
        print("1. Test contre l'agent aléatoire")
        agent_aleatoire = AgentAleatoire(Player.O)
        loss_rate_random = test_agent(losing_agent, agent_aleatoire, 1000, "Agent Aléatoire")
        
        # Test contre l'agent intermédiaire
        print("2. Test contre l'agent intermédiaire")
        agent_intermediaire = AgentIntermediaire(Player.O)
        loss_rate_intermediate = test_agent(losing_agent, agent_intermediaire, 1000, "Agent Intermédiaire")
        
        # Test contre l'agent expert
        print("3. Test contre l'agent expert")
        agent_expert = AgentExpert(Player.O)
        loss_rate_expert = test_agent(losing_agent, agent_expert, 1000, "Agent Expert")
        
        # Vérifier s'il y a eu un timeout
        if loss_rate_random == -1 or loss_rate_intermediate == -1 or loss_rate_expert == -1:
            print("\n🚨 TIMEOUT DÉTECTÉ! 🚨")
            print("Votre agent a pris plus de 10 secondes pour prendre une décision.")
            print("RÉSULTAT FINAL: 0/15 points")
            return
        
        # Évaluation finale
        print("=== ÉVALUATION FINALE ===")
        total_points = 0
        
        if loss_rate_random >= 80:
            print(f"✓ Non-victoire contre agent aléatoire ({loss_rate_random:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-victoire contre agent aléatoire ({loss_rate_random:.1f}%): 0/5 points (besoin: 80%)")
        
        if loss_rate_intermediate >= 80:
            print(f"✓ Non-victoire contre agent intermédiaire ({loss_rate_intermediate:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-victoire contre agent intermédiaire ({loss_rate_intermediate:.1f}%): 0/5 points (besoin: 80%)")
        
        if loss_rate_expert >= 80:
            print(f"✓ Non-victoire contre agent expert ({loss_rate_expert:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-victoire contre agent expert ({loss_rate_expert:.1f}%): 0/5 points (besoin: 80%)")
        
        print(f"\nScore total: {total_points}/15 points")
        
    except ImportError as e:
        print(f"Erreur d'import: {e}")
        print("Assurez-vous que tous les fichiers d'agents sont présents.")
    except Exception as e:
        print(f"Erreur lors des tests: {e}")


if __name__ == "__main__":
    main()
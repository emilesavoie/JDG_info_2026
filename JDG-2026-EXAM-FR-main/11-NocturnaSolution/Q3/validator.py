import sys
import os
from collections import deque

# SCRIPT DE VALIDATION
# NE MODIFIEZ PAS CE FICHIER

# Force UTF-8 output for emojis on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

EMOJI_PASS = "\u2705"  # crochet vert
EMOJI_FAIL = "\u274C"  # X rouge

EMOJI_MAP = {
    '.': '⬜',
    'P': '🌿',
    'R': '🪑',
    'M': '☕',
    'C': '🧑',
    '#': '⬛'
}

def read_grid(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Erreur: Le fichier {filepath} est introuvable.")
        sys.exit(1)

def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_min_distance_to_set(point, target_set):
    if not target_set:
        return float("inf")
    return min(get_distance(point, target) for target in target_set)

def find_elements(grid):
    elements = {
        "C": [],
        "M": [],
        "R": [],
        "P": [],
        "#": [],
        ".": []
    }
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char in elements:
                elements[char].append((r, c))
    return elements, rows, cols

def check_grid_integrity(input_grid, output_grid):
    if len(input_grid) != len(output_grid):
        return False, f"Nombre de lignes incorrect ({len(output_grid)} vs {len(input_grid)})."
    
    if len(input_grid[0]) != len(output_grid[0]):
        return False, f"Nombre de colonnes incorrect ({len(output_grid[0])} vs {len(input_grid[0])})."
    
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    for r in range(rows):
        if len(output_grid[r]) != cols:
             return False, f"Ligne {r} de longueur incorrecte."
        for c in range(cols):
            if input_grid[r][c] == "#" and output_grid[r][c] != "#":
                return False, f"Mur manquant ou déplacé en ({r},{c})."
            if input_grid[r][c] != "#" and output_grid[r][c] == "#":
                return False, f"Mur ajouté illégalement en ({r},{c})."
    return True, "OK"


def render_grid_with_emojis(grid):
    lines = []
    for row in grid:
        line = ''.join(EMOJI_MAP.get(ch, '?') for ch in row)
        lines.append(line)
    return "\n".join(lines)

def check_chair_integrity(r_coords):
    # On s'attend à 4 "R" qui forment 2 groupes de 2 adjacents
    if len(r_coords) != 4:
        return False, f"Nombre incorrect de tuiles de fauteuil R: {len(r_coords)} (Attendu: 4 pour 2 fauteuils)"
    
    visited = set()
    chairs_found = 0
    
    for r_pos in r_coords:
        if r_pos in visited:
            continue
            
        # Chercher un voisin
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r_pos[0] + dr, r_pos[1] + dc
            if (nr, nc) in r_coords and (nr, nc) not in visited:
                neighbors.append((nr, nc))
        
        if len(neighbors) == 1:
            visited.add(r_pos)
            visited.add(neighbors[0])
            chairs_found += 1
        else:
            return False, f"Structure de fauteuil invalide autour de {r_pos}"
            
    if chairs_found == 2:
        return True, "OK"
    return False, f"Trouvé {chairs_found} fauteuils valides au lieu de 2."

def check_vital_space(grid, c_coords, rows, cols):
    for r, c in c_coords:
        # Vérifier les 8 voisins
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "C":
                        return False, f"Consultant en ({r},{c}) est trop proche de ({nr},{nc})"
    return True, "OK"

def check_accessibility(grid, elements, rows, cols):
    # Flood fill depuis le premier consultant
    if not elements["C"]:
        return False, "Pas de consultants pour tester l'accessibilité."
    
    start_node = elements["C"][0]
    queue = deque([start_node])
    visited = {start_node}
    
    reachable_targets = {
        "C": 0,
        "M": 0,
        "R": 0
    }
    
    # Compter le start node
    reachable_targets["C"] += 1
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                cell = grid[nr][nc]
                                
                if cell == ".":
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    # Trouver une case vide adjacente au premier consultant
    start_empty = None
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = start_node[0] + dr, start_node[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ".":
            start_empty = (nr, nc)
            break
            
    if not start_empty:
        return False, "Le premier consultant est enfermé (pas de case vide adjacente)."

    q = deque([start_empty])
    visited_empty = {start_empty}
    
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "." and (nr, nc) not in visited_empty:
                    visited_empty.add((nr, nc))
                    q.append((nr, nc))

    # Vérifier l'accessibilité de tous les objets requis
    required_access = elements["C"] + elements["M"] + elements["R"]
    
    for obj_r, obj_c in required_access:
        is_accessible = False
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = obj_r + dr, obj_c + dc
            if (nr, nc) in visited_empty:
                is_accessible = True
                break
        
        if not is_accessible:
            return False, f"L'objet en ({obj_r},{obj_c}) ({grid[obj_r][obj_c]}) n'est pas accessible par un chemin de cases vides."

    return True, "OK"

def calculate_score(grid, elements):
    total_score = 0
    
    machine_pos = elements["M"][0]
    chairs = elements["R"]
    
    print(f"\n{'Consultant':<12} | {'Café':<10} | {'Social':<10} | {'Plantes':<10} | {'Repos':<10} | {'Total':<10}")
    print("-" * 75)
    
    for i, c_pos in enumerate(elements["C"]):
        sub_score = 0
        
        # A. Café
        dist_m = get_distance(c_pos, machine_pos)
        score_m = 0
        if dist_m > 3:
            score_m = max(0, 15 - (dist_m * 2))
        sub_score += score_m
        
        # B. Social
        score_s = 0
        for other_c in elements["C"]:
            if c_pos == other_c: continue
            d = get_distance(c_pos, other_c)
            if d <= 2: score_s -= 10
            elif 3 <= d <= 6: score_s += 5
        sub_score += score_s
        
        # C. Plantes
        score_p = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr==0 and dc==0: continue
                nr, nc = c_pos[0] + dr, c_pos[1] + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == "P":
                        score_p += 1
        sub_score += score_p
        
        # D. Repos
        dist_r = get_min_distance_to_set(c_pos, chairs)
        score_r = 0
        if dist_r <= 3:
            score_r = 5
        sub_score += score_r
        
        total_score += sub_score
        print(f"C#{i+1} ({c_pos[0]:02},{c_pos[1]:02}) | {score_m:<10} | {score_s:<10} | {score_p:<10} | {score_r:<10} | {sub_score:<10}")
        
    return total_score

def main():
    if len(sys.argv) < 2:
        print("Usage: python validator.py <path_to_output_grid.txt> [path_to_input_grid.txt]")
        # Fallback pour test rapide si fichier existe
        if os.path.exists("output.txt"):
            output_filepath = "output.txt"
            input_filepath = "input_grid.txt"
        else:
            return
    else:
        output_filepath = sys.argv[1]
        input_filepath = sys.argv[2] if len(sys.argv) > 2 else "input_grid.txt"

    print(f"====== VALIDATEUR DE SOLUTION ======\n")

    print(f"Fichier de solution:        {output_filepath}")
    print(f"Fichier de layout initial:  {input_filepath}")
    
    output_grid = read_grid(output_filepath)
    input_grid = read_grid(input_filepath)
    
    # --- Rendu de la grille avec des emojis ---
    print("\n--- Grille de sortie (visualisation) ---")
    print(render_grid_with_emojis(output_grid))
    
    # --- Validation de l'intégrité de la grille ---
    ok_integrity, msg_integrity = check_grid_integrity(input_grid, output_grid)
    if not ok_integrity:
        print(f"{EMOJI_FAIL} Solution Invalide: {msg_integrity}")
        print("La grille de sortie doit avoir les mêmes dimensions et les mêmes murs que la grille d'entrée.")
        return
    print(f"{EMOJI_PASS} Intégrité de la grille (Dimensions et Murs)")

    elements, rows, cols = find_elements(output_grid)
    
    # --- Validation des Contraintes Strictes ---
    print("\n--- Vérification des Contraintes Strictes ---\n")
    
    # 1. Inventaire
    valid_inv = True
    if len(elements["C"]) != 7: print(f"{EMOJI_FAIL} Consultants: {len(elements['C'])}/7"); valid_inv = False
    if len(elements["M"]) != 1: print(f"{EMOJI_FAIL} Machine à Café: {len(elements['M'])}/1"); valid_inv = False
    if len(elements["R"]) != 4: print(f"{EMOJI_FAIL} Tuiles Fauteuil: {len(elements['R'])}/4 (pour 2 fauteuils)"); valid_inv = False
    
    if not valid_inv:
        return
    print(f"{EMOJI_PASS} Inventaire complet")

    # 2. Intégrité Fauteuils
    ok_chairs, msg_chairs = check_chair_integrity(elements["R"])
    if not ok_chairs:
        print(f"{EMOJI_FAIL} Fauteuils: {msg_chairs}")
        return
    print(f"{EMOJI_PASS} Intégrité des fauteuils")

    # 3. Espace Vital
    ok_vital, msg_vital = check_vital_space(output_grid, elements["C"], rows, cols)
    if not ok_vital:
        print(f"{EMOJI_FAIL} Espace Vital: {msg_vital}")
        return
    print(f"{EMOJI_PASS} Espace Vital")

    # 4. Accessibilité
    ok_access, msg_access = check_accessibility(output_grid, elements, rows, cols)
    if not ok_access:
        print(f"{EMOJI_FAIL} Accessibilité: {msg_access}")
        return
    print(f"{EMOJI_PASS} Accessibilité")
    
    # --- Calcul du Score ---
    print("\n--- Calcul du Score de Joie ---")
    final_score = calculate_score(output_grid, elements)
    print("-" * 75)
    print(f"SCORE FINAL DE JOIE: {final_score}\n")

if __name__ == "__main__":
    main()

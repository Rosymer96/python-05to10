#!/bin/bash

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

EXERCISES=(
    "ex0:ft_garden_intro.py"
    "ex1:ft_garden_data.py"
    "ex2:ft_plant_growth.py"
    "ex3:ft_plant_factory.py"
    "ex4:ft_garden_security.py"
    "ex5:ft_plant_types.py"
    "ex6:ft_garden_analytics.py"
)

echo -e "${BLUE}=== Iniciando validación de CodeCultivation ===${NC}\n"

for item in "${EXERCISES[@]}"; do
    dir="${item%%:*}"
    expected_file="${item#*:}"
    file_path="$dir/$expected_file"

    echo -e "${BLUE}Verificando $dir...${NC}"

    if [ ! -d "$dir" ]; then
        echo -e "  ${RED}[ERROR]${NC} Directorio $dir no encontrado."
        echo ""
        continue
    fi

    if [ ! -f "$file_path" ]; then
        echo -e "  ${RED}[ERROR]${NC} Falta '$expected_file'."
        echo ""
        continue
    else
        echo -e "  ${GREEN}[OK]${NC} Archivo encontrado."
    fi

    # 3. Flake8 (como módulo)
    echo -n "  flake8: "
    python3 -m flake8 "$file_path" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}PASS${NC}"
    else
        echo -e "${RED}FAIL${NC} (Ejecuta 'python3 -m flake8 $file_path' para ver errores)"
    fi

    # 4. Mypy (como módulo)
    echo -n "  mypy:   "
    python3 -m mypy "$file_path" --ignore-missing-imports > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}PASS${NC}"
    else
        echo -e "${RED}FAIL${NC} (Ejecuta 'python3 -m mypy $file_path' para ver errores)"
    fi
    echo ""
done

echo -e "${BLUE}=== Validación finalizada ===${NC}"
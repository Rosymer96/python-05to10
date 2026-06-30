#!/bin/bash
# Mi pipeline v1.0

echo "--- Limpiando caché ---"
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "--- Verificando Norma Flake8 ---"
python3 -m flake8 . --exclude=main.py

if [ $? -nq 0 ]; then
    echo "Error de estilo detectado."
    exit 1
fi

echo "Vinculando archivos para main.py..."
ln -sf ex0/ft_hello_garden.py .
ln -sf ex1/ft_plot_area.py .
ln -sf ex2/ft_harvest_total.py .
ln -sf ex3/ft_plant_age.py .
ln -sf ex4/ft_water_reminder.py .
ln -sf ex5/ft_count_harvest_iterative.py .
ln -sf ex5/ft_count_harvest_recursive.py .
ln -sf ex6/ft_garden_summary.py .
ln -sf ex7/ft_seed_inventory.py .

echo -e "Lanzando main.py..."
python3 main.py

find . -maxdepth 1 -type l -name "ft_*.py" -delete
find . -type d -name "__pycache__" -exec rm -rf {} +
# oa_water

Obstacle Avoidance (water) baseado no Ping1D..

## Função atual
- Leitura do sonar Ping1D via serial
- Retorna:
  - distance (mm)
  - confidence (%)

## Rodar fora do ROS
```bash
python3 src/oa_water/ping_reader.py

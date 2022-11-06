import services.generate_vitals as generate_vitals
import repository.monitor_db as db

for i in range(50000):
    generate_vitals.generate_vitals()

db.commit()
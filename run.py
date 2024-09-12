import sys
from app import create_app

from flask import Flask

app: Flask = create_app()

if __name__ == '__main__':
    with app.app_context():
        if len(sys.argv) > 1 and sys.argv[1] == 'seed':
            # seeder = DatabaseSeeder(db)
            # seeder.seed()
            print("Database seeded successfully")
        else:
            app.run(host="0.0.0.0", port=5001, debug=True)
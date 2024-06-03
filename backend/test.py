

try: 
    import psycopg2
    print("Psycopg2 is installed.") 
except ImportError: 
    print("Psycopg2 is not installed.")
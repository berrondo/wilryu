import sqlite3

conn = sqlite3.connect('module.db')

cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE taxa (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            datapath INTEGER,
            porta INTEGER,
            segundos INTEGER,
            nsegundos INTEGER,
            transmitidos INTEGER,
            recebidos INTEGER,
            taxa_recebidos INTEGER,
            errostx INTEGER,
            errosrx INTEGER
    );
    """)
except sqlite3.OperationalError:
    #raise
    pass

def manda_pro_banco(datapath, porta, segundos, nsegundos, transmitidos, recebidos, taxa_recebidos, errostx, errosrx):
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO taxa (datapath, porta, segundos, nsegundos, transmitidos, recebidos, taxa_recebidos, errostx, errosrx)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (datapath, porta, segundos, nsegundos, transmitidos, recebidos, taxa_recebidos, errostx, errosrx))
    conn.commit()

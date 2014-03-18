#encoding='utf8'
import MySQLdb
 
# SELECT INET_ATON("192.168.1.38");
# SELECT INET_NTOA(4294967295)

sql_dest_summary = """

CREATE TABLE dest_summary(
    dt DATETIME NOT NULL,
    dip INT(10) UNSIGNED NOT NULL,
    dport INT(8) UNSIGNED,
    dmac VARCHAR(18),
    ave_len INT(10) COMMENT 'average package length',
    flow_cnt INT COMMENT 'flow count',
    PRIMARY KEY (dt, dip)
)
"""

sql_dest_rank = """
CREATE TABLE dest_rank(
    dt DATETIME NOT NULL,
    dip INT(10) UNSIGNED UNSIGNED NOT NULL,
    dport INT(8) UNSIGNED,
    dmac VARCHAR(18),
    flow_cnt INT(4) UNSIGNED NOT NULL COMMENT 'rank for source IP',
    sip INT(10) UNSIGNED,
    sport INT(8) UNSIGNED,
    smac VARCHAR(18),
    PRIMARY KEY (dt, dip)
)
"""
# select * from dest_rank order by flow_cnt desc limit 20

def createdb():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='openflow')
        cur=conn.cursor()
        conn.select_db('test')
        
        cur.execute(sql_dest_summary)
        cur.execute(sql_dest_rank)
        """ 
        value=[1,'hi rollen']
        cur.execute('insert into test values(%s,%s)',value)
        values=[]
        for i in range(20):
            values.append((i,'hi rollen'+str(i)))
        cur.executemany('insert into test values(%s,%s)',values)
        cur.execute('update test set info="I am rollen" where id=3')
        """
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    print "create dest_summary, dest_rank"


if __name__ == "__main__":
    createdb()

import unittest
from mysql import connector
from datetime import datetime

class NormalDataIT(unittest.TestCase):
    def setUp(self):
        self.cnx = connector.connect(user='root', database='cjx', password='root', host='192.168.99.100')
        cursor = self.cnx.cursor()
        cursor.execute('''CREATE TABLE `mondata_jingsu20394` (
          `id` bigint(20) NOT NULL AUTO_INCREMENT,
          `collect_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
          `device_code` varchar(255) NOT NULL,
          `humidity` double DEFAULT NULL,
          `sensor_index` tinyint(4) NOT NULL,
          `temperature` double DEFAULT NULL,
          `create_time` datetime NOT NULL,
          `original_temp` double DEFAULT NULL,
          `original_humidity` double DEFAULT NULL,
          PRIMARY KEY (`id`)
        )''')

        cursor.execute('INSERT INTO xdevice(id, code, status, support_power_alarm) VALUES(%s,%s,%s,%s)', (1, 'Jingsu20394', '1', '1'))
        cursor.execute(
          ('INSERT INTO xsensor(id, collectTime, temperature, minTemp, maxTemp, humidity, minHumidity, maxHumidity, device_id, sensor_index)' 
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'), (1, datetime.now(), 10.0, 5.0, 20.0, 50.0, 40.0, 100.0, 1, 0))

        cursor.close()

        self.cnx.commit()


    def tearDown(self):
        cursor = self.cnx.cursor()
        cursor.execute('drop table mondata_jingsu20394')
        cursor.execute('delete from xsensor')
        cursor.execute('delete from xdevice')

        cursor.close()

        self.cnx.commit()
        self.cnx.close()

    def test_Test(self):
        print 'test'
        pass

if __name__ == '__main__':
    unittest.main()
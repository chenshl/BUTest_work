# coding:utf-8
# @author : csl
# @date   : 2018/07/18 16:15
# kafka生产者,测试kafka常用api

from pykafka import KafkaClient
import time

class kafka_producerTest(object):

    def __init__(self, host="127.0.0.1:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)

    def product_partition(self, message):
        """
        生产者分区查看，主要查看生产消息时offset的变化
        :return:
        """
        topic = self.client.topics[b"test"]
        partitions = topic.partitions
        print(u"查看所有分区{}".format(partitions))

        earliest_offset = topic.earliest_available_offsets()
        print(u"获取最早可用的offset{}".format(earliest_offset))

        # 生成消息之前查看offset
        last_offset = topic.latest_available_offsets()
        print(u"最近可用的offset{}".format(last_offset))

        # 同步生成消息
        producer = topic.get_producer(sync=True)
        producer.produce(bytes(message, encoding="utf-8"))  # 转换成bytes格式

        # 查看offset变化
        last_offset = topic.latest_available_offsets()
        print(u"最近可用的offset{}".format(last_offset))


    def producer_designated_partition(self):
        """
        往指定分区写消息，如果要控制打印到某个分区，
        需要在获取生产者的时候指定选区函数，
        并且在生产消息的时候额外指定一个key
        :return:
        """
        def assign_patition(pid, key):
            """
            指定特定分区, 这里测试写入第一个分区(id=0)
            :param pid: 为分区列表
            :param key:
            :return:
            """
            print("为消息分配partition {} {}".format(pid, key))
            return pid[0]
        topic = self.client.topics["test".encode()]
        producer = topic.get_producer(sync = True, partitioner=assign_patition)
        producer.produce(bytes(str(time.time()), encoding="utf-8"), partition_key=b"partition_key_0")


    def async_produce_message(self):
        """
        异步生产消息，消息会被推到一个队列里面，
        另外一个线程会在队列中消息大小满足一个阈值（min_queued_messages）
        或到达一段时间（linger_ms）后统一发送,默认5s
        :return:
        """
        topic = self.client.topics["test".encode()]
        last_offset = topic.latest_available_offsets()
        print(u"最近的偏移量 offset{}".format(last_offset))

        # 记录最初的偏移量
        old_offset = last_offset[0].offset[0]
        producer = topic.get_producer(sync = False, partitioner=lambda pid, key: pid[0])
        producer.produce(bytes(str(time.time()), encoding="utf-8"))
        s_time = time.time()
        while True:
            last_offset = topic.latest_available_offsets()
            print(u"最近可用offset{}".format(last_offset))
            if last_offset[0].offset[0] != old_offset:
                e_time = time.time()
                print("cost_time{}".format(e_time - s_time))
                break
            time.sleep(1)


    def get_produce_message_report(self):
        """
        查看异步发送消报告,默认会等待5s后才能获得报告
        """
        topic = self.client.topics["test".encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量{}".format(last_offset))
        producer = topic.get_producer(sync = False, delivery_reports=True , partitioner=lambda pid, key: pid[0])
        producer.produce(bytes(str(time.time()), encoding="utf-8"))
        s_time = time.time()
        delivery_report = producer.get_delivery_report()
        e_time = time.time()
        print(u"等待{}s，提交报告{}".format(e_time - s_time, delivery_report))
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量{}".format(last_offset))





    # def producersend2kafka(self):
    #     client = KafkaClient(hosts="127.0.0.1:9092")  # 可接受多个Clienthosts="192.168.1.1:9092, 192.168.1.2:9092"
    #     client.topics  # 查看所有topic
    #     topic = client.topics[b"test"]  # 选择一个topic
    #     producer = topic.get_producer()
    #     producer.produce(bytes(self.message, encoding='utf-8'))  # 转换为bytes类型



if __name__ == "__main__":
    # for i in range(1, 10):
    #     sendmessage = "test_python" + str(i)
    #     print(sendmessage)
    #     kafka_producer(sendmessage).producersend2kafka()

    kafka_ins = kafka_producerTest()
    # kafka_ins.producer_partition()
    # kafka_ins.producer_designated_partition()
    # kafka_ins.async_produce_message()
    for x in range(1, 11):
        kafka_ins.product_partition("hello world -" + str(x))
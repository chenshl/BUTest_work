# coding:utf-8
# @author : csl
# @date   : 2018/07/18 16:30
# kafka消费者

from pykafka import KafkaClient

class kafka_consumer(object):

    def __init__(self, host="127.0.0.1:9092"):

        self.host = host
        self.client = KafkaClient(hosts=self.host)

    # def consumer_connect_kafka(self):
    #     self.client = KafkaClient(hosts="127.0.0.1:9092")
    #     self.client.topics
    #     self.topic = self.client.topics[b"test"]
    #     self.consumer = self.topic.get_simple_consumer()
    #     for message in self.consumer:
    #         if message is not None:
    #             print(message.offset, message.value)

    def simple_consumer(self, offset=0):
        """
        消费者指定消费
        :param offset:
        :return:
        """
        topic = self.client.topics["test".encode()]
        partitions = topic.partitions
        last_offset = topic.latest_available_offsets()
        print("最近可用offset{}".format(last_offset))  # 查看所有分区
        consumer = topic.get_simple_consumer(b"simple_consumer_group",   # 指定分区进行消费
                                             partitions=[partitions[0]],
                                             auto_commit_enable=True,
                                             auto_commit_interval_ms=1,
                                             # zookeeper_connect='192.168.1.140:2181,192.168.1.141:2181,192.168.1.142:2181',  # 从zookeeper消费,zookeeper的默认端口为2181,这里就是连接多个zk
                                             reset_offset_on_start=False
                                             )
        offset_list = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset_list))  # 消费者拥有的分区offset的情况
        consumer.reset_offsets([(partitions[0], offset)])  # 设置offset
        # msg = consumer.consume()
        # print("消费{}".format(msg.value.decode()))
        # msg = consumer.consume()
        # print("消费{}".format(msg.value.decode()))
        # msg = consumer.consume()
        # print("消费{}".format(msg.value.decode()))
        offset = consumer.held_offsets
        for msg in consumer:
            if msg is not None:
                print("消费消息 {}".format(msg.value.decode('utf-8')))
        print("当前消费者分区offset情况{}".format(offset))


    def balance_consumer(self):
        """
        使用balance consumer去消费kafka
        :return:
        """
        topic = self.client.topics["test".encode()]
        # managed=True 设置后，使用新式reblance分区方法，不需要使用zk，而False是通过zk来实现reblance的需要使用zk
        consumer = topic.get_balanced_consumer(b"consumer_group_balanced2", managed=True)
        partitions = topic.partitions
        print("分区 {}".format(partitions))
        earliest_offsets = topic.earliest_available_offsets()
        print("最早可用offset {}".format(earliest_offsets))
        last_offsets = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offsets))
        offset = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset))
        while True:
            msg = consumer.consume()
            offset = consumer.held_offsets
            print("{}, 当前消费者分区offset情况{}".format(msg.value.decode(), offset))



if __name__ == "__main__":
    # kafka_consumer().consumer_connect_kafka()
    kafka_ins = kafka_consumer()
    kafka_ins.simple_consumer()
    # kafka_ins.balance_consumer()
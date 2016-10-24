使用方法及说明

# scanPort*.py <target_port> <start_ip-- end_ip> <number of threads>

功能：
扫描某个IP段
加上命令行使用帮助,使用“-h” 得到使用说明

修复bug:
单个线程只能做一次socket.connect_ex
将它放到循环里面后解决。



目前存在的bug:


多线程的输出时，由于未做处理，控制台上的输出不按顺序，可能会显的凌乱。   ----20160512


DATE


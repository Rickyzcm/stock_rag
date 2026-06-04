公司服务器—部署flato测试使用
名称：gd-hyperchain
公网IP: 47.96.101.189
私网IP: 10.0.0.112
用户名：hyperchain
密码: yXVH9e0nxfffu2oL

备注 ： 你用这台吧，上面有其他项目测试的链，你自己换个端口部一条试试吧

ssh hyperchain@47.96.101.189





# 尝试部署flato链
## 预计使用的端口
### node1
> jsonrpc  = 10081   
> grpcApi = 12001
> grpc  = 52011 # p2p

以上端口均需要检查
sudo netstat -nap | grep 10081

检查多个端口的占用情况
sudo netstat -tuln | grep -E ':(10081|10082|10083|10084|12001|12002|12003|12004|52011|52012|52013|52014)'

-- 使用 ss命令同理
sudo ss -tuln | grep -E ':(10081|10082|10083|10084|12001|12002|12003|12004|52011|52012|52013|52014)'

### node2
> jsonrpc  = 10082   
> grpcApi = 12002
> grpc  = 52012 # p2p

### node3
> jsonrpc  = 10083   
> grpcApi = 12003
> grpc  = 52013 # p2p

### node4
> jsonrpc  = 10084   
> grpcApi = 12004
> grpc  = 52014 # p2p


修改配置路径示例：
/home/hyperchain/zcmTest/node1/configuration/dynamic.toml 

/home/hyperchain/zcmTest/node2/configuration/dynamic.toml 

/home/hyperchain/zcmTest/node3/configuration/dynamic.toml 

/home/hyperchain/zcmTest/node4/configuration/dynamic.toml 

## 目标安装目录
### 期望安装目录：/data/zcmhc/

远程主机工作路径 /home/hyperchain/zcmTest

上传文件
Scp ./ hyperchain@47.96.101.189:/home/hyperchain/zcmTest/downloads

— 以 node1 为例
Flato 安装路径：/home/hyperchain/zcmTest/node1

节点安装
执行 ./deploy-local.sh -d /home/hyperchain/zcmTest/node4

Certs 路径 以 node1 为例 
《节点证书源路径》
/home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node1

/home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node1/CA/
/home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node1/certs/
将 CA certs 放入
/home/hyperchain/zcmTest/node1/namespaces/global/certs/


-- 总结数字证书和签证的复制脚本
-- node1


-- node2


-- node3


-- node4
cp -r /home/hyperchain/zcmTest/downloads/4a09cba1-d6d5-4047-86b2-9223c1e6f546/LICENSE /home/hyperchain/zcmTest/node4

cp -r /home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node4/CA /home/hyperchain/zcmTest/node4/namespaces/global/certs/

cp -r /home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node4/certs/ /home/hyperchain/zcmTest/node4/namespaces/global/certs/





配置动态链库
/home/hyperchain/zcmTest/node1/tools/lib

备份flato安装节点目录

tar -zcvf ~/flato-node1-backup.tar.gz ./node1 &
tar -zcvf ~/flato-node2-backup.tar.gz ./node2 &
tar -zcvf ~/flato-node3-backup.tar.gz ./node3 &
tar -zcvf ~/flato-node4-backup.tar.gz ./node4 

将备份文件批量移动位置
find ~ -maxdepth 1 -type f -name "flato-*.tar.gz" -exec mv {} ~/zcmTest/backup/ \;


启动前检查节点二进制程序是否可执行
./node1/flato --version
./node2/flato --version
./node3/flato --version
./node4/flato --version


节点安全证书配置 

### 节点2
cat ../node2/namespaces/global/certs/certs/node2.cert 
-----BEGIN CERTIFICATE-----
MIICSzCCAfCgAwIBAgIIHpymq2toz0QwCgYIKoZIzj0EAwIwSDELMAkGA1UEBhMC
Q04xEzARBgNVBAoTCkh5cGVyY2hhaW4xCTAHBgNVBAsTADEOMAwGA1UEAxMFbm9k
ZTExCTAHBgNVBCoTADAgFw0yNTExMTkwMDAwMDBaGA8yMTI1MTExOTAwMDAwMFow
UjELMAkGA1UEBhMCQ04xEzARBgNVBAoTCkh5cGVyY2hhaW4xDjAMBgNVBAsTBWVj
ZXJ0MQ4wDAYDVQQDEwVub2RlMjEOMAwGA1UEKhMFZWNlcnQwWTATBgcqhkjOPQIB
BggqhkjOPQMBBwNCAATBE9seO0cB7bepXwe8V2IDvbJgNwqIf4qAsjp4DorD0JqQ
YmAChDTOJuwasUzp4mdO9QTYeD3xXxfFgmv0Se2to4G3MIG0MA4GA1UdDwEB/wQE
AwIB7jAxBgNVHSUEKjAoBggrBgEFBQcDAgYIKwYBBQUHAwEGCCsGAQUFBwMDBggr
BgEFBQcDBDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSkJ2Ml+MMr23KZZlr+
c00z2d/dXjAfBgNVHSMEGDAWgBQGQmeXHflxfuRAam95e/U8i9KrATAQBgNVHREE
CTAHggVub2RlMjAMBgMqVgEEBWVjZXJ0MAoGCCqGSM49BAMCA0kAMEYCIQDQwilB
5fltUxNpK+XKROcE/OmDtv7bwjFeBLvXFQS9hQIhAJKoLYbnIkkYAeoxv2PiyNpH
6pVF4DCi88MxBde3JIS+
-----END CERTIFICATE-----


### 节点3
cat ../node3/namespaces/global/certs/certs/node3.cert 

-----BEGIN CERTIFICATE-----
MIICSzCCAfCgAwIBAgIIX/wbjBroIEswCgYIKoZIzj0EAwIwSDELMAkGA1UEBhMC
Q04xEzARBgNVBAoTCkh5cGVyY2hhaW4xCTAHBgNVBAsTADEOMAwGA1UEAxMFbm9k
ZTExCTAHBgNVBCoTADAgFw0yNTExMTkwMDAwMDBaGA8yMTI1MTExOTAwMDAwMFow
UjELMAkGA1UEBhMCQ04xEzARBgNVBAoTCkh5cGVyY2hhaW4xDjAMBgNVBAsTBWVj
ZXJ0MQ4wDAYDVQQDEwVub2RlMzEOMAwGA1UEKhMFZWNlcnQwWTATBgcqhkjOPQIB
BggqhkjOPQMBBwNCAARHUuTwFcCTk25+PBO9OYsxka5j2kfYdbNMyYfWAnUOKN8r
ex3nfbiy+1/3V8gaOmA7skp1RKZV0+oZJTtyeKFQo4G3MIG0MA4GA1UdDwEB/wQE
AwIB7jAxBgNVHSUEKjAoBggrBgEFBQcDAgYIKwYBBQUHAwEGCCsGAQUFBwMDBggr
BgEFBQcDBDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTsyob0GViw56LhBZ4y
EaIW21GHFjAfBgNVHSMEGDAWgBQGQmeXHflxfuRAam95e/U8i9KrATAQBgNVHREE
CTAHggVub2RlMzAMBgMqVgEEBWVjZXJ0MAoGCCqGSM49BAMCA0kAMEYCIQCclfSw
XTxtA+MvvfkZNw/bA+cKd3JBWipvES3LFWW9jAIhAMJi8XxKWQCYrQk16m+0WLjo
33lW9pUJ1J8viCm0hjfR
-----END CERTIFICATE-----


### 节点4
cat ../node4/namespaces/global/certs/certs/node4.cert 
-----BEGIN CERTIFICATE-----
MIICSjCCAfCgAwIBAgIIQyKJkl+Gi4kwCgYIKoZIzj0EAwIwSDELMAkGA1UEBhMC
Q04xEzARBgNVBAoTCkh5cGVyY2hhaW4xCTAHBgNVBAsTADEOMAwGA1UEAxMFbm9k
ZTExCTAHBgNVBCoTADAgFw0yNTExMTkwMDAwMDBaGA8yMTI1MTExOTAwMDAwMFow
UjELMAkGA1UEBhMCQ04xEzARBgNVBAoTCkh5cGVyY2hhaW4xDjAMBgNVBAsTBWVj
ZXJ0MQ4wDAYDVQQDEwVub2RlNDEOMAwGA1UEKhMFZWNlcnQwWTATBgcqhkjOPQIB
BggqhkjOPQMBBwNCAAQkZkHsOf5pMWcw8lmOypyzbQ0WyIWo3OYDkH2tPnSwoXK1
694oVoUhJojO77HN+UuZAVcPITyW4Su704o7D0h/o4G3MIG0MA4GA1UdDwEB/wQE
AwIB7jAxBgNVHSUEKjAoBggrBgEFBQcDAgYIKwYBBQUHAwEGCCsGAQUFBwMDBggr
BgEFBQcDBDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSB5/Jdvcj9NQDVb8YQ
6NBWKZkxUzAfBgNVHSMEGDAWgBQGQmeXHflxfuRAam95e/U8i9KrATAQBgNVHREE
CTAHggVub2RlNDAMBgMqVgEEBWVjZXJ0MAoGCCqGSM49BAMCA0gAMEUCIHq3aVk/
KRS6r1qG6NH8JvLwyF48cVEySApFpgsbNrZoAiEAuo7CxEJbNwNafdvhZoE/JJs7
3TJMLcWwICq1rqp5tcE=
-----END CERTIFICATE-----

将node1 的配置复制给其他3个节点
cp -r ./node1/configuration/global/ns_genesis.toml ./node2/configuration/global/ns_genesis.toml


打印启动日志== ns级别日志
tail -300f ~/zcmTest/node1/namespaces/global/data/logs/flato_2025-11-25

打印启动日志 == system 级别日志


下载Namespace 日志
scp -r hyperchain@47.96.101.189:/home/hyperchain/zcmTest/node4/namespaces/global/data/logs/ /Users/hyperchain/sshlogs/node4/namespace/


下载ystem 级别的日志
scp -r hyperchain@47.96.101.189:/home/hyperchain/zcmTest/node4/system/logs/ /Users/hyperchain/sshlogs/node4/system/



停止节点；
./node1/stop.sh & ./node2/stop.sh & ./node3/stop.sh & ./node4/stop.sh & wait

启动节点
./node1/start.sh & ./node2/start.sh & ./node3/start.sh & ./node4/start.sh & wait


打印节点CA

节点的sdk证书
【路径】  /home/hyperchain/zcmTest/downloads/2025-11-19_08_27_03_allcerts/hyperchain2.0/node1/sdkcerts

1. ssh登录远程服务器
ssh useername@ip

1. 获取网络信息
ip address show  也可以写 ip a

输出当前端口占用情况
netstat -tuln
其后的选项
-t  显示TCP连接
-u 显示UDP连接
-l  仅显示监听状态的端口
-n  显示IP地址和端口号，而不是尝试解析域名

1. 也可以使用 ss  -tuln  用于检查套接字统计信息的工具，也是 netstat 的替代品

lsof -i:\[port\]  这个就是查看制定特定的端口号被占用情况；

nmap 网络扫描工具  nmap -p \[端口号\]  主机名或IP地址

1. 查看当前服务器的用户和用户组信息
cat /etc/passwd

1. 查看当前登录用户的操作权限


1. 检查服务时间
date

1. 检查服务器配置
  - 查看CPU 主频

  - 查看CPU 核数

  - 查看内存大小

  - 查看挂载的文件系统大小
  df -h

1. 检查某一端口的占用情况
nestat -nap | grep \[port\]

1. 检查网络连通性
  - nt工具
  - nc命令
  - Python HTTP 模块


1. 检查系统字符集


1. 检查最大文件句柄数  -- 会有文件句柄数不足而导致系统宕机
ulimit -n  ### 期望结果是 65535


1. 传输文件
scp 命令如何使用
源文件和目标路径可以是本地路径或者远程路径

远程的user@remote_host:/path/...

scp  hyperchain@47.96.101.189

1. 压缩和解压缩文件

tar 命令 对应的压缩文件后缀是 tar / tar.gz


压缩文件
tar -zcvf  【目标文件名】 【源文件/文件夹(可以是多个，空格分隔)】
zip 


解压缩文件
tar -zxvf 【目标压缩文件】-C /path/

列出压缩文件中的内容
tar -ztvf 【目标压缩文件】



unzip 命令

修改文件名称 mv

rename 有可以制定模式的批量修改文件名

复制文件到指定目录
cp -r 递归目录下所有内容
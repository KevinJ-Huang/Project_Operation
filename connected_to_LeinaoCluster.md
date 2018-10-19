1.使用test.json提交，然后run起来

2.点击进任务。获得ssh秘钥，建立该文件。

3.终端输入：chmod 600 秘钥文件名

4.传数据：scp -i your_ssh_key -P -r your_ssh_port your_file root@ssh_ip:/userhome/
例如:sudo scp -i application_1537874394512_13348 -P 14516 -r /home/ustc-ee-huangjie/下载/MIT-FiveK/ root@202.38.95.226:/userhome/

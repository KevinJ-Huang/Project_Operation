1.使用test.json提交，然后run起来

2.点击进任务。获得ssh秘钥，建立该文件。

3.终端输入：chmod 600 秘钥文件名

4.传数据：scp -i your_ssh_key -P -r your_ssh_port your_file 你的用户名@ssh_ip:/userhome/

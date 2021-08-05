# TIL

구글이 일부 공개한 소름돋는 사진, 인공지능이 스스로 진화해버린 역사적인 순간

https://m.youtube.com/watch?v=_rs4CK5-ss0&feature=share

- 인공지능이 인공지능을 만들어냄

- 인공지능과 사람의 변곡점이 얼마 남지 않았다



 우분투 기반 자바 설치 및 환경 변수를 설정한다 

 sudo apt install openjdk-8-jdk

$ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 

$ export CLASSPATH=$JAVA_HOME/lib/*:. 

$ export JAVA_LIBRARY_PATH=$HADOOP_HOME/lib/native:$JAVA_LIBRARY_PATH 

$ export PATH=$PATH:$JAVA_HOME/bin

$ wget http://mirror.apache-kr.org/apache/hadoop/common/hadoop-3.2.2/hadoop-3.2.2.tar.gz



$ tar xvfz hadoop-3.1.2.tar.gz 

$ ls 

hadoop-3.1.2 hadoop-3.1.2.tar.gz 

$ cd hadoop-3.1.2 3. 

하둡 환경 변수를 설정한다.   

$ export HADOOP_HOME=$HOME/hadoop-3.1.2/  

$ export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar 

$ export HADOOP_COMMON_HOME=$HADOOP_PREFIX 

$ export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_PREFIX/lib/native 

$ export HADOOP_CONF_DIR=$HADOOP_PREFIX/etc/hadoop 

$ export HADOOP_HDFS_HOME=$HADOOP_PREFIX 

$ export HADOOP_MAPRED_HOME=$HADOOP_PREFIX 

$ export YARN_HOME=$HADOOP_PREFIX  

$ export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin 

환경 변수 설정값은 echo $변수명을 입력하면 해당 환경 변수값을 확인할 수 



NCS 및 학습모듈 검색

- 20. 정보통신

https://m.ncs.go.kr/unity/th03/ncsSearchMain.do

**세계 경제란?**

달러 (기축통화)

- 미국의 독점 

원장 관리 중앙화를 분산화하자는 개념의 시작 ⇒ 블록체인

중국이 기축통화를 위안화 (독점)하는게 목적 

- 미국와 동등하게
- 그래서 블록체인 기술 싫어한다 
- 미국도 싫어한다

분산 원장 기술 = 블록체인

4차 산업 혁명에서 블록체인 기술은 필요

- 그 중 한 분야가 가상화폐



vagrant 설치

https://www.vagrantup.com/

Vagrant Boxes 설치

https://app.vagrantup.com/anassbo/boxes/spark-in-action-box



시스템 고급 환경변수 할때, 사용자 변수와, 시스템 변수 차이점이 있을까요?

사용자 변수는 user defined 변수 이고, 시스템 변수는 windows OS자체에서 사용하는 변수입니다.